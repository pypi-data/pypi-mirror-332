import math
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from geoassistant.ground_support.displacement_based.support_elements.BoltSystem import BoltSystem


class BoltSystemCalculations(object):

    def __init__(self, bolt_system: 'BoltSystem'):
        self.bolt_system: 'BoltSystem' = bolt_system

        self.di: Optional[float] = None
        self.equivalent_spacing: Optional[float] = None

        self.displacement_capacity: Optional[float] = None
        self.energy_capacity: Optional[float] = None

    def getDi(self) -> Optional[float]:
        return self.di

    def getEquivalentSpacing(self) -> Optional[float]:
        return self.equivalent_spacing

    def getDisplacementCapacity(self) -> Optional[float]:
        return self.displacement_capacity

    def getEnergyCapacity(self) -> Optional[float]:
        return self.energy_capacity

    def calculateInititalDisplacement(self) -> None:
        self.di = min([bs.getBolt().getDi() for bs in self.bolt_system])

    def calculateEquivalentSpacing(self) -> None:
        n_bolt_sets = len(self.bolt_system)

        if not n_bolt_sets:
            return

        if n_bolt_sets == 1:
            self.equivalent_spacing = self.bolt_system[0].getNormalizedSpacing()

        elif n_bolt_sets == 2:

            bs1 = self.bolt_system[0]
            bs2 = self.bolt_system[1]

            if bs1.getRingSpacing() == bs2.getRingSpacing() and bs1.getBoltSpacing() == bs2.getBoltSpacing():
                ring_term = (bs1.getRingSpacing() / 2.) ** 2
                bolt_term = (bs1.getBoltSpacing() / 2.) ** 2
                self.equivalent_spacing = math.sqrt(ring_term + bolt_term)
            else:
                self.equivalent_spacing = 1. / (bs1.getBoltsPerArea() + bs2.getBoltsPerArea())
                # raise ValueError("On development.")

        else:
            raise ValueError("Only up to 2 bolt sets.")

    def calculateDisplacementCapacity(self) -> None:
        self.displacement_capacity = max([bs.getDisplacementCapacity() for bs in self.bolt_system])

    def calculateEnergyCapacity(self) -> None:
        self.energy_capacity = sum([bs.getEnergyCapacity() for bs in self.bolt_system])

    def calculateUsedEnergyAtDisplacement(self, displacement: float) -> Optional[float]:
        y = 0
        for bs in self.bolt_system:
            y += bs.calculateUsedEnergyAtDisplacement(displacement=displacement)
        return y

    def updateCalculations(self) -> None:
        self.calculateInititalDisplacement()

        self.calculateDisplacementCapacity()
        self.calculateEnergyCapacity()

        self.calculateEquivalentSpacing()
