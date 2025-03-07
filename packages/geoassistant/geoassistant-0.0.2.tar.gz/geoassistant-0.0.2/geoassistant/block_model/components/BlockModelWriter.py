import os
import pickle
import tempfile
import zipfile

from typing import TYPE_CHECKING

import pyarrow.parquet

if TYPE_CHECKING:
    from geoassistant.block_model.BlockModel import BlockModel


class BlockModelWriter(object):

    def __init__(self, block_model: 'BlockModel'):
        self.block_model: 'BlockModel' = block_model

    def save(self, savepath: str) -> None:

        with zipfile.ZipFile(savepath, "w") as gabm_file:

            if self.block_model.getTable():
                with tempfile.NamedTemporaryFile(delete=False, suffix=".parquet") as temp_file:
                    temp_file_path = temp_file.name
                try:
                    pyarrow.parquet.write_table(self.block_model.getTable(), temp_file_path, compression="BROTLI")
                    gabm_file.write(temp_file_path, arcname="table.parquet")
                finally:
                    os.remove(temp_file_path)

            with tempfile.NamedTemporaryFile(delete=False, suffix=".pkl") as temp_file:
                temp_file_path = temp_file.name
            try:
                with open(temp_file_path, 'wb') as f:
                    pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)
                gabm_file.write(temp_file_path, arcname="data.pkl")
            finally:
                os.remove(temp_file_path)