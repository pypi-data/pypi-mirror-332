from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from geoassistant.ground_support.displacement_based.demand_elements.DemandSystem import DemandSystem


class ShakedownDemand(object):

    def __init__(self, demand_system: 'DemandSystem'):
        self.demand_system: 'DemandSystem' = demand_system

        self.elongated: Optional[float] = None
        self.intersection: Optional[float] = None
        self.central: Optional[float] = None
        self.central_intersection: Optional[float] = None

    def getElongatedShakedownDemand(self) -> float:
        return self.elongated

    def getIntersectionShakedownDemand(self) -> float:
        return self.intersection

    def getCentralShakedownDemand(self) -> float:
        return self.central

    def getCentralIntersectionShakedownDemand(self) -> float:
        return self.central_intersection

    def calculateDemands(self):
        unstable_mass = self.demand_system.getUnstableMass()
        seismic_response = self.demand_system.getSeismicResponse()

        g = 9.81  # [m/s2]
        PGA = seismic_response.getPeakGroundAcceleration()

        self.elongated = unstable_mass.getElongatedUnstableMass() * (g + PGA)
        self.intersection = unstable_mass.getIntersectionUnstableMass() * (g + PGA)
        self.central = unstable_mass.getCentralUnstableMass() * (g + PGA)
        self.central_intersection = unstable_mass.getCentralIntersectionUnstableMass() * (g + PGA)
