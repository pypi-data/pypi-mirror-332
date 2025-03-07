from typing import TYPE_CHECKING, Optional

import numpy as np


if TYPE_CHECKING:
    from geoassistant.ground_support.displacement_based.site_elements.Site import Site
    from geoassistant.ground_support.displacement_based.demand_elements.SeismicResponse import SeismicResponse
    from geoassistant.ground_support.displacement_based.demand_elements.Strainburst import Strainburst
    from geoassistant.ground_support.displacement_based.demand_elements.PreviousDisplacement import PreviousDisplacement

    from geoassistant.ground_support.displacement_based.demand_elements.BulkingFactors import BulkingFactors

    from geoassistant.ground_support.displacement_based.demand_elements.UnstableMass import UnstableMass

    from geoassistant.ground_support.displacement_based.demand_elements.StaticDemand import StaticDemand
    from geoassistant.ground_support.displacement_based.demand_elements.ShakedownDemand import ShakedownDemand

    from geoassistant.ground_support.displacement_based.demand_elements.DisplacementDemand import DisplacementDemand
    from geoassistant.ground_support.displacement_based.demand_elements.EnergyDemand import EnergyDemand

    from geoassistant.ground_support.displacement_based.demand_elements.demandsystem_components.DemandSystemCalculations import DemandSystemCalculations


class DemandSystemProperties(object):

    def __init__(self):
        self.site: Optional['Site'] = None

        self.seismic_response: Optional['SeismicResponse'] = None
        self.strainburst: Optional['Strainburst'] = None
        self.previous_displacement: Optional['PreviousDisplacement'] = None

        self.bulking_factors: Optional['BulkingFactors'] = None

        self.unstable_mass: Optional['UnstableMass'] = None

        self.static_demand: Optional['StaticDemand'] = None
        self.shakedown_demand: Optional['ShakedownDemand'] = None

        self.displacement_demand: Optional['DisplacementDemand'] = None
        self.energy_demand: Optional['EnergyDemand'] = None

        self.calculations: Optional['DemandSystemCalculations'] = None

    def setSite(self, site: 'Site') -> None:
        self.site = site
        self.calculations.checkDemandsCalculations()

    def setSeismicResponse(self, seismic_response: 'SeismicResponse') -> None:
        self.seismic_response = seismic_response
        self.calculations.checkDemandsCalculations()

    def setStrainburst(self, strainburst: 'Strainburst') -> None:
        self.strainburst = strainburst
        self.calculations.checkDemandsCalculations()

    def setPreviousDisplacement(self, previous_displacement: 'PreviousDisplacement') -> None:
        self.previous_displacement = previous_displacement
        self.calculations.checkDemandsCalculations()

    def setBulkingFactors(self, bulking_factors: 'BulkingFactors') -> None:
        self.bulking_factors = bulking_factors
        self.calculations.checkDemandsCalculations()

    def getSite(self) -> Optional['Site']:
        return self.site

    def getSeismicResponse(self) -> Optional['SeismicResponse']:
        return self.seismic_response

    def getStrainburst(self) -> Optional['Strainburst']:
        return self.strainburst

    def getPreviousDisplacement(self) -> 'PreviousDisplacement':
        return self.previous_displacement

    def getBulkingFactors(self) -> Optional['BulkingFactors']:
        return self.bulking_factors

    def getUnstableMass(self) -> Optional['UnstableMass']:
        return self.unstable_mass

    def getStaticDemand(self) -> 'StaticDemand':
        return self.static_demand

    def getShakedownDemand(self) -> 'ShakedownDemand':
        return self.shakedown_demand

    def getDisplacementDemand(self) -> 'DisplacementDemand':
        return self.displacement_demand

    def getEnergyDemand(self) -> 'EnergyDemand':
        return self.energy_demand

    def getElongatedStaticDemand(self) -> float:
        return self.static_demand.getElongatedStaticDemand()

    def getIntersectionStaticDemand(self) -> float:
        return self.static_demand.getIntersectionStaticDemand()

    def getCentralStaticDemand(self) -> float:
        return self.static_demand.getCentralStaticDemand()

    def getCentralIntersectionStaticDemand(self) -> float:
        return self.static_demand.getCentralIntersectionStaticDemand()

    def getElongatedShakedownDemand(self) -> float:
        return self.shakedown_demand.getElongatedShakedownDemand()

    def getIntersectionShakedownDemand(self) -> float:
        return self.shakedown_demand.getIntersectionShakedownDemand()

    def getCentralShakedownDemand(self) -> float:
        return self.shakedown_demand.getCentralShakedownDemand()

    def getCentralIntersectionShakedownDemand(self) -> float:
        return self.shakedown_demand.getCentralIntersectionShakedownDemand()

    def getDynamicDisplacement(self) -> Optional[float]:
        return self.displacement_demand.getDynamicDisplacement()

    def getAdditionalDepthOfFracture(self) -> Optional[float]:
        return self.displacement_demand.getAdditionalDepthOfFracture()

    def getDfDisplacement(self) -> Optional[float]:
        return self.displacement_demand.getDfDisplacement()

    def getTotalDisplacementDemand(self) -> Optional[float]:
        return self.displacement_demand.getTotalDisplacementDemand()

    def getBulkingVelocity(self) -> Optional[float]:
        return self.energy_demand.getBulkingVelocity()

    def getStrainburstKineticEnergy(self) -> Optional[float]:
        return self.energy_demand.getStrainburstKineticEnergy()

    def getStrainburstRemoteEnergy(self) -> Optional[float]:
        return self.energy_demand.getStrainburstRemoteEnergy()

    def getTotalEnergyDemand(self) -> Optional[float]:
        return self.energy_demand.getTotalEnergyDemand()

    def getEnergyDemandCurve(self) -> Optional[np.ndarray]:
        return self.calculations.getEnergyDemandCurve()
