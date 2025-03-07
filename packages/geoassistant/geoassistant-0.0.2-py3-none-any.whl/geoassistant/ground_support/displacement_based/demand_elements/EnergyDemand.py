from typing import TYPE_CHECKING

from geoassistant.ground_support.displacement_based.demand_elements.energydemand_components.EnergyDemandProperties import EnergyDemandProperties
from geoassistant.ground_support.displacement_based.demand_elements.energydemand_components.EnergyDemandCalculations import EnergyDemandCalculations

if TYPE_CHECKING:
    from geoassistant.ground_support.displacement_based.demand_elements.DemandSystem import DemandSystem


class EnergyDemand(EnergyDemandProperties):

    def __init__(self, demand_system: 'DemandSystem'):
        super().__init__(demand_system=demand_system)

        self.calculations: EnergyDemandCalculations = EnergyDemandCalculations(self)

    def calculateDemands(self) -> None:
        self.calculations.calculateDemands()