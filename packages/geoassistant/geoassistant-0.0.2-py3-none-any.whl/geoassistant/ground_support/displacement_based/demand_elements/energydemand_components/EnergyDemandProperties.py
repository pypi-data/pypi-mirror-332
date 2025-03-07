from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from geoassistant.ground_support.displacement_based.demand_elements.DemandSystem import DemandSystem
    from geoassistant.ground_support.displacement_based.demand_elements.energydemand_components.EnergyDemandCalculations import EnergyDemandCalculations


class EnergyDemandProperties(object):

    def __init__(self, demand_system: 'DemandSystem'):
        self.demand_system: 'DemandSystem' = demand_system

        self.calculations: Optional['EnergyDemandCalculations'] = None

    def getDemandSystem(self) -> 'DemandSystem':
        return self.demand_system

    def getBulkingVelocity(self) -> Optional[float]:
        return self.calculations.getBulkingVelocity()

    def getStrainburstKineticEnergy(self) -> Optional[float]:
        return self.calculations.getStrainburstKineticEnergy()

    def getStrainburstRemoteEnergy(self) -> Optional[float]:
        return self.calculations.getStrainburstRemoteEnergy()

    def getTotalEnergyDemand(self) -> Optional[float]:
        return self.calculations.getTotalEnergyDemand()
