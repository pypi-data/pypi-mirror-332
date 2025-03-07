from typing import Optional, TYPE_CHECKING

import numpy as np

from geoassistant.ground_support.displacement_based.demand_elements.UnstableMass import UnstableMass


if TYPE_CHECKING:
    from geoassistant.ground_support.displacement_based.demand_elements.DemandSystem import DemandSystem


class DemandSystemCalculations(object):

    def __init__(self, demand_system: 'DemandSystem'):
        self.demand_system: 'DemandSystem' = demand_system

        self.demand_curve: Optional[np.ndarray] = None

    def getEnergyDemandCurve(self) -> Optional[np.ndarray]:
        return self.demand_curve

    def calculateEnergyDemandAtDisplacement(self, x: float) -> Optional[float]:
        d0 = self.demand_system.getPreviousDisplacement().getD0()
        displacement_demand = self.demand_system.getTotalDisplacementDemand()

        n = 4

        if x < d0:
            return 0
        elif x >= displacement_demand:
            return None
        else:
            return self.demand_system.getTotalEnergyDemand() * ((x - d0) / (displacement_demand - d0)) ** n

    def calculateEnergyDemandCurve(self) -> None:
        d0 = self.demand_system.getPreviousDisplacement().getD0()
        displacement_demand = self.demand_system.getTotalDisplacementDemand()

        energy_demand = self.demand_system.getTotalEnergyDemand()

        xs = [0, d0]
        ys = [0, 0]

        diff_x = displacement_demand - d0

        if diff_x > 5:
            dx = diff_x / 20.

            _xs = [d0 + (dx * i) for i in range(1, 20)]
            _ys = [self.calculateEnergyDemandAtDisplacement(_x) for _x in _xs]

            xs += _xs
            ys += _ys

        xs += [displacement_demand]
        ys += [energy_demand]

        self.demand_curve = np.array([xs, ys])

    def checkDemandsCalculations(self) -> None:

        if self.demand_system.getSite() is not None and self.demand_system.getSeismicResponse():

            if self.demand_system.getUnstableMass() is None:
                self.demand_system.unstable_mass = UnstableMass(site=self.demand_system.getSite())

                sd = self.demand_system.getStaticDemand()
                sd.calculateDemands()

                shd = self.demand_system.getShakedownDemand()
                shd.calculateDemands()

        fields = [
            self.demand_system.getSite(),
            self.demand_system.getSeismicResponse(),
            self.demand_system.getStrainburst(),
            self.demand_system.getPreviousDisplacement(),
            self.demand_system.getBulkingFactors(),
        ]

        if None in fields:
            return

        dd = self.demand_system.getDisplacementDemand()
        dd.calculateDemands()

        ed = self.demand_system.getEnergyDemand()
        ed.calculateDemands()
