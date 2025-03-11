import os

import fsspec
import numpy as np
import omfiles

from .test_utils import create_test_om_file

# def test_fsspec_backend():
#     fsspec_object = fsspec.open("test_files/read_test.om", "rb")

#     file = omfiles.FsSpecBackend(fsspec_object)
#     assert file.file_size == 144


def test_s3_reader():
    file_path = "openmeteo/data/dwd_icon_d2/temperature_2m/chunk_3960.om"
    fs = fsspec.filesystem("s3", anon=True)
    backend = fs.open(file_path, mode="rb")

    # Create reader over fs spec backend
    reader = omfiles.OmFilePyReader(backend)
    data = reader[57812:57813, 0:100]

    # Verify the data
    expected = [18.0, 17.7, 17.65, 17.45, 17.15, 17.6, 18.7, 20.75, 21.7, 22.65]
    np.testing.assert_array_almost_equal(data[:10], expected)


def test_s3_reader_with_cache():
    file_path = "openmeteo/data/dwd_icon_d2/temperature_2m/chunk_3960.om"
    fs = fsspec.filesystem(protocol="s3", anon=True)
    backend = fs.open(file_path, mode="rb", cache_type="mmap", block_size=1024, cache_options={"location": "cache"})

    # Create reader over fs spec backend
    reader = omfiles.OmFilePyReader(backend)
    data = reader[57812:57813, 0:100]

    # Verify the data
    expected = [18.0, 17.7, 17.65, 17.45, 17.15, 17.6, 18.7, 20.75, 21.7, 22.65]
    np.testing.assert_array_almost_equal(data[:10], expected)

def test_fsspec_reader_close():
    """Test that closing a reader with fsspec file object works correctly."""
    temp_file = "test_fsspec_close.om"

    try:
        create_test_om_file(temp_file)
        fs = fsspec.filesystem("file")

        # Test explicit closure
        with fs.open(temp_file, "rb") as f:
            reader = omfiles.OmFilePyReader(f)

            # Check properties before closing
            assert reader.shape == [5, 5]
            assert not reader.closed

            # Get data and verify
            data = reader[0:4, 0:4]
            assert data.dtype == np.float32
            assert data.shape == (4, 4)

            # Close and verify
            reader.close()
            assert reader.closed

            # Operations should fail after close
            try:
                _ = reader[0:4, 0:4]
                assert False, "Should fail on closed reader"
            except ValueError:
                pass

        # Test context manager
        with fs.open(temp_file, "rb") as f:
            with omfiles.OmFilePyReader(f) as reader:
                ctx_data = reader[0:4, 0:4]
                np.testing.assert_array_equal(ctx_data, data)

            # Should be closed after context
            assert reader.closed

        # Data obtained before closing should still be valid
        expected = [
            [0.0, 1.0, 2.0, 3.0],
            [5.0, 6.0, 7.0, 8.0],
            [10.0, 11.0, 12.0, 13.0],
            [15.0, 16.0, 17.0, 18.0],
        ]
        np.testing.assert_array_equal(data, expected)

    finally:
        if os.path.exists(temp_file):
            os.remove(temp_file)


def test_fsspec_file_actually_closes():
    """Test that the underlying fsspec file is actually closed."""
    temp_file = "test_fsspec_actual_close.om"

    try:
        create_test_om_file(temp_file)

        # Create tracked file handle
        fs = fsspec.filesystem("file")
        f = fs.open(temp_file, "rb")

        # Create, verify and close reader
        reader = omfiles.OmFilePyReader(f)
        assert reader.shape == [5, 5]
        dtype = reader.dtype
        assert dtype == np.float32
        reader.close()

        # File should be closed - verify by trying to read from it
        try:
            f.read(1)
            assert False, "File should be closed"
        except (ValueError, OSError):
            pass

    finally:
        if os.path.exists(temp_file):
            os.remove(temp_file)
