from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from geoassistant.ground_support.displacement_based.support_elements.BoltSystem import BoltSystem
    from geoassistant.ground_support.displacement_based.support_elements.SurfaceSupport import SurfaceSupport

    from geoassistant.ground_support.displacement_based.support_elements.supportsystem_components.SupportSystemCalculations import SupportSystemCalculations


class SupportSystemProperties(object):

    def __init__(self):
        self.bolt_system: Optional['BoltSystem'] = None
        self.surface_support: Optional['SurfaceSupport'] = None

        self.calculations: Optional['SupportSystemCalculations'] = None

    def setBoltSystem(self, bolt_system: 'BoltSystem') -> None:
        self.bolt_system = bolt_system
        self.calculations.checkCapacitiesCalculation()

    def setSurfaceSupport(self, surface_support: 'SurfaceSupport') -> None: ...

    def getBoltSystem(self) -> Optional['BoltSystem']:
        return self.bolt_system

    def getSurfaceSupport(self) -> Optional['SurfaceSupport']:
        return self.surface_support

    def getStaticCapacity(self) -> Optional[float]:
        return self.calculations.getStaticCapacity()

    def getDisplacementCapacity(self) -> Optional[float]:
        return self.calculations.getDisplacementCapacity()

    def getEnergyCapacity(self) -> Optional[float]:
        return self.calculations.getEnergyCapacity()
