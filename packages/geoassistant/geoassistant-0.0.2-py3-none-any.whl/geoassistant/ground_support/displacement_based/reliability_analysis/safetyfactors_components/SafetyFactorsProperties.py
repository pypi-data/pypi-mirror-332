from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from geoassistant.ground_support.displacement_based.support_elements.SupportSystem import SupportSystem
    from geoassistant.ground_support.displacement_based.demand_elements.DemandSystem import DemandSystem

    from geoassistant.ground_support.displacement_based.reliability_analysis.safetyfactors_components.SafetyFactorsCalculations import SafetyFactorsCalculations


class SafetyFactorsProperties(object):

    def __init__(self, support_system: 'SupportSystem', demand_system: 'DemandSystem'):
        self.support_system: 'SupportSystem' = support_system
        self.demand_system: 'DemandSystem' = demand_system

        self.calculations: Optional['SafetyFactorsCalculations'] = None

    def getSupportSystem(self) -> Optional['SupportSystem']:
        return self.support_system

    def getDemandSystem(self) -> Optional['DemandSystem']:
        return self.demand_system

    def getElongatedStaticSafetyFactor(self) -> float:
        return self.calculations.getElongatedStaticSafetyFactor()

    def getIntersectionStaticSafetyFactor(self) -> float:
        return self.calculations.getIntersectionStaticSafetyFactor()

    def getCentralStaticSafetyFactor(self) -> float:
        return self.calculations.getCentralStaticSafetyFactor()

    def getCentralIntersectionStaticSafetyFactor(self) -> float:
        return self.calculations.getCentralIntersectionStaticSafetyFactor()

    def getElongatedShakedownInitiationSafetyFactor(self) -> float:
        return self.calculations.getElongatedShakedownInitiationSafetyFactor()

    def getIntersectionShakedownInitiationSafetyFactor(self) -> float:
        return self.calculations.getIntersectionShakedownInitiationSafetyFactor()

    def getCentralShakedownInitiationSafetyFactor(self) -> float:
        return self.calculations.getCentralShakedownInitiationSafetyFactor()

    def getCentralIntersectionShakedownInitiationSafetyFactor(self) -> float:
        return self.calculations.getCentralIntersectionShakedownInitiationSafetyFactor()

    def getElongatedShakedownSurvivalSafetyFactor(self) -> float:
        return self.calculations.getElongatedShakedownSurvivalSafetyFactor()

    def getIntersectionShakedownSurvivalSafetyFactor(self) -> float:
        return self.calculations.getIntersectionShakedownSurvivalSafetyFactor()

    def getCentralShakedownSurvivalSafetyFactor(self) -> float:
        return self.calculations.getCentralShakedownSurvivalSafetyFactor()

    def getCentralIntersectionShakedownSurvivalSafetyFactor(self) -> float:
        return self.calculations.getCentralIntersectionShakedownSurvivalSafetyFactor()

    def getSelfInitiatedStrainburstDisplacementSafetyFactor(self):
        return self.calculations.getSelfInitiatedStrainburstDisplacementSafetyFactor()

    def getSelfInitiatedStrainburstEnergySafetyFactor(self):
        return self.calculations.getSelfInitiatedStrainburstEnergySafetyFactor()

    def getDynamicallyLoadedStrainburstDisplacementSafetyFactor(self):
        return self.calculations.getDynamicallyLoadedStrainburstDisplacementSafetyFactor()

    def getDynamicallyLoadedStrainburstEnergySafetyFactor(self):
        return self.calculations.getDynamicallyLoadedStrainburstEnergySafetyFactor()
