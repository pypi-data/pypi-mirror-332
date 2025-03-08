import os

import numpy as np
import omfiles

from .test_utils import create_test_om_file


def test_write_om_roundtrip():
    temp_file = "test_file.om"

    try:
        create_test_om_file(temp_file)

        reader = omfiles.OmFilePyReader(temp_file)
        data = reader[0:5, 0:5]
        del reader

        assert data.shape == (5, 5)
        assert data.dtype == np.float32
        np.testing.assert_array_equal(
            data,
            [
                [0.0, 1.0, 2.0, 3.0, 4.0],
                [5.0, 6.0, 7.0, 8.0, 9.0],
                [10.0, 11.0, 12.0, 13.0, 14.0],
                [15.0, 16.0, 17.0, 18.0, 19.0],
                [20.0, 21.0, 22.0, 23.0, 24.0],
            ],
        )

    finally:
        os.remove(temp_file)


def test_round_trip_array_datatypes():
    shape = (5, 5, 5, 2)
    chunks = [2, 2, 2, 1]
    test_cases = [
        (np.random.rand(*shape).astype(np.float32), "float32"),
        (np.random.rand(*shape).astype(np.float64), "float64"),
        (np.random.randint(-128, 127, size=shape, dtype=np.int8), "int8"),
        (np.random.randint(-32768, 32767, size=shape, dtype=np.int16), "int16"),
        (np.random.randint(-2147483648, 2147483647, size=shape, dtype=np.int32), "int32"),
        (np.random.randint(-9223372036854775808, 9223372036854775807, size=shape, dtype=np.int64), "int64"),
        (np.random.randint(0, 255, size=shape, dtype=np.uint8), "uint8"),
        (np.random.randint(0, 65535, size=shape, dtype=np.uint16), "uint16"),
        (np.random.randint(0, 4294967295, size=shape, dtype=np.uint32), "uint32"),
        (np.random.randint(0, 18446744073709551615, size=shape, dtype=np.uint64), "uint64"),
    ]

    for test_data, dtype in test_cases:
        temp_file = f"test_file_{dtype}.om"

        try:
            # Write data
            writer = omfiles.OmFilePyWriter(temp_file)
            variable = writer.write_array(test_data, chunks=chunks, scale_factor=10000.0, add_offset=0.0)
            writer.close(variable)

            del writer

            # Read data back
            reader = omfiles.OmFilePyReader(temp_file)
            read_data = reader[:]
            del reader

            # Verify data
            assert read_data.dtype == test_data.dtype
            assert read_data.shape == test_data.shape
            # use assert_array_almost_equal since our floating point values are compressed lossy
            np.testing.assert_array_almost_equal(read_data, test_data, decimal=4)

        finally:
            # Always try to remove the temp file
            os.remove(temp_file)

def test_write_hierarchical_file():
    temp_file = "test_hierarchical.om"

    try:
        # Create test data
        root_data = np.random.rand(10, 10).astype(np.float32)
        child1_data = np.random.rand(5, 5).astype(np.float32)
        child2_data = np.random.rand(3, 3).astype(np.float32)

        # Write hierarchical structure
        writer = omfiles.OmFilePyWriter(temp_file)

        # Write child2 array
        child2_var = writer.write_array(
            child2_data,
            chunks=[1, 1],
            name="child2",
            scale_factor=100000.0
        )

        # Write attributes and get their variables
        meta1_var = writer.write_scalar(42.0, name="metadata1")
        meta2_var = writer.write_scalar(123, name="metadata2")
        meta3_var = writer.write_scalar(3.14, name="metadata3")

        # Write child1 array with attribute children
        child1_var = writer.write_array(
            child1_data,
            chunks=[2, 2],
            name="child1",
            scale_factor=100000.0,
            children=[meta1_var, meta2_var, meta3_var]
        )

        # Write root array with children
        root_var = writer.write_array(
            root_data,
            chunks=[5, 5],
            name="root",
            scale_factor=100000.0,
            children=[child1_var, child2_var]
        )

        # Finalize the file
        writer.close(root_var)
        del writer

        # Read and verify the data using OmFilePyReader
        reader = omfiles.OmFilePyReader(temp_file)

        # Verify root data
        read_root = reader[:]
        np.testing.assert_array_almost_equal(read_root, root_data, decimal=4)
        assert read_root.shape == (10, 10)
        assert read_root.dtype == np.float32

        # Get child readers
        child_metadata = reader.get_flat_variable_metadata()

        # Verify child1 data
        child1_reader = reader.init_from_variable(child_metadata["root/child1"])
        read_child1 = child1_reader[:]
        np.testing.assert_array_almost_equal(read_child1, child1_data, decimal=4)
        assert read_child1.shape == (5, 5)
        assert read_child1.dtype == np.float32

        # Verify child2 data
        child2_reader = reader.init_from_variable(child_metadata["root/child2"])
        read_child2 = child2_reader[:]
        np.testing.assert_array_almost_equal(read_child2, child2_data, decimal=4)
        assert read_child2.shape == (3, 3)
        assert read_child2.dtype == np.float32

        # Verify metadata attributes
        metadata_reader = reader.init_from_variable(child_metadata["root/child1/metadata1"])

        metadata = metadata_reader.get_scalar()
        assert metadata == 42.0
        assert metadata_reader.dtype == np.float64

        del reader
        del child1_reader
        del child2_reader
        del metadata_reader

    finally:
        if os.path.exists(temp_file):
            os.remove(temp_file)
