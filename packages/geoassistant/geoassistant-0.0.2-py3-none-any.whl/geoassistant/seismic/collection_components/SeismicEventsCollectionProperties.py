from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from geoassistant.seismic.collection_components.SeismicEventsCollectionDataPlotter import SeismicEventsCollectionDataPlotter
    from geoassistant.seismic.collection_components.SeismicEventsCollectionMetrics import SeismicEventsCollectionMetrics


class SeismicEventsCollectionProperties(object):

    def __init__(self):

        self.data_plotter: Optional['SeismicEventsCollectionDataPlotter'] = None
        self.metrics: Optional['SeismicEventsCollectionMetrics'] = None

    def getMinimumLocalMagnitude(self) -> Optional[float]:
        return self.metrics.getMinimumLocalMagnitude()

    def getMaximumLocalMagnitude(self) -> Optional[float]:
        return self.metrics.getMaximumLocalMagnitude()

    def getAverageLocalMagnitude(self) -> Optional[float]:
        return self.metrics.getAverageLocalMagnitude()
