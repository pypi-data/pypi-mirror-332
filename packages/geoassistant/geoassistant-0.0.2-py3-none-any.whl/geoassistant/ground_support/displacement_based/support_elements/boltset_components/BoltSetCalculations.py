from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from geoassistant.ground_support.displacement_based.support_elements.BoltSet import BoltSet


class BoltSetCalculations(object):

    def __init__(self, bolt_set: 'BoltSet'):
        self.bolt_set: 'BoltSet' = bolt_set

        self.normalized_spacing: Optional[float] = None
        self.bolts_per_area: Optional[float] = None

        self.energy_capacity: Optional[float] = None

    def getNormalizedSpacing(self) -> Optional[float]:
        return self.normalized_spacing

    def getBoltsPerArea(self) -> Optional[float]:
        return self.bolts_per_area

    def getEnergyCapacity(self) -> Optional[float]:
        return self.energy_capacity

    def calculateNormalizedSpacing(self) -> None:
        bs = self.bolt_set.getBoltSpacing()
        rs = self.bolt_set.getRingSpacing()

        self.normalized_spacing = (bs + rs) / 2.

    def calculateBoltsPerArea(self) -> None:
        self.bolts_per_area = (1 / self.normalized_spacing) ** 2

    def calculateEnergyCapacity(self) -> None:
        bolt = self.bolt_set.getBolt()

        work_capacity_D = self.bolts_per_area * bolt.getFm_D() * (bolt.getDu_D() / 1000.)
        work_capacity_ID = self.bolts_per_area * bolt.getFm_ID() * (bolt.getDu_ID() / 1000.)

        dsf = bolt.getDisplacementSplitFactor()

        self.energy_capacity = dsf * work_capacity_D + (1 - dsf) * work_capacity_ID

    def calculateUsedEnergyAtDisplacement(self, displacement: float) -> Optional[float]:
        if displacement < 0.:
            raise ValueError(f"Trying to evaluate using negative displacement: {displacement} [mm]")

        if displacement <= self.bolt_set.getDi():
            return 0

        if displacement >= self.bolt_set.getDisplacementCapacity():
            return self.bolt_set.getEnergyCapacity()

        y = (displacement - self.bolt_set.getDi()) * (self.bolt_set.getEnergyCapacity() / (self.bolt_set.getDisplacementCapacity() - self.bolt_set.getDi()))

        return y

    def checkCapacityCalculations(self) -> None:
        bs = self.bolt_set.getBoltSpacing()
        rs = self.bolt_set.getRingSpacing()

        if self.bolt_set.getBolt() is not None:
            if bs is not None and rs is not None:
                self.calculateEnergyCapacity()

    def checkSpacingCalculations(self) -> None:
        bs = self.bolt_set.getBoltSpacing()
        rs = self.bolt_set.getRingSpacing()

        if bs is not None and rs is not None:
            self.calculateNormalizedSpacing()
            self.calculateBoltsPerArea()
