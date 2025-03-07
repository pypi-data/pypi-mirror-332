from geoassistant.ground_support.displacement_based.site_elements.excavation_components.ExcavationProperties import ExcavationProperties
from geoassistant.ground_support.displacement_based.site_elements.excavation_components.ExcavationCalculations import ExcavationCalculations


class Excavation(ExcavationProperties):

    def __init__(self):
        super().__init__()

        self.calculations: ExcavationCalculations = ExcavationCalculations(self)