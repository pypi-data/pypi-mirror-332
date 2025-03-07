from typing import TYPE_CHECKING

from geoassistant.ground_support.displacement_based.reliability_analysis.safetyfactors_components.SafetyFactorsProperties import SafetyFactorsProperties
from geoassistant.ground_support.displacement_based.reliability_analysis.safetyfactors_components.SafetyFactorsCalculations import SafetyFactorsCalculations

if TYPE_CHECKING:
    from geoassistant.ground_support.displacement_based.support_elements.SupportSystem import SupportSystem
    from geoassistant.ground_support.displacement_based.demand_elements.DemandSystem import DemandSystem


class SafetyFactors(SafetyFactorsProperties):

    def __init__(self, support_system: 'SupportSystem', demand_system: 'DemandSystem'):
        super().__init__(support_system=support_system, demand_system=demand_system)

        self.calculations: SafetyFactorsCalculations = SafetyFactorsCalculations(self)
