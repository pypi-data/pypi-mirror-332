from typing import Optional, TypeVar, TYPE_CHECKING, Generic

from geoassistant.shared.BaseObject import BaseObject

from geoassistant.shared.BaseCollection import BaseCollection

CollectionType = TypeVar('CollectionType', bound='BaseCollection')
ElementType = TypeVar('ElementType', bound='BaseObject')


class BaseBin(BaseCollection[CollectionType, ElementType], Generic[CollectionType, ElementType]):

    def __init__(self, variable_id: str, name: Optional[str] = None):
        super().__init__(name=name)

        self.variable_id: str = variable_id

        self.lower_limit: Optional[float] = None
        self.upper_limit: Optional[float] = None

        self.mid_value: Optional[float] = None

    def setLowerLimit(self, lower_limit: float) -> None:
        self.lower_limit = lower_limit

    def setUpperLimit(self, upper_limit: float) -> None:
        self.upper_limit = upper_limit

    def getLowerLimit(self) -> float:
        return self.lower_limit

    def getUpperLimit(self) -> float:
        return self.upper_limit

    def getMidValue(self) -> float:
        return self.mid_value

    def calculateMidValue(self) -> None:
        self.mid_value = (self.lower_limit + self.upper_limit) / 2.
