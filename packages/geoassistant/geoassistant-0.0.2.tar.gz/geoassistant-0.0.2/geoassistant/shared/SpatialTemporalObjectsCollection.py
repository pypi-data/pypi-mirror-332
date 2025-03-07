from abc import abstractmethod
from typing import Optional, Type, TypeVar, TYPE_CHECKING, Generic

from geoassistant.shared.SpatialObjectsCollection import SpatialObjectsCollection
from geoassistant.shared.TemporalObjectsCollection import TemporalObjectsCollection

if TYPE_CHECKING:
    from geoassistant.shared.BaseCollection import BaseCollection
    from geoassistant.shared.SpatialTemporalObject import SpatialTemporalObject

CollectionType = TypeVar('CollectionType', bound='BaseCollection')
SpatialTemporalType = TypeVar('SpatialTemporalType', bound='SpatialTemporalObject')


class SpatialTemporalObjectsCollection(SpatialObjectsCollection[CollectionType, SpatialTemporalType],
                                       TemporalObjectsCollection[CollectionType, SpatialTemporalType],
                                       Generic[CollectionType, SpatialTemporalType]):

    def __init__(self, name: Optional[str] = None):
        super().__init__(name=name)

    @abstractmethod
    def getCollectionClass(self) -> Type: ...

