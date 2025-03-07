import math
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from geoassistant.ground_support.displacement_based.site_elements.Excavation import Excavation


class ExcavationCalculations(object):

    def __init__(self, excavation: 'Excavation'):
        self.excavation: 'Excavation' = excavation

        self.equivalent_radius: Optional[float] = None

    def getEquivalentRadius(self) -> Optional[float]:
        return self.equivalent_radius

    def calculateEquivalentRadius(self) -> None:
        A = self.excavation.getHeight() / 2
        B = self.excavation.getWidth() / 2

        self.equivalent_radius = math.sqrt(A ** 2 + B ** 2)

    def checkEquivalentRadiusCalculation(self):
        if self.excavation.getWidth() is not None and self.excavation.getHeight() is not None:
            self.calculateEquivalentRadius()
