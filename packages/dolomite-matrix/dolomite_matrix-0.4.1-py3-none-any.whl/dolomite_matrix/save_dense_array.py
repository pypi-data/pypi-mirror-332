from typing import Tuple, Optional, Any, Dict, Union
import numpy
from dolomite_base import save_object, validate_saves
import delayedarray
import os
import h5py

from .choose_chunk_dimensions import choose_chunk_dimensions 
from . import _optimize_storage as optim
from . import _utils as ut


###################################################
###################################################


def _blockwise_write_to_hdf5(dhandle: h5py.Dataset, chunk_shape: Tuple, x: Any, placeholder: Any, buffer_size: int):
    masked = delayedarray.is_masked(x)
    is_string = numpy.issubdtype(dhandle.dtype, numpy.bytes_)
    if placeholder is not None:
        if is_string:
            placeholder = placeholder.encode("UTF8")
        else:
            placeholder = dhandle.dtype.type(placeholder)

    def _blockwise_dense_writer(pos: Tuple, block):
        if masked:
            block = ut.replace_mask_with_placeholder(block, placeholder, dhandle.dtype)

        # h5py doesn't want to convert from numpy's Unicode type to bytes
        # automatically, and fails: so fine, we'll do it ourselves.
        if is_string: 
            block = block.astype(dhandle.dtype, copy=False)

        # Block processing is inherently Fortran-order based (i.e., first
        # dimension is assumed to change the fastest), and the blocks
        # themselves are also in F-contiguous layout (i.e., column-major). By
        # comparison HDF5 uses C order. To avoid any rearrangement of data
        # by h5py, we save it as a transposed array for efficiency.
        coords = [slice(start, end) for start, end in reversed(pos)]
        dhandle[(*coords,)] = block.T

    # Cost factor doesn't really matter here as we're not choosing between grids.
    grid = delayedarray.chunk_shape_to_grid(chunk_shape, x.shape, cost_factor=10)
    delayedarray.apply_over_blocks(x, _blockwise_dense_writer, grid = grid, buffer_size = buffer_size)
    return


def _blockwise_write_to_hdf5_vls(phandle: h5py.Dataset, hhandle: h5py.Dataset, chunk_shape: Tuple, x: Any, placeholder: Any, buffer_size: int):
    masked = delayedarray.is_masked(x)
    if placeholder is not None:
        placeholder = placeholder.encode("UTF8")

    heap_counter = 0

    def _blockwise_dense_writer(pos: Tuple, block):
        current_strings = numpy.ravel(block, order="F").astype("S")
        current_pointers = numpy.ndarray(current_strings.shape, dtype=numpy.dtype([('offset', 'u8'), ('length', 'u8')]))
        current_heap = []

        nonlocal heap_counter
        old_heap = heap_counter

        if placeholder is None:
            for i, x in enumerate(current_strings):
                current_pointers[i] = (heap_counter + len(current_heap), len(x))
                current_heap += list(x)
        else:
            for i, x in enumerate(current_strings):
                if current_strings.mask[i]:
                    encoded = placeholder
                else:
                    encoded = x
                current_pointers[i] = (heap_counter + len(current_heap), len(encoded))
                current_heap += list(encoded)

        # Block processing is inherently Fortran-order based (i.e., first
        # dimension is assumed to change the fastest), and the blocks
        # themselves are also in F-contiguous layout (i.e., column-major). By
        # comparison HDF5 uses C order. To avoid any rearrangement of data
        # by h5py, we save it as a transposed array for efficiency.
        coords = [slice(start, end) for start, end in reversed(pos)]
        phandle[(*coords,)] = numpy.reshape(current_pointers, (*reversed(block.shape),), order="C")
        heap_counter += len(current_heap)
        hhandle[old_heap:heap_counter] = current_heap

    # Cost factor doesn't really matter here as we're not choosing between grids.
    grid = delayedarray.chunk_shape_to_grid(chunk_shape, x.shape, cost_factor=10)
    delayedarray.apply_over_blocks(x, _blockwise_dense_writer, grid = grid, buffer_size = buffer_size)
    return


###################################################
###################################################


def _save_dense_array(
    x: numpy.ndarray, 
    path: str, 
    dense_array_chunk_dimensions: Optional[Tuple[int, ...]] = None, 
    dense_array_chunk_args: Dict = {},
    dense_array_buffer_size: int = 1e8, 
    dense_array_string_vls: bool = False,
    **kwargs
):
    os.mkdir(path)

    # Coming up with a decent chunk size.
    if dense_array_chunk_dimensions is None:
        dense_array_chunk_dimensions = choose_chunk_dimensions(x.shape, x.dtype.itemsize, **dense_array_chunk_args)
    else:
        capped = []
        for i, d in enumerate(x.shape):
            capped.append(min(d, dense_array_chunk_dimensions[i]))
        dense_array_chunk_dimensions = (*capped,)

    # Choosing the smallest data type that we can use.
    tt = None
    blockwise = False 
    if numpy.issubdtype(x.dtype, numpy.integer):
        tt = "integer"
        opts = optim.optimize_integer_storage(x, buffer_size = dense_array_buffer_size)

    elif numpy.issubdtype(x.dtype, numpy.floating):
        tt = "number"
        opts = optim.optimize_float_storage(x, buffer_size = dense_array_buffer_size)

    elif x.dtype == numpy.bool_:
        tt = "boolean"
        opts = optim.optimize_boolean_storage(x, buffer_size = dense_array_buffer_size)

    elif numpy.issubdtype(x.dtype, numpy.str_):
        opts = optim.optimize_string_storage(x, buffer_size = dense_array_buffer_size)
        max_len, total_len = opts.type
        if dense_array_string_vls is None:
            # i.e., is it worth replacing fixed-length strings with pointers to a VLS array?
            dense_array_string_vls = x.size * max_len > x.size * 16 + total_len 
        if dense_array_string_vls:
            tt = "vls"
        else:
            tt = "string"
        blockwise = True

    else:
        raise NotImplementedError("cannot save dense array of type '" + x.dtype.name + "'")

    if opts.placeholder is not None:
        blockwise = True
    if not isinstance(x, numpy.ndarray):
        blockwise = True
    
    fpath = os.path.join(path, "array.h5")
    with h5py.File(fpath, "w") as handle:
        ghandle = handle.create_group("dense_array")
        ghandle.attrs["type"] = tt

        if not blockwise:
            # Saving it in transposed form if it's in Fortran order (i.e., first dimensions are fastest).
            # This avoids the need for any data reorganization inside h5py itself.
            if x.flags.f_contiguous:
                x = x.T
                dense_array_chunk_dimensions = (*reversed(dense_array_chunk_dimensions),)
                ghandle.attrs.create("transposed", data=1, dtype="i1")
            else:
                ghandle.attrs.create("transposed", data=0, dtype="i1")
            dhandle = ghandle.create_dataset("data", data=x, chunks=dense_array_chunk_dimensions, dtype=opts.type, compression="gzip")

        else:
            # Block processing of a dataset is always Fortran order, but HDF5 uses C order.
            # So, we save the blocks in transposed form for efficiency.
            ghandle.attrs.create("transposed", data=1, dtype="i1")
            revshape = (*reversed(x.shape),)
            revchunks = (*reversed(dense_array_chunk_dimensions),)
            maxlen, totallen = opts.type

            if not dense_array_string_vls:
                outtype = opts.type
                if tt == "string":
                    outtype = h5py.string_dtype(encoding = "utf8", length = max(1, max_len))
                dhandle = ghandle.create_dataset("data", shape=revshape, chunks=revchunks, dtype=outtype, compression="gzip")
                _blockwise_write_to_hdf5(dhandle, chunk_shape=dense_array_chunk_dimensions, x=x, placeholder=opts.placeholder, buffer_size=dense_array_buffer_size) 
                if opts.placeholder is not None:
                    dhandle.attrs.create("missing-value-placeholder", data=opts.placeholder, dtype=outtype)

            elif tt == "vls":
                phandle = ghandle.create_dataset("pointers", shape=revshape, chunks=revchunks, dtype=numpy.dtype([('offset', 'u8'), ('length', 'u8')]), compression="gzip")
                hhandle = ghandle.create_dataset("heap", shape=(total_len,), dtype=numpy.dtype('u1'), compression="gzip", chunks=True)
                _blockwise_write_to_hdf5_vls(phandle, hhandle, chunk_shape=dense_array_chunk_dimensions, x=x, placeholder=opts.placeholder, buffer_size=dense_array_buffer_size) 
                if opts.placeholder is not None:
                    phandle.attrs["missing-value-placeholder"] = opts.placeholder

    with open(os.path.join(path, "OBJECT"), "w") as handle:
        handle.write('{ "type": "dense_array", "dense_array": { "version": "1.1" } }')


###################################################
###################################################


@save_object.register
@validate_saves
def save_dense_array_from_ndarray(
    x: numpy.ndarray, 
    path: str, 
    dense_array_chunk_dimensions: Optional[Tuple[int, ...]] = None, 
    dense_array_chunk_args: Dict = {},
    dense_array_buffer_size: int = 1e8,
    dense_array_string_vls: bool = False,
    **kwargs
):
    """
    Method for saving :py:class:`~numpy.ndarray` objects to disk, see
    :py:meth:`~dolomite_base.save_object.save_object` for details.

    Args:
        x: Object to be saved.

        path: Path to a directory to save ``x``.

        dense_array_chunk_dimensions: 
            Chunk dimensions for the HDF5 dataset. Larger values improve
            compression at the potential cost of reducing random access
            efficiency. If not provided, we choose some chunk sizes with
            :py:meth:`~dolomite_matrix.choose_chunk_dimensions.choose_chunk_dimensions`.

        dense_array_chunk_args: 
            Arguments to pass to ``choose_chunk_dimensions`` if
            ``dense_array_chunk_dimensions`` is not provided.

        dense_array_buffer_size:
            Size of the buffer in bytes, for blockwise processing and writing
            to file. Larger values improve speed at the cost of memory.

        kwargs: Further arguments, ignored.

    Returns:
        ``x`` is saved to ``path``.
    """
    _save_dense_array(
        x, 
        path=path, 
        dense_array_chunk_dimensions=dense_array_chunk_dimensions,
        dense_array_chunk_args = dense_array_chunk_args,
        dense_array_buffer_size = dense_array_buffer_size,
        dense_array_string_vls = dense_array_string_vls,
        **kwargs
    )
