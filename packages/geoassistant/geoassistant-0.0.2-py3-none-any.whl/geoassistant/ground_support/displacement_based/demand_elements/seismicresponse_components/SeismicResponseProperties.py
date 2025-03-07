from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from geoassistant.seismic.SeismicEvent import SeismicEvent
    from geoassistant.ground_support.displacement_based.site_elements.Site import Site
    from geoassistant.ground_support.displacement_based.demand_elements.seismicresponse_components.SeismicResponseCalculations import SeismicResponseCalculations


class SeismicResponseProperties(object):

    def __init__(self):

        self.site: Optional['Site'] = None
        self.seismic_event: Optional['SeismicEvent'] = None

        self.peak_ground_velocity: Optional[float] = None  # PGV [m/s]

        self.calculations: Optional['SeismicResponseCalculations'] = None

    def setSite(self, site: 'Site') -> None:
        self.site = site
        self.calculations.checkParametersCalculation()

    def setSeismicEvent(self, seismic_event: 'SeismicEvent') -> None:
        self.seismic_event = seismic_event
        self.calculations.checkParametersCalculation()

    def setPeakGroundVelocity(self, peak_ground_velocity: Optional[float]) -> None:
        self.peak_ground_velocity = peak_ground_velocity
        self.calculations.checkParametersCalculation()

    def getSite(self) -> Optional['Site']:
        return self.site

    def getSeismicEvent(self) -> Optional['SeismicEvent']:
        return self.seismic_event

    def getPeakGroundVelocity(self) -> Optional[float]:
        return self.peak_ground_velocity

    def getPeakGroundAcceleration(self) -> Optional[float]:
        return self.calculations.getPeakGroundAcceleration()

    def getDTSI(self) -> Optional[float]:
        return self.calculations.getDTSI()

    def getStressLevelChange(self) -> Optional[float]:
        return self.calculations.getStressLevelChange()
