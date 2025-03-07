import datetime
from typing import Optional, TYPE_CHECKING, Type

import matplotlib.pyplot as plt

from geoassistant.seismic.SeismicEventsCollection import SeismicEventsCollection
from geoassistant.shared.SpatialTemporalObjectsCollection import SpatialTemporalObjectsCollection

if TYPE_CHECKING:
    from geoassistant.blasting.BlastingEvent import BlastingEvent


class BlastingEventsCollection(SpatialTemporalObjectsCollection['BlastingEventsCollection', 'BlastingEvent']):

    def __init__(self, name: Optional[str] = None):
        super().__init__(name=name)

    def getCollectionClass(self) -> Type:
        return BlastingEventsCollection

    def plotSeisman(self, seismic_events: 'SeismicEventsCollection') -> None:
        fig = plt.figure()
        ax = fig.add_subplot(111)

        dates = seismic_events.getElementsDatetimes()
        magnitudes = seismic_events.getEventsMagnitudes()

        ax.scatter(dates, magnitudes, alpha=0.3)

        for be in self:
            date = be.getDatetime()
            if date is not None:
                ax.axvline(x=date, c='black', lw=1)

        ax.set_ylabel("Local Magnitude")

        plt.show()

    def plotSeismanWithTimeControl(self, seismic_events: 'SeismicEventsCollection', time_offset: datetime.timedelta):
        fig = plt.figure()
        ax = fig.add_subplot(111)

        for be in self:
            date = be.getDatetime()
            if date is None:
                continue

            ax.axvline(x=date, c='black', lw=1)

            se = be.getSeismicEventsFromTimeOffset(seismic_events=seismic_events, time_offset=time_offset)

            dates = se.getElementsDatetimes()
            magnitudes = se.getEventsMagnitudes()
            ax.scatter(dates, magnitudes, alpha=0.3, c='blue')

        ax.set_ylabel("Local Magnitude")

        plt.show()