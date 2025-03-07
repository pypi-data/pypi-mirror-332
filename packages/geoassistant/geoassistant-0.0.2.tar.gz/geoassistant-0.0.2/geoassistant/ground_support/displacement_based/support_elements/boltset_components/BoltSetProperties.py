from typing import Optional, TYPE_CHECKING

from geoassistant.ground_support.displacement_based.support_elements.boltset_components.BoltSetCalculations import BoltSetCalculations
from geoassistant.ground_support.displacement_based.support_elements.boltset_components.BoltSetPlotter import BoltSetPlotter

if TYPE_CHECKING:
    from geoassistant.ground_support.displacement_based.support_elements.Bolt import Bolt


class BoltSetProperties(object):

    def __init__(self):
        self.bolt: Optional['Bolt'] = None

        self.bolt_spacing: Optional[float] = None
        self.ring_spacing: Optional[float] = None

        self.calculations: Optional['BoltSetCalculations'] = None
        self.plotter: Optional['BoltSetPlotter'] = None

    def setBolt(self, bolt: 'Bolt') -> None:
        self.bolt = bolt
        self.calculations.checkCapacityCalculations()

    def setBoltSpacing(self, bolt_spacing: float) -> None:
        self.bolt_spacing = bolt_spacing
        self.calculations.checkSpacingCalculations()
        self.calculations.checkCapacityCalculations()

    def setRingSpacing(self, ring_spacing: float) -> None:
        self.ring_spacing = ring_spacing
        self.calculations.checkSpacingCalculations()
        self.calculations.checkCapacityCalculations()

    def getBolt(self) -> Optional['Bolt']:
        return self.bolt

    def getBoltSpacing(self) -> Optional[float]:
        return self.bolt_spacing

    def getRingSpacing(self) -> Optional[float]:
        return self.ring_spacing

    def getNormalizedSpacing(self) -> Optional[float]:
        return self.calculations.getNormalizedSpacing()

    def getBoltsPerArea(self) -> Optional[float]:
        return self.calculations.getBoltsPerArea()

    def getDi(self) -> Optional[float]:
        return self.bolt.getDi()

    def getDisplacementCapacity(self) -> Optional[float]:
        return self.bolt.getDisplacementCapacity()

    def getEnergyCapacity(self) -> Optional[float]:
        return self.calculations.getEnergyCapacity()

