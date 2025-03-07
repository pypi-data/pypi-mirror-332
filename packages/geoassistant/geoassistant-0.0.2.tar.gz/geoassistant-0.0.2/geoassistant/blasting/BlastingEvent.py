import datetime
from typing import Optional, TYPE_CHECKING

from geogeometry import Sphere

from geoassistant.shared.SpatialTemporalObject import SpatialTemporalObject

if TYPE_CHECKING:
    from geoassistant.seismic.SeismicEventsCollection import SeismicEventsCollection


class BlastingEvent(SpatialTemporalObject):

    def __init__(self, name: Optional[str] = None):
        super().__init__(name=name)

    def __str__(self) -> str:
        txt = (f"BlastingEvent("
               f"name={self.name}, "
               f"position={self.position.getValue()}, "
               f"datetime={self.datetime.getValue()})")
        return txt

    def getSeismicEventsFromTimeOffset(self, seismic_events: 'SeismicEventsCollection', time_offset: datetime.timedelta) -> 'SeismicEventsCollection':
        t0 = self.getDatetime()
        return seismic_events.getSubsetBetweenDatetimes(t0=t0, t1=t0 + time_offset)

    def getSeismicEventsWithinDistance(self, seismic_events: 'SeismicEventsCollection', distance: float) -> 'SeismicEventsCollection':
        sphere = Sphere(center=self.getPosition().getValue(), radius=distance)
        return seismic_events.getSubsetInsideSphere(sphere=sphere)

    def getSeismicEventsFromDistanceAndTimeOffset(self, seismic_events: 'SeismicEventsCollection', distance: float, time_offset: datetime.timedelta) -> 'SeismicEventsCollection':
        sc = self.getSeismicEventsWithinDistance(seismic_events=seismic_events, distance=distance)
        return self.getSeismicEventsFromTimeOffset(seismic_events=sc, time_offset=time_offset)
