from typing import Optional

from geoassistant.ground_support.displacement_based.demand_elements.StaticDemand import StaticDemand
from geoassistant.ground_support.displacement_based.demand_elements.ShakedownDemand import ShakedownDemand
from geoassistant.ground_support.displacement_based.demand_elements.demandsystem_components.DemandSystemProperties import DemandSystemProperties
from geoassistant.ground_support.displacement_based.demand_elements.DisplacementDemand import DisplacementDemand
from geoassistant.ground_support.displacement_based.demand_elements.EnergyDemand import EnergyDemand

from geoassistant.ground_support.displacement_based.demand_elements.demandsystem_components.DemandSystemCalculations import DemandSystemCalculations


class DemandSystem(DemandSystemProperties):

    def __init__(self):
        super().__init__()

        self.static_demand: StaticDemand = StaticDemand(self)
        self.shakedown_demand: ShakedownDemand = ShakedownDemand(self)

        self.displacement_demand: DisplacementDemand = DisplacementDemand(self)
        self.energy_demand: EnergyDemand = EnergyDemand(self)

        self.calculations: DemandSystemCalculations = DemandSystemCalculations(self)
