from typing import TYPE_CHECKING, Dict, Optional

from geoassistant.shared.NumericalMetrics import NumericalMetrics

if TYPE_CHECKING:
    from geoassistant.seismic.SeismicEventsCollection import SeismicEventsCollection


class SeismicEventsCollectionMetrics(object):

    def __init__(self, collection: 'SeismicEventsCollection'):
        self.collection: 'SeismicEventsCollection' = collection

        self.magnitude: Optional[Dict[str, NumericalMetrics]] = None

        self.local_magnitude: Optional[NumericalMetrics] = None
        self.energy: Optional[NumericalMetrics] = None
        self.moment: Optional[NumericalMetrics] = None
        self.potency: Optional[NumericalMetrics] = None

    def calculateLocalMagnitudeMetrics(self) -> None:
        self.local_magnitude = NumericalMetrics(values=self.collection.getEventsMagnitudes())

    def calculateMomentMetrics(self) -> None:
        self.moment = NumericalMetrics(values=self.collection.getEventsMoment())

    def getMinimumLocalMagnitude(self) -> Optional[float]:
        return self.local_magnitude.getMinimum()

    def getMaximumLocalMagnitude(self) -> Optional[float]:
        return self.local_magnitude.getMaximum()

    def getAverageLocalMagnitude(self) -> Optional[float]:
        return self.local_magnitude.getAverage()
