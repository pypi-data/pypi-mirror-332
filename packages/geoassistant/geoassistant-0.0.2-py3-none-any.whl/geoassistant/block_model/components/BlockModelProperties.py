from typing import Optional, TYPE_CHECKING, List

import pyarrow


if TYPE_CHECKING:
    from geoassistant.block_model.BlockModelField import BlockModelField
    from geoassistant.block_model.components.BlockModelReader import BlockModelReader


class BlockModelProperties(object):

    def __init__(self):

        self.table: Optional[pyarrow.Table] = None

        self.positions: 'BlockModelPositions' = None

        self.fields_names: Optional[List[str]] = None
        self.fields: List['BlockModelField'] = []

        self.reader: Optional['BlockModelReader'] = None
        self.loadpath: Optional[str] = None

    def setTable(self, table: pyarrow.Table) -> None:
        self.table = table

    def setFieldsNames(self, fields_names: List[str]) -> None:
        self.fields_names = fields_names

    def addField(self, field: 'BlockModelField') -> None:
        self.fields += [field]

    def getTable(self) -> Optional[pyarrow.Table]:
        return self.table

    def getFieldsNames(self) -> Optional[List[str]]:
        return self.fields_names

    def getField(self, field_id: str) -> Optional['BlockModelField']:
        for f in self.fields:
            if f.getName() == field_id:
                return f
        else:
            raise ValueError(f"Field '{field_id}' not found in BlockModel.")

    def getLoadpath(self) -> Optional[str]:
        return self.loadpath
