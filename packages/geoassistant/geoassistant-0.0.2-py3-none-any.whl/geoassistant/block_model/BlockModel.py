from typing import Optional, Type, Literal

import numpy as np

from geoassistant.block_model.components.BlockModelPositions import BlockModelPositions
from geoassistant.shared.BaseObject import BaseObject
from geoassistant.shared.SpatialObjectsCollection import SpatialObjectsCollection

from geoassistant.block_model.components.BlockModelProperties import BlockModelProperties
from geoassistant.block_model.components.BlockModelReader import BlockModelReader
from geoassistant.block_model.components.BlockModelWriter import BlockModelWriter
from geoassistant.block_model.components.BlockModelReporter import BlockModelReporter
from geoassistant.block_model.BlockModelField import BlockModelField


class BlockModel(SpatialObjectsCollection['BlockModel', 'UnitBlock'], BlockModelProperties):

    def __init__(self, name: Optional[str] = None):
        super().__init__(name=name)

        self.positions: BlockModelPositions = BlockModelPositions(self)
        self.writer: BlockModelWriter = BlockModelWriter(self)
        self.reporter: BlockModelReporter = BlockModelReporter(self)

    def __getitem__(self, field_id: str) -> Optional['BlockModelField']:
        return self.getField(field_id=field_id)

    def __getstate__(self):
        state = self.__dict__.copy()
        state.pop("table", None)
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        self.table = None

    def getCollectionClass(self) -> Type:
        return BlockModel

    def getElementsPositions(self) -> np.ndarray:
        return np.array([ev.getPosition().getValue() for ev in self])

    @classmethod
    def load(cls, filepath: str) -> 'BlockModel':
        return BlockModelReader.load(cls, filepath=filepath)

    def save(self, savepath: str) -> None:
        self.writer.save(savepath=savepath)

    def createVariablesReport(self, savepath: Optional[str]) -> None:
        self.reporter.createVariablesReport(savepath=savepath)
