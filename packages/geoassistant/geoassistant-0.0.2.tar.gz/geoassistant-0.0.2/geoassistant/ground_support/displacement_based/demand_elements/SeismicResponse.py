import numpy as np

from geoassistant.ground_support.displacement_based.demand_elements.seismicresponse_components.SeismicResponseProperties import SeismicResponseProperties
from geoassistant.ground_support.displacement_based.demand_elements.seismicresponse_components.SeismicResponseCalculations import SeismicResponseCalculations


class SeismicResponse(SeismicResponseProperties):

    def __init__(self):
        super().__init__()

        self.calculations: SeismicResponseCalculations = SeismicResponseCalculations(self)


