from typing import TYPE_CHECKING

from geoassistant.ground_support.displacement_based.demand_elements.displacementdemand_components.DisplacementDemandProperties import DisplacementDemandProperties
from geoassistant.ground_support.displacement_based.demand_elements.displacementdemand_components.DisplacementDemandCalculations import DisplacementDemandCalculations

if TYPE_CHECKING:
    from geoassistant.ground_support.displacement_based.demand_elements.DemandSystem import DemandSystem


class DisplacementDemand(DisplacementDemandProperties):

    def __init__(self, demand_system: 'DemandSystem'):
        super().__init__(demand_system=demand_system)

        self.calculations: DisplacementDemandCalculations = DisplacementDemandCalculations(self)

    def calculateDemands(self) -> None:
        self.calculations.calculateDemands()