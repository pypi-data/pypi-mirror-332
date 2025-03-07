from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from geoassistant.ground_support.displacement_based.reliability_analysis.SafetyFactors import SafetyFactors


class SafetyFactorsCalculations(object):

    def __init__(self, safety_factors: 'SafetyFactors'):
        self.safety_factors: 'SafetyFactors' = safety_factors

        # STATIC ASSESSMENT
        self.elongated_static_fs: Optional[float] = None
        self.intersection_static_fs: Optional[float] = None
        self.central_static_fs: Optional[float] = None
        self.central_intersection_static_fs: Optional[float] = None

        # SHAKEDOWN ASSESSMENT
        self.elongated_shakedown_initiation_fs: Optional[float] = None
        self.intersection_shakedown_initiation_fs: Optional[float] = None
        self.central_shakedown_initiation_fs: Optional[float] = None
        self.central_intersection_shakedown_initiation_fs: Optional[float] = None

        self.elongated_shakedown_survival_fs: Optional[float] = None
        self.intersection_shakedown_survival_fs: Optional[float] = None
        self.central_shakedown_survival_fs: Optional[float] = None
        self.central_intersection_shakedown_survival_fs: Optional[float] = None

        # STRAINBURST ASSESSMENT
        self.initiated_strainburst_displacement_fs: Optional[float] = None
        self.initiated_strainburst_energy_fs: Optional[float] = None
        self.loaded_strainburst_displacement_fs: Optional[float] = None
        self.loaded_strainburst_energy_fs: Optional[float] = None

        # CALCULATIONS
        self.calculateStaticSafetyFactors()
        self.calculateShakedownInitiationSafetyFactors()
        self.calculateShakedownSurvivalSafetyFactors()
        self.calculateSelfInitiatedStrainburstSafetyFactors()
        self.calculateDynamicallyLoadedStrainburstSafetyFactors()

    def getElongatedStaticSafetyFactor(self) -> float:
        return self.elongated_static_fs

    def getIntersectionStaticSafetyFactor(self) -> float:
        return self.intersection_static_fs

    def getCentralStaticSafetyFactor(self) -> float:
        return self.central_static_fs

    def getCentralIntersectionStaticSafetyFactor(self) -> float:
        return self.central_intersection_static_fs

    def getElongatedShakedownInitiationSafetyFactor(self) -> float:
        return self.elongated_shakedown_initiation_fs

    def getIntersectionShakedownInitiationSafetyFactor(self) -> float:
        return self.intersection_shakedown_initiation_fs

    def getCentralShakedownInitiationSafetyFactor(self) -> float:
        return self.central_shakedown_initiation_fs

    def getCentralIntersectionShakedownInitiationSafetyFactor(self) -> float:
        return self.central_intersection_shakedown_initiation_fs

    def getElongatedShakedownSurvivalSafetyFactor(self) -> float:
        return self.elongated_shakedown_survival_fs

    def getIntersectionShakedownSurvivalSafetyFactor(self) -> float:
        return self.intersection_shakedown_survival_fs

    def getCentralShakedownSurvivalSafetyFactor(self) -> float:
        return self.central_shakedown_survival_fs

    def getCentralIntersectionShakedownSurvivalSafetyFactor(self) -> float:
        return self.central_intersection_shakedown_survival_fs

    def getSelfInitiatedStrainburstDisplacementSafetyFactor(self):
        return self.initiated_strainburst_displacement_fs

    def getSelfInitiatedStrainburstEnergySafetyFactor(self):
        return self.initiated_strainburst_energy_fs

    def getDynamicallyLoadedStrainburstDisplacementSafetyFactor(self):
        return self.loaded_strainburst_displacement_fs

    def getDynamicallyLoadedStrainburstEnergySafetyFactor(self):
        return self.loaded_strainburst_energy_fs

    def calculateStaticSafetyFactors(self):
        ssys = self.safety_factors.getSupportSystem()
        dsys = self.safety_factors.getDemandSystem()

        self.elongated_static_fs = ssys.getStaticCapacity() / dsys.getElongatedStaticDemand()
        self.intersection_static_fs = ssys.getStaticCapacity() / dsys.getIntersectionStaticDemand()
        self.central_static_fs = ssys.getStaticCapacity() / dsys.getCentralStaticDemand()
        self.central_intersection_static_fs = ssys.getStaticCapacity() / dsys.getCentralIntersectionStaticDemand()

    def calculateShakedownInitiationSafetyFactors(self):
        ssys = self.safety_factors.getSupportSystem()
        dsys = self.safety_factors.getDemandSystem()

        self.elongated_shakedown_initiation_fs = ssys.getStaticCapacity() / dsys.getElongatedShakedownDemand()
        self.intersection_shakedown_initiation_fs = ssys.getStaticCapacity() / dsys.getIntersectionShakedownDemand()
        self.central_shakedown_initiation_fs = ssys.getStaticCapacity() / dsys.getCentralShakedownDemand()
        self.central_intersection_shakedown_initiation_fs = ssys.getStaticCapacity() / dsys.getCentralIntersectionShakedownDemand()

    def calculateShakedownSurvivalSafetyFactors(self):
        dsys = self.safety_factors.getDemandSystem()
        ssys = self.safety_factors.getSupportSystem()

        g = 9.81  # [m/s2]
        n_amplification = 1.
        md = 1.1

        PGV = dsys.getSeismicResponse().getPeakGroundVelocity()

        elongated_dss_ult = 1000 * ((n_amplification * PGV) ** 2) / (2 * g * (md * self.elongated_static_fs - 1))  # [mm]
        intersection_dss_ult = 1000 * ((n_amplification * PGV) ** 2) / (2 * g * (md * self.intersection_static_fs - 1))  # [mm]
        central_dss_ult = 1000 * ((n_amplification * PGV) ** 2) / (2 * g * (md * self.central_static_fs - 1))  # [mm]
        central_intersection_dss_ult = 1000 * ((n_amplification * PGV) ** 2) / (2 * g * (md * self.central_intersection_static_fs - 1))  # [mm]

        displacement_capacity = ssys.getBoltSystem().getDisplacementCapacity()
        d0 = dsys.getPreviousDisplacement().getD0()

        self.elongated_shakedown_survival_fs = (displacement_capacity - d0) / elongated_dss_ult
        self.intersection_shakedown_survival_fs = (displacement_capacity - d0) / intersection_dss_ult
        self.central_shakedown_survival_fs = (displacement_capacity - d0) / central_dss_ult
        self.central_intersection_shakedown_survival_fs = (displacement_capacity - d0) / central_intersection_dss_ult

    def calculateSelfInitiatedStrainburstSafetyFactors(self):
        dsys = self.safety_factors.getDemandSystem()
        ssys = self.safety_factors.getSupportSystem()

        # DISPLACEMENT
        d0 = dsys.getPreviousDisplacement().getD0()
        displacement_demand = dsys.getDynamicDisplacement() + d0  # Just considering dSB

        energy_demand = dsys.getStrainburstKineticEnergy()  # Just considering dSB energy
        du = ssys.calculateDisplacementAtRemnantEnergy(remnant_energy=energy_demand)

        self.initiated_strainburst_displacement_fs = (du - d0) / (displacement_demand - d0)

        # ENERGY
        dE = ssys.calculateRemnantEnergyAtDisplacement(displacement=displacement_demand)
        self.initiated_strainburst_energy_fs = dE / energy_demand

    def calculateDynamicallyLoadedStrainburstSafetyFactors(self):
        dsys = self.safety_factors.getDemandSystem()
        ssys = self.safety_factors.getSupportSystem()

        # DISPLACEMENT
        d0 = dsys.getPreviousDisplacement().getD0()
        displacement_demand = dsys.getTotalDisplacementDemand()
        energy_demand = dsys.getTotalEnergyDemand()

        du = ssys.calculateDisplacementAtRemnantEnergy(remnant_energy=energy_demand)

        self.loaded_strainburst_displacement_fs = (du - d0) / (displacement_demand - d0)

        # ENERGY
        dE = ssys.calculateRemnantEnergyAtDisplacement(displacement=displacement_demand)
        self.loaded_strainburst_energy_fs = dE / energy_demand

