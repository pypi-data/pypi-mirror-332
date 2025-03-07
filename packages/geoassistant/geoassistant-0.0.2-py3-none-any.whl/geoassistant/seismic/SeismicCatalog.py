import datetime
from typing import Optional, Dict, List, Any, Literal, Tuple, Type

from geoassistant.shared.BaseCatalog import BaseCatalog

from geoassistant.seismic.SeismicEvent import SeismicEvent
from geoassistant.seismic.SeismicEventsCollection import SeismicEventsCollection


class SeismicCatalog(BaseCatalog[SeismicEventsCollection, SeismicEvent]):

    def __init__(self,
                 filepath: str,
                 name: Optional[str] = None):
        super().__init__(filepath=filepath, name=name)

    def getElementClass(self) -> Type:
        return SeismicEvent

    def getCollectionClass(self) -> Type:
        return SeismicEventsCollection

    def setMomentAttributes(self, key: str, units: Literal['Nm']) -> None:
        self.fields_attributes['Moment'] = (key, units)
        for i, ev in enumerate(self.elements_collection):
            ev.setMoment(value=self.catalog_data[key][i], units=units)
        self.elements_collection.calculateMomentMetrics()

    def setEnergyAttributes(self, key: str, units: Literal['J', 'KJ', 'MJ']) -> None:
        self.fields_attributes['Energy'] = (key, units)
        for i, ev in enumerate(self.elements_collection):
            ev.setEnergy(value=self.catalog_data[key][i], units=units)

    def setLocalMagnitudeAttributes(self, key: str) -> None:
        self.fields_attributes['Local Magnitude'] = (key, None)
        for i, ev in enumerate(self.elements_collection):
            ev.setLocalMagnitude(value=self.catalog_data[key][i])
        self.elements_collection.calculateLocalMagnitudeMetrics()

    def getMomentAttributes(self) -> Optional[Tuple]:
        return self.fields_attributes['Moment']

    def getEvents(self) -> SeismicEventsCollection:
        return self.elements_collection
