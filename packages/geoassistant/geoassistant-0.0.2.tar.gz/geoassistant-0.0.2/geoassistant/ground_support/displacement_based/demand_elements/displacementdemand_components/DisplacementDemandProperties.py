from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from geoassistant.ground_support.displacement_based.demand_elements.DemandSystem import DemandSystem
    from geoassistant.ground_support.displacement_based.demand_elements.BulkingFactors import BulkingFactors
    from geoassistant.ground_support.displacement_based.demand_elements.displacementdemand_components.DisplacementDemandCalculations import DisplacementDemandCalculations


class DisplacementDemandProperties(object):

    def __init__(self, demand_system: 'DemandSystem'):
        self.demand_system: 'DemandSystem' = demand_system

        self.calculations: Optional['DisplacementDemandCalculations'] = None

    def getDemandSystem(self) -> 'DemandSystem':
        return self.demand_system

    def getDynamicDisplacement(self) -> Optional[float]:
        return self.calculations.getDynamicDisplacement()

    def getAdditionalDepthOfFracture(self) -> Optional[float]:
        return self.calculations.getAdditionalDepthOfFracture()

    def getDfDisplacement(self) -> Optional[float]:
        return self.calculations.getDfDisplacement()

    def getTotalDisplacementDemand(self) -> Optional[float]:
        return self.calculations.getTotalDisplacementDemand()
