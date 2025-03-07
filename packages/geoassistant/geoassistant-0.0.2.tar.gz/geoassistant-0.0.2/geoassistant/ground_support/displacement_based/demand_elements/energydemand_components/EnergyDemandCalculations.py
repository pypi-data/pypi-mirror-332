from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from geoassistant.ground_support.displacement_based.demand_elements.EnergyDemand import EnergyDemand


class EnergyDemandCalculations(object):

    def __init__(self, energy_demand: 'EnergyDemand'):
        self.energy_demand: 'EnergyDemand' = energy_demand

        self.bulking_velocity: Optional[float] = None  # also known as vi or strainburst velocity [m/s]

        self.sb_kinetic_energy: Optional[float] = None
        self.sb_remote_energy: Optional[float] = None

        self.idmg_kinetic_energy: Optional[float] = None
        self.idmg_remote_energy: Optional[float] = None

        self.total_energy_demand: Optional[float] = None

    def getBulkingVelocity(self) -> Optional[float]:
        return self.bulking_velocity

    def getStrainburstKineticEnergy(self) -> Optional[float]:
        return self.sb_kinetic_energy

    def getStrainburstRemoteEnergy(self) -> Optional[float]:
        return self.sb_remote_energy

    def getTotalEnergyDemand(self) -> Optional[float]:
        return self.total_energy_demand

    def calculateDemands(self) -> None:
        self.calculateBulkingVelocity()

        self.calculateStrainburstEnergyDemand()
        self.calculateInitialDamageEnergyDemand()

        self.calculateTotalEnergyDemand()

    def calculateBulkingVelocity(self) -> None:
        ds = self.energy_demand.getDemandSystem()

        tr = ds.getStrainburst().getRuptureTime()

        self.bulking_velocity = ds.getDynamicDisplacement() / tr

    def calculateStrainburstEnergyDemand(self) -> None:
        ds = self.energy_demand.getDemandSystem()

        straiburst = ds.getStrainburst()
        seismic_response = ds.getSeismicResponse()
        rock_mass = ds.getSite().getRockMass()

        n = 1

        self.sb_kinetic_energy = (0.5 * straiburst.getStrainburstDepth() * rock_mass.getDensity() * (self.bulking_velocity / 2) ** 2) / 1000.
        self.sb_remote_energy = (0.5 * straiburst.getStrainburstDepth() * rock_mass.getDensity() * (n * seismic_response.getPeakGroundVelocity()) ** 2) / 1000

    def calculateInitialDamageEnergyDemand(self) -> None:
        pass

    def calculateTotalEnergyDemand(self) -> None:
        kinetic_energy = self.sb_kinetic_energy  # + self.idmg_kinetic_energy
        remote_energy = self.sb_remote_energy  # self.idmg_remote_energy

        self.total_energy_demand = kinetic_energy + remote_energy

