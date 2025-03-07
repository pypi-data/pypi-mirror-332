from typing import Optional, TYPE_CHECKING, Tuple, List

from geoassistant.ground_support.displacement_based.support_elements.SupportElement import SupportElement

from geoassistant.ground_support.displacement_based.support_elements.boltset_components.BoltSetProperties import BoltSetProperties
from geoassistant.ground_support.displacement_based.support_elements.boltset_components.BoltSetCalculations import BoltSetCalculations
from geoassistant.ground_support.displacement_based.support_elements.boltset_components.BoltSetPlotter import BoltSetPlotter


if TYPE_CHECKING:
    pass


class BoltSet(SupportElement, BoltSetProperties):

    def __init__(self, name: Optional[str]):
        super().__init__(name=name)

        self.calculations: BoltSetCalculations = BoltSetCalculations(self)
        self.plotter: BoltSetPlotter = BoltSetPlotter(self)

    def getUsedEnergyCapacityCurve(self) -> Tuple[List[float], List[float]]:
        xs = [0, self.getBolt().getDi(), self.getBolt().getDisplacementCapacity()]
        ys = [0, 0, self.getEnergyCapacity()]
        return xs, ys

    def calculateUsedEnergyAtDisplacement(self, displacement: float) -> Optional[float]:
        return self.calculations.calculateUsedEnergyAtDisplacement(displacement=displacement)

    def plotCapacityCurve(self) -> None:
        self.plotter.plotCapacityCurve()
