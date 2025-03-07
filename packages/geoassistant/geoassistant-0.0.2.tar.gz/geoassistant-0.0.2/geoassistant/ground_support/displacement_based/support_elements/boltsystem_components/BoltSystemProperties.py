from typing import List, TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from geoassistant.ground_support.displacement_based.support_elements.BoltSet import BoltSet
    from geoassistant.ground_support.displacement_based.support_elements.boltsystem_components.BoltSystemCalculations import BoltSystemCalculations


class BoltSystemProperties(object):

    def __init__(self):

        self.bolt_sets: List['BoltSet'] = []

        self.calculations: Optional['BoltSystemCalculations'] = None

    def addBoltSet(self, bolt_set: 'BoltSet') -> None:
        self.bolt_sets += [bolt_set]
        self.calculations.updateCalculations()

    def getDi(self) -> Optional[float]:
        return self.calculations.getDi()

    def getDisplacementCapacity(self) -> Optional[float]:
        return self.calculations.getDisplacementCapacity()

    def getEnergyCapacity(self) -> Optional[float]:
        return self.calculations.getEnergyCapacity()

    def getEquivalentSpacing(self) -> Optional[float]:
        return self.calculations.getEquivalentSpacing()
