from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from geoassistant.ground_support.displacement_based.site_elements.excavation_components.ExcavationCalculations import ExcavationCalculations


class ExcavationProperties(object):

    def __init__(self):

        self.width: Optional[float] = None  # [m]
        self.height: Optional[float] = None  # [m]

        self.widest_intersection_span: Optional[float] = None  # [m]

        self.initial_damage_depth: Optional[float] = None  # [mm]

        self.calculations: Optional['ExcavationCalculations'] = None

    def setWidth(self, width: float) -> None:
        self.width = width
        self.calculations.checkEquivalentRadiusCalculation()

    def setHeight(self, height: float) -> None:
        self.height = height
        self.calculations.checkEquivalentRadiusCalculation()

    def setWidestIntersectionSpan(self, widest_intersection_span: float) -> None:
        self.widest_intersection_span = widest_intersection_span

    def setInitialDamageDepth(self, initial_damage_depth: float) -> None:
        self.initial_damage_depth = initial_damage_depth

    def getWidth(self) -> Optional[float]:
        return self.width

    def getHeight(self) -> Optional[float]:
        return self.height

    def getWidestIntersectionSpan(self) -> Optional[float]:
        return self.widest_intersection_span

    def getEquivalentRadius(self) -> Optional[float]:
        return self.calculations.getEquivalentRadius()

    def getInitialDamageDepth(self) -> Optional[float]:
        return self.initial_damage_depth
