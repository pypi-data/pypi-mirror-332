from typing import TYPE_CHECKING, Optional

import numpy as np

if TYPE_CHECKING:
    from geoassistant.ground_support.displacement_based.support_elements.SupportSystem import SupportSystem


class SupportSystemCalculations(object):

    def __init__(self, support_system: 'SupportSystem'):
        self.support_system: 'SupportSystem' = support_system

        self.static_capacity: Optional[float] = None
        self.displacement_capacity: Optional[float] = None
        self.energy_capacity: Optional[float] = None

    def getStaticCapacity(self) -> Optional[float]:
        return self.static_capacity

    def getDisplacementCapacity(self) -> Optional[float]:
        return self.displacement_capacity

    def getEnergyCapacity(self) -> Optional[float]:
        return self.energy_capacity

    def checkCapacitiesCalculation(self) -> None:
        if self.support_system.getBoltSystem() is not None and self.support_system.getSurfaceSupport() is not None:
            self.calculateStaticCapacity()
            self.calculateDisplacementCapacity()
            self.calculateEnergyCapacity()

    def calculateStaticCapacity(self) -> None:
        load_capacity = 0
        for bs in self.support_system.getBoltSystem():
            load_capacity += bs.getBolt().getFm_D() * bs.getBoltsPerArea()

        self.static_capacity = load_capacity

    def calculateDisplacementCapacity(self) -> None:
        self.displacement_capacity = self.support_system.getBoltSystem().getDisplacementCapacity()

    def calculateEnergyCapacity(self) -> None:
        energy_capacity = 0
        energy_capacity += self.support_system.getBoltSystem().getEnergyCapacity()
        energy_capacity += self.support_system.getSurfaceSupport().getEnergyCapacity()

        self.energy_capacity = energy_capacity

    def calculateUsedEnergyAtDisplacement(self, displacement: float) -> Optional[float]:
        y = 0
        y += self.support_system.getBoltSystem().calculateUsedEnergyAtDisplacement(displacement=displacement)
        y += self.support_system.getSurfaceSupport().calculateUsedEnergyAtDisplacement(displacement=displacement)

        return y

    def calculateDisplacementAtRemnantEnergy(self, remnant_energy: float) -> Optional[float]:

        if remnant_energy < 0.:
            raise ValueError("Negative energy.")

        if remnant_energy > self.energy_capacity:
            raise ValueError("Remnant energy greater than total energy capacity.")

        if not remnant_energy:
            return self.displacement_capacity

        xs, ys = self.support_system.getRemnantEnergyCapacityCurve()

        idy = np.searchsorted(ys, remnant_energy)
        x1, y1 = xs[idy - 1], ys[idy - 1]
        x2, y2 = xs[idy], ys[idy]

        x = x1 + (remnant_energy - y1) * (x2-x1) / (y2-y1)

        return x
