import os
import pickle
import tempfile
import zipfile
from typing import TYPE_CHECKING, Optional

import pathlib

import pyarrow
import pyarrow.csv
import pyarrow.parquet

from geoassistant.block_model.BlockModelField import BlockModelField

if TYPE_CHECKING:
    from geoassistant.block_model.BlockModel import BlockModel


class BlockModelReader(object):

    @staticmethod
    def load(cls, filepath: str) -> 'BlockModel':

        extensions = pathlib.Path(filepath).suffixes
        extensions = [ext[1:] for ext in extensions]  # Deletes the point

        if len(extensions) != 1:
            joined_extension = '.'.join(extensions)
            raise ValueError(f"Extension '{joined_extension}' is not supported as Block Model input.")

        extension = extensions[0]

        if extension == 'gabm':
            return BlockModelReader.readGABMFile(filepath)
        elif extension == 'csv':
            return BlockModelReader.readCSVFile(cls, filepath)
        else:
            raise ValueError(f"Extension '{extension}' is not supported as Block Model input.")

    @staticmethod
    def readGABMFile(filepath: str) -> 'BlockModel':
        """
        Load a BlockModel instance from a .gabm file.
        """
        with zipfile.ZipFile(filepath, "r") as gabm_file:
            # Extract and load the serialized object
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pkl") as temp_file:
                temp_file_path = temp_file.name
            try:
                with gabm_file.open("data.pkl") as f:
                    with open(temp_file_path, "wb") as temp_out:
                        temp_out.write(f.read())

                with open(temp_file_path, "rb") as f:
                    block_model: 'BlockModel' = pickle.load(f)
            finally:
                os.remove(temp_file_path)

            # Extract and load the Parquet table, if it exists
            if "table.parquet" in gabm_file.namelist():
                with tempfile.NamedTemporaryFile(delete=False, suffix=".parquet") as temp_file:
                    temp_file_path = temp_file.name
                try:
                    with gabm_file.open("table.parquet") as f:
                        with open(temp_file_path, "wb") as temp_out:
                            temp_out.write(f.read())

                    block_model.setTable(table=pyarrow.parquet.read_table(temp_file_path))
                finally:
                    os.remove(temp_file_path)
            else:
                block_model.table = None  # Ensure table is None if not present

        return block_model

    @staticmethod
    def readCSVFile(cls, filepath: str) -> 'BlockModel':

        bm = cls()

        table: pyarrow.Table = pyarrow.csv.read_csv(input_file=filepath)

        bm.setTable(table=table)
        bm.setFieldsNames(table.schema.names)

        for field_name in bm.getFieldsNames():
            field = BlockModelField(block_model=bm, name=field_name)
            bm.addField(field=field)

        return bm
