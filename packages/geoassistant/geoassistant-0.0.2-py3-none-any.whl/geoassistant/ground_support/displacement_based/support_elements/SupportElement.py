from abc import ABC, abstractmethod
from typing import Optional, Tuple, List

from geoassistant.shared.BaseObject import BaseObject


class SupportElement(BaseObject, ABC):

    def __init__(self, name: Optional[str]):
        super().__init__(name=name)

    @abstractmethod
    def getUsedEnergyCapacityCurve(self) -> Tuple[List[float], List[float]]: ...

    def getRemnantEnergyCapacityCurve(self) -> Tuple[List[float], List[float]]:
        xs, ys = self.getUsedEnergyCapacityCurve()
        new_ys = [self.getEnergyCapacity() - y for y in ys]

        return xs, new_ys

    @abstractmethod
    def calculateUsedEnergyAtDisplacement(self, displacement: float) -> Optional[float]: ...

    def calculateRemnantEnergyAtDisplacement(self, displacement: float) -> float:
        return self.getEnergyCapacity() - self.calculateUsedEnergyAtDisplacement(displacement=displacement)

