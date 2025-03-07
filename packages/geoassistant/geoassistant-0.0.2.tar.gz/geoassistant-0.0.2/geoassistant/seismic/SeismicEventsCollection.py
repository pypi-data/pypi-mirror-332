import datetime
from typing import List, TYPE_CHECKING, Optional, Type, Literal

import numpy as np
from matplotlib import pylab as py
from geoassistant.seismic.collection_components.SeismicEventsCollectionDataPlotter import SeismicEventsCollectionDataPlotter
from geoassistant.seismic.collection_components.SeismicEventsCollectionMetrics import SeismicEventsCollectionMetrics
from geoassistant.seismic.collection_components.SeismicEventsCollectionProperties import SeismicEventsCollectionProperties
from geoassistant.shared.SpatialTemporalObjectsCollection import SpatialTemporalObjectsCollection

if TYPE_CHECKING:
    from geoassistant.seismic.SeismicEvent import SeismicEvent


class SeismicEventsCollection(SpatialTemporalObjectsCollection['SeismicEventsCollection', 'SeismicEvent'], SeismicEventsCollectionProperties):

    def __init__(self, name: Optional[str] = None):
        super().__init__(name=name)

        self.data_plotter: SeismicEventsCollectionDataPlotter = SeismicEventsCollectionDataPlotter(self)
        self.metrics: SeismicEventsCollectionMetrics = SeismicEventsCollectionMetrics(self)

    def __str__(self) -> str:
        txt = ("SeismicEventsCollection("
               f"events={len(self)}, "
               f"first={self[0].getDatetime()}, "
               f"last={self[-1].getDatetime()})")
        return txt

    def getCollectionClass(self) -> Type:
        return SeismicEventsCollection

    def calculateMomentMetrics(self) -> None:
        self.metrics.calculateMomentMetrics()

    def calculateLocalMagnitudeMetrics(self) -> None:
        self.metrics.calculateLocalMagnitudeMetrics()

    def getEventsMagnitudes(self) -> np.ndarray:
        return np.array([ev.getLocalMagnitude() for ev in self])

    def getEventsMoment(self) -> np.ndarray:
        return np.array([ev.getMoment().getValue() for ev in self])

    def getSubsetWithinMagnitudes(self, lower_magnitude: Optional[float] = None,
                                  upper_magnitude: Optional[float] = None,
                                  include_limits: bool = False,
                                  include_lower_limit: bool = False,
                                  include_upper_limit: bool = False) -> 'SeismicEventsCollection':
        sc = SeismicEventsCollection()
        for i, ev in enumerate(self):
            if lower_magnitude is not None:
                if include_limits or include_lower_limit:
                    if ev.getLocalMagnitude() < lower_magnitude:
                        continue
                else:
                    if ev.getLocalMagnitude() <= lower_magnitude:
                        continue

            if upper_magnitude is not None:
                if include_limits or include_upper_limit:
                    if upper_magnitude < ev.getLocalMagnitude():
                        continue
                else:
                    if upper_magnitude <= ev.getLocalMagnitude():
                        continue
            sc.addElement(element=ev)

        sc.calculateLocalMagnitudeMetrics()
        return sc

    # def plotMagnitudeHistogram(self) -> None

    def getTimeInterval(self) -> datetime.timedelta:
        min_datetime = np.min(self.getElementsDatetimes())
        max_datetime = np.max(self.getElementsDatetimes())
        delta = max_datetime - min_datetime

        return delta

    def plotGR(self, interval: float) -> None:
        self.data_plotter.plotGR(interval=interval)

    def plotHazardCurve(self) -> None:
        self.data_plotter.plotHazardCurve()