from typing import Optional, TYPE_CHECKING, Literal


if TYPE_CHECKING:
    from geoassistant.ground_support.displacement_based.site_elements.Site import Site
    from geoassistant.ground_support.displacement_based.site_elements.Excavation import Excavation


class UnstableMass(object):

    def __init__(self, site: 'Site'):
        self.site: 'Site' = site

        self.excavation: 'Excavation' = self.site.getExcavation()

        self.n: Optional[Literal[2, 3, 6]] = self.site.getRockMass().getN()
        self.density: float = self.site.getRockMass().getDensity()

        self.elongated: float = self.calculateElongatedUnstableMass()
        self.intersection: float = self.calculateIntersectionUnstableMass()
        self.central: float = self.calculateCentralUnstableMass()
        self.central_intersection: float = self.calculateCentralIntersectionUnstableMass()

    def getElongatedUnstableMass(self) -> float:
        return self.elongated

    def getIntersectionUnstableMass(self) -> float:
        return self.intersection

    def getCentralUnstableMass(self) -> float:
        return self.central

    def getCentralIntersectionUnstableMass(self) -> float:
        return self.central_intersection

    def calculateElongatedUnstableMass(self) -> float:
        span = self.excavation.getWidth()
        unstable_mass = (2. / 3.) * (span / self.n) * (self.density / 1000)
        return unstable_mass

    def calculateIntersectionUnstableMass(self) -> float:
        span = self.excavation.getWidestIntersectionSpan()
        unstable_mass = (1. / 2.) * (span / self.n) * (self.density / 1000)
        return unstable_mass

    def calculateCentralUnstableMass(self) -> float:
        span = self.excavation.getWidth()
        unstable_mass = (span / self.n) * (self.density / 1000)
        return unstable_mass

    def calculateCentralIntersectionUnstableMass(self) -> float:
        span = self.excavation.getWidestIntersectionSpan()
        unstable_mass = (span / self.n) * (self.density / 1000)
        return unstable_mass
