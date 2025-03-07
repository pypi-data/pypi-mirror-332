from typing import TYPE_CHECKING, Any, Optional, List

import numpy as np
import pyarrow.compute

if TYPE_CHECKING:
    from geoassistant.block_model.BlockModelField import BlockModelField


class BlockModelFieldAnalyzer(object):

    def __init__(self, field: 'BlockModelField'):
        self.field: 'BlockModelField' = field

        self.data_type: Any = None
        self.is_categoric: Optional[bool] = None

        self.unique_values: Optional[List[Any]] = None

        self.random_values: Optional[List[Any]] = None

        self._analyzeData()

    def getDataType(self) -> Any:
        return self.data_type

    def isCategoric(self) -> bool:
        return self.is_categoric

    def getUniqueValues(self) -> Optional[List[Any]]:
        return self.unique_values

    def getRandomValues(self) ->  Optional[List[Any]]:
        return self.random_values

    def _analyzeData(self) -> None:
        data = self.field.getData(output_type='pyarrow')

        self.data_type = data.type

        unique_values = pyarrow.compute.unique(data)
        self.is_categoric = len(unique_values) < 30

        if self.is_categoric:
            self.unique_values = unique_values.to_pylist()

        random_indices = np.random.choice(len(data), size=10, replace=False)
        self.random_values = pyarrow.compute.take(data=data, indices=random_indices)
