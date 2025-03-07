from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from geoassistant.ground_support.displacement_based.support_elements.Bolt import Bolt


class BoltCalculations(object):

    def __init__(self, bolt: 'Bolt'):
        self.bolt: 'Bolt' = bolt

        self.displacement_capacity: Optional[float] = None

    def getDisplacementCapacity(self) ->  Optional[float]:
        return self.displacement_capacity

    def calculateDisplacementCapacity(self) -> None:
        dsf = self.bolt.getDisplacementSplitFactor()

        self.displacement_capacity = dsf * self.bolt.getDu_ID() + (1 - dsf) * self.bolt.getDu_D()
        self.displacement_capacity += self.bolt.getDi()

    def checkCapacityCalculations(self) -> None:
        needed_parameters = [
            self.bolt.getDisplacementSplitFactor(),
            self.bolt.getDu_D(),
            self.bolt.getDu_ID(),
            self.bolt.getDi()
        ]

        if None not in needed_parameters:
            self.calculateDisplacementCapacity()
