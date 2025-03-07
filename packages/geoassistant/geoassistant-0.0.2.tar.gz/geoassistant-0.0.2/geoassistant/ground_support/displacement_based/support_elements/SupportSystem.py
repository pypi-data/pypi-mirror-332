from typing import Optional, Tuple, List

import numpy as np

from geoassistant.ground_support.displacement_based.support_elements.SupportElement import SupportElement
from geoassistant.ground_support.displacement_based.support_elements.SurfaceSupport import SurfaceSupport

from geoassistant.ground_support.displacement_based.support_elements.supportsystem_components.SupportSystemProperties import SupportSystemProperties
from geoassistant.ground_support.displacement_based.support_elements.supportsystem_components.SupportSystemCalculations import SupportSystemCalculations


class SupportSystem(SupportElement, SupportSystemProperties):

    def __init__(self, name: Optional[str]):
        super().__init__(name=name)

        self.calculations: SupportSystemCalculations = SupportSystemCalculations(self)

    def setSurfaceSupport(self, surface_support: 'SurfaceSupport') -> None:
        self.surface_support = surface_support
        self.surface_support.setSupportSystem(self)

        self.calculations.checkCapacitiesCalculation()

    def calculateUsedEnergyAtDisplacement(self, displacement: float) -> Optional[float]:
        return self.calculations.calculateUsedEnergyAtDisplacement(displacement=displacement)

    def calculateDisplacementAtRemnantEnergy(self, remnant_energy: float) -> Optional[float]:
        return self.calculations.calculateDisplacementAtRemnantEnergy(remnant_energy=remnant_energy)

    def getUsedEnergyCapacityCurve(self) -> Tuple[List[float], List[float]]:

        # xs = [0]
        # for bs in self.bolt_system:
        #     xs += [bs.getDi()]
        #     xs += [bs.getDisplacementCapacity()]
        #
        # xs += [self.surface_support.getDisplacementCapacity()]
        #
        # xs = list(set(xs))
        xs = list(np.arange(start=0, stop=self.surface_support.getDisplacementCapacity()+5, step=5))
        ys = [self.calculateUsedEnergyAtDisplacement(displacement=x) for x in xs]

        return xs, ys
