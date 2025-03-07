from typing import TYPE_CHECKING, Literal, Union, Any, Optional, List

import numpy as np
import pyarrow

from geoassistant.shared.BaseObject import BaseObject

from geoassistant.block_model.field_components.BlockModelFieldAnalyzer import BlockModelFieldAnalyzer

if TYPE_CHECKING:
    from geoassistant.block_model.BlockModel import BlockModel


class BlockModelField(BaseObject):

    def __init__(self, block_model: 'BlockModel', name: str):
        super().__init__(name=name)

        self.block_model: 'BlockModel' = block_model
        self.column_index: int = self.block_model.getFieldsNames().index(self.name)

        self.analyzer: BlockModelFieldAnalyzer = BlockModelFieldAnalyzer(self)

    def getData(self, output_type: Literal['numpy', 'pyarrow'] = 'numpy') -> Union[np.ndarray, pyarrow.ChunkedArray]:
        table = self.block_model.getTable()
        data: pyarrow.ChunkedArray = table.column(self.column_index)

        if output_type == 'numpy':
            return data.to_numpy()
        else:
            return data

    def getDataType(self) -> Any:
        return self.analyzer.getDataType()

    def isCategoric(self) -> bool:
        return self.analyzer.isCategoric()

    def getUniqueValues(self) -> Optional[List[Any]]:
        return self.analyzer.getUniqueValues()

    def getRandomValues(self) -> Optional[List[Any]]:
        return self.analyzer.getRandomValues()
