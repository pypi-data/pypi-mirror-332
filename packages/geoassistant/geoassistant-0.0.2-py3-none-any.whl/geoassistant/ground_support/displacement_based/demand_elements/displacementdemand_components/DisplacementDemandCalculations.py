from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from geoassistant.ground_support.displacement_based.demand_elements.DisplacementDemand import DisplacementDemand


class DisplacementDemandCalculations(object):

    def __init__(self, displacement_demand: 'DisplacementDemand'):
        self.displacement_demand: 'DisplacementDemand' = displacement_demand

        self.pre_sb_displacement: Optional[float] = None
        self.dynamic_displacement: Optional[float] = None

        self.delta_df: Optional[float] = None  # Known as "Additional Depth of Fracturing"
        self.df_displacement: Optional[float] = None

        self.total_displacement_demand: Optional[float] = None

    def getDynamicDisplacement(self) -> Optional[float]:
        return self.dynamic_displacement

    def getAdditionalDepthOfFracture(self) -> Optional[float]:
        return self.delta_df

    def getDfDisplacement(self) -> Optional[float]:
        return self.df_displacement

    def getTotalDisplacementDemand(self) -> Optional[float]:
        return self.total_displacement_demand

    def calculateDemands(self) -> None:
        self.calculateStaticDisplacement()
        self.calculatePreStrainburstDisplacement()

        self.calculateDynamicDisplacement()
        self.calculateAdditionalDepthOfFracture()
        self.calculateDfDisplacement()

        self.calculateTotalDisplacementDemand()

    def calculateStaticDisplacement(self) -> None:
        pass

    def calculatePreStrainburstDisplacement(self) -> None:
        ds = self.displacement_demand.getDemandSystem()
        self.pre_sb_displacement = ds.getPreviousDisplacement().getD0()  # + self.static_displacement

    def calculateDynamicDisplacement(self) -> None:
        ds = self.displacement_demand.getDemandSystem()

        strainburst = ds.getStrainburst()
        bulking_factors = ds.getBulkingFactors()

        self.dynamic_displacement = strainburst.getStrainburstDepth() * bulking_factors.getDynamicBulkingFactor() * 1000

    def calculateAdditionalDepthOfFracture(self) -> None:
        ds = self.displacement_demand.getDemandSystem()

        site = ds.getSite()
        seismic_response = ds.getSeismicResponse()

        Ra = site.getExcavation().getEquivalentRadius()
        pd_model = site.getRockMass().getPerrasDiederichsModel()

        stress_level = site.getStressState().getStressLevel()

        if stress_level > 0.43:
            sum_SL = (stress_level + seismic_response.getStressLevelChange())

            A = Ra * pd_model['a'] * ((sum_SL / pd_model['Ci']) - 1) ** pd_model['b']
            B = Ra * pd_model['a'] * ((stress_level / pd_model['Ci']) - 1) ** pd_model['b']

            self.delta_df = A - B
        else:
            self.delta_df = 0.

    def calculateDfDisplacement(self) -> None:
        ds = self.displacement_demand.getDemandSystem()
        bulking_factors = ds.getBulkingFactors()

        self.df_displacement = self.delta_df * bulking_factors.getDynamicBulkingFactor() * 1000

    def calculateTotalDisplacementDemand(self) -> None:
        self.total_displacement_demand = self.pre_sb_displacement + self.dynamic_displacement + self.df_displacement
