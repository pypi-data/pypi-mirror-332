import os
import struct
import numpy as np
import numpy.typing as npt
from ..types import VectorInput


def ensure_absolute_path(file_path: str) -> str:
    """Convert relative path to absolute if needed."""
    if not os.path.isabs(file_path):
        return os.path.abspath(file_path)
    return file_path


def create_db_files(file_path: str, dimensions: int = 0):
    """
    Create vector storage files with initial header.
    Raises FileExistsError if any of the files already exist.
    """
    absolute_path = ensure_absolute_path(file_path)
    vector_count = 0

    # Pack header data: two 32-bit integers for vector_count and dimensions
    header = struct.pack('<ii', vector_count, dimensions)

    # Creates a new file and fails if it exists
    try:
        with open(absolute_path, 'xb') as f:
            f.write(header)
            # Force flush to disk
            f.flush()
            os.fsync(f.fileno())

    except FileExistsError as e:
        try:
            os.unlink(absolute_path)
        except FileNotFoundError:
            pass
        raise FileExistsError(
            f"One or more vector files already exist at {absolute_path}") from e


def file_exists(file_path: str) -> bool:
    """Check if a file exists at the given path."""
    return os.path.exists(file_path)


def get_float32_array(query_vec: VectorInput) -> np.ndarray:
    """Convert input vector to float32 numpy array.

    Args:
        query_vec: Input vector (numpy array, list, or sequence of numbers)

    Returns:
        numpy float32 array

    Raises:
        ValueError: If input is empty or None
    """
    # Check for None
    if query_vec is None:
        raise ValueError("Vector cannot be None")

    # For sequences (lists, tuples), check length
    if isinstance(query_vec, (list, tuple)) and len(query_vec) == 0:
        raise ValueError("Vector cannot be empty")

    # For numpy arrays, check size
    if isinstance(query_vec, np.ndarray) and query_vec.size == 0:
        raise ValueError("Vector cannot be empty")

    query_vec_float32: npt.NDArray[np.float32]
    if isinstance(query_vec, np.ndarray):
        if query_vec.dtype != np.float32:
            query_vec_float32 = query_vec.astype(np.float32)
        else:
            query_vec_float32 = query_vec
    else:
        query_vec_float32 = np.asarray(query_vec, dtype=np.float32)

    return query_vec_float32


def write_file_header(file_path: str, vectors: int, dims: int) -> None:
    """Write the tinyvec file header to initialize a file."""
    # Create a bytearray for the header data (8 bytes total)
    header = bytearray(8)

    # Write vectors count and dimensions as 32-bit integers
    struct.pack_into('<ii', header, 0, vectors, dims)

    try:
        # Open the file in write binary mode, creating it if it doesn't exist
        with open(file_path, 'wb') as f:
            f.write(header)
            # Force flush to disk
            f.flush()
            os.fsync(f.fileno())  # Ensure data is written to disk
    except Exception as e:
        raise RuntimeError(f"Failed to write file header: {e}") from e
