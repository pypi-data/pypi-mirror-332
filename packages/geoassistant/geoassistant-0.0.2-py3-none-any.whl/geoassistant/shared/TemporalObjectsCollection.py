import datetime
from typing import Optional, Type, TypeVar, Generic, TYPE_CHECKING
from abc import ABC, abstractmethod

import numpy as np

from geoassistant.shared.BaseCollection import BaseCollection

if TYPE_CHECKING:
    from geoassistant.shared.TemporalObject import TemporalObject

CollectionType = TypeVar('CollectionType', bound=BaseCollection)
TemporalType = TypeVar('TemporalType', bound='TemporalObject')


class TemporalObjectsCollection(BaseCollection[CollectionType, TemporalType], ABC, Generic[CollectionType, TemporalType]):

    def __init__(self, name: Optional[str] = None):
        super().__init__(name=name)

    @abstractmethod
    def getCollectionClass(self) -> Type: ...

    def getElementsDatetimes(self) -> np.ndarray:
        return np.array([ev.getDatetime() for ev in self])

    def getSubsetBetweenDatetimes(self, t0: datetime.datetime, t1: datetime.datetime) -> CollectionType:
        collection: CollectionType = self.getCollectionClass()()
        for ev in self:
            if t0 < ev.getDatetime() < t1:
                collection.addElement(element=ev)
        return collection
