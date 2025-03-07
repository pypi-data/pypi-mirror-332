from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from geoassistant.ground_support.displacement_based.demand_elements.DemandSystem import DemandSystem


class StaticDemand(object):

    def __init__(self, demand_system: 'DemandSystem'):
        self.demand_system: 'DemandSystem' = demand_system

        self.elongated: Optional[float] = None
        self.intersection: Optional[float] = None
        self.central: Optional[float] = None
        self.central_intersection: Optional[float] = None

    def getElongatedStaticDemand(self) -> float:
        return self.elongated

    def getIntersectionStaticDemand(self) -> float:
        return self.intersection

    def getCentralStaticDemand(self) -> float:
        return self.central

    def getCentralIntersectionStaticDemand(self) -> float:
        return self.central_intersection

    def calculateDemands(self):
        unstable_mass = self.demand_system.getUnstableMass()

        g = 9.81  # [m/s2]

        self.elongated = unstable_mass.getElongatedUnstableMass() * g
        self.intersection = unstable_mass.getIntersectionUnstableMass() * g
        self.central = unstable_mass.getCentralUnstableMass() * g
        self.central_intersection = unstable_mass.getCentralIntersectionUnstableMass() * g
