from typing import TYPE_CHECKING, Optional, List

import numpy as np


from geoassistant.seismic.SeismicEvent import SeismicEvent
from geoassistant.ground_support.displacement_based.demand_elements.SeismicResponse import SeismicResponse
from geoassistant.ground_support.displacement_based.demand_elements.Strainburst import Strainburst
from geoassistant.ground_support.displacement_based.demand_elements.PreviousDisplacement import PreviousDisplacement
from geoassistant.ground_support.displacement_based.demand_elements.BulkingFactors import BulkingFactors
from geoassistant.ground_support.displacement_based.demand_elements.DemandSystem import DemandSystem

from geoassistant.ground_support.displacement_based.reliability_analysis.SafetyFactors import SafetyFactors

if TYPE_CHECKING:
    from geoassistant.ground_support.displacement_based.support_elements.SupportSystem import SupportSystem
    from geoassistant.ground_support.displacement_based.site_elements.Site import Site


class MontecarloSimulation(object):

    def __init__(self, support_system: 'SupportSystem', site: 'Site'):
        self.support_system: 'SupportSystem' = support_system
        self.site: 'Site' = site

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

        self.initiated_strainburst_displacement_pof: Optional[float] = None
        self.initiated_strainburst_energy_pof: Optional[float] = None
        self.loaded_strainburst_displacement_pof: Optional[float] = None
        self.loaded_strainburst_energy_pof: Optional[float] = None

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

    def getSelfInitiatedStrainburstDisplacementProbabilityOfFailure(self):
        return self.initiated_strainburst_displacement_pof

    def getSelfInitiatedStrainburstEnergyProbabilityOfFailure(self):
        return self.initiated_strainburst_energy_pof

    def getDynamicallyLoadedStrainburstDisplacementProbabilityOfFailure(self):
        return self.loaded_strainburst_displacement_pof

    def getDynamicallyLoadedStrainburstEnergyProbabilityOfFailure(self):
        return self.loaded_strainburst_energy_pof

    def test(self) -> List['SafetyFactors']:

        n_samples = 3000

        mu, sigma = 0.82, 0.1  # Mean and standard deviation
        PGVs = np.random.normal(mu, sigma, n_samples)

        left, mode, right = 0.2, 0.4, 1.0
        dSBs = np.random.triangular(left, mode, right, n_samples)

        left, mode, right = 20.0, 25.3, 33.0
        tRs = np.random.triangular(left, mode, right, n_samples)

        left, mode, right = 0.0, 15.0, 40.0
        d0s = np.random.triangular(left, mode, right, n_samples)

        se = SeismicEvent()
        se.setFrequency(value=7, units="Hz")

        bf = BulkingFactors()
        bf.setStaticBulkingFactor(static_bulking_factor=0.02)
        bf.setDynamicBulkingFactor(dynamic_bulking_factor=0.059)

        safety_factors_instances = []

        for PGV, dSB, tR, d0 in zip(PGVs, dSBs, tRs, d0s):
            sr = SeismicResponse()
            sr.setSite(self.site)
            sr.setSeismicEvent(seismic_event=se)
            sr.setPeakGroundVelocity(peak_ground_velocity=PGV)

            sb = Strainburst()
            sb.setStrainburstDepth(strainburst_depth=dSB)
            sb.setRuptureTime(rupture_time=tR)

            pd = PreviousDisplacement()
            pd.setD0(d0=d0)

            ds = DemandSystem()
            ds.setSite(site=self.site)
            ds.setSeismicResponse(seismic_response=sr)
            ds.setStrainburst(strainburst=sb)
            ds.setPreviousDisplacement(previous_displacement=pd)
            ds.setBulkingFactors(bulking_factors=bf)

            sfs = SafetyFactors(support_system=self.support_system, demand_system=ds)

            safety_factors_instances += [sfs]

        return safety_factors_instances

    def calculateMontecarloResults(self) -> None:
        safety_factors_instances = self.test()

        self.elongated_shakedown_initiation_fs = np.average([sfs.getElongatedShakedownInitiationSafetyFactor() for sfs in safety_factors_instances])
        self.intersection_shakedown_initiation_fs = np.average([sfs.getIntersectionShakedownInitiationSafetyFactor() for sfs in safety_factors_instances])
        self.central_shakedown_initiation_fs = np.average([sfs.getCentralShakedownInitiationSafetyFactor() for sfs in safety_factors_instances])
        self.central_intersection_shakedown_initiation_fs = np.average([sfs.getCentralIntersectionShakedownInitiationSafetyFactor() for sfs in safety_factors_instances])

        self.elongated_shakedown_survival_fs = np.average([sfs.getElongatedShakedownSurvivalSafetyFactor() for sfs in safety_factors_instances])
        self.intersection_shakedown_survival_fs = np.average([sfs.getIntersectionShakedownSurvivalSafetyFactor() for sfs in safety_factors_instances])
        self.central_shakedown_survival_fs = np.average([sfs.getCentralShakedownSurvivalSafetyFactor() for sfs in safety_factors_instances])
        self.central_intersection_shakedown_survival_fs = np.average([sfs.getCentralIntersectionShakedownSurvivalSafetyFactor() for sfs in safety_factors_instances])

        self.initiated_strainburst_displacement_fs = np.average([sfs.getSelfInitiatedStrainburstDisplacementSafetyFactor() for sfs in safety_factors_instances])
        self.initiated_strainburst_energy_fs = np.average([sfs.getSelfInitiatedStrainburstEnergySafetyFactor() for sfs in safety_factors_instances])
        self.loaded_strainburst_displacement_fs = np.average([sfs.getDynamicallyLoadedStrainburstDisplacementSafetyFactor() for sfs in safety_factors_instances])
        self.loaded_strainburst_energy_fs = np.average([sfs.getDynamicallyLoadedStrainburstEnergySafetyFactor() for sfs in safety_factors_instances])

        fs_list = [sfs.getSelfInitiatedStrainburstDisplacementSafetyFactor() for sfs in safety_factors_instances]
        self.initiated_strainburst_displacement_pof = sum(1 for fs in fs_list if fs <= 1) / len(fs_list)

        fs_list = [sfs.getSelfInitiatedStrainburstEnergySafetyFactor() for sfs in safety_factors_instances]
        self.initiated_strainburst_energy_pof = sum(1 for fs in fs_list if fs <= 1) / len(fs_list)

        fs_list = [sfs.getDynamicallyLoadedStrainburstDisplacementSafetyFactor() for sfs in safety_factors_instances]
        self.loaded_strainburst_displacement_pof = sum(1 for fs in fs_list if fs <= 1) / len(fs_list)

        fs_list = [sfs.getDynamicallyLoadedStrainburstEnergySafetyFactor() for sfs in safety_factors_instances]
        self.loaded_strainburst_energy_pof = sum(1 for fs in fs_list if fs <= 1) / len(fs_list)
