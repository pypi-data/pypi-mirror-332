from typing import Optional, Type, TypeVar, Generic, TYPE_CHECKING
from abc import ABC, abstractmethod

import numpy as np
from geogeometry import Sphere

from geoassistant.shared.BaseCollection import BaseCollection

if TYPE_CHECKING:
    from geoassistant.shared.SpatialObject import SpatialObject

CollectionType = TypeVar('CollectionType', bound=BaseCollection)
SpatialType = TypeVar('SpatialType', bound='SpatialObject')


class SpatialObjectsCollection(BaseCollection[CollectionType, SpatialType], ABC, Generic[CollectionType, SpatialType]):

    def __init__(self, name: Optional[str] = None):
        super().__init__(name=name)

    @abstractmethod
    def getCollectionClass(self) -> Type: ...

    def getElementsPositions(self) -> np.ndarray:
        return np.array([ev.getPosition().getValue() for ev in self])

    def getSubsetInsideSphere(self, sphere: 'Sphere') -> CollectionType:
        results = sphere.arePointsInside(points=self.getElementsPositions())
        collection: CollectionType = self.getCollectionClass()()
        for i, ev in enumerate(self):
            if results[i]:
                collection.addElement(element=ev)
        return collection
