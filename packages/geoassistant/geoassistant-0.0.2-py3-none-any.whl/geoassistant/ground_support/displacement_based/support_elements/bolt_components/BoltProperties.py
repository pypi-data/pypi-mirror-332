from typing import Optional

from geoassistant.ground_support.displacement_based.support_elements.bolt_components.BoltCalculations import BoltCalculations


class BoltProperties(object):

    def __init__(self):
        # Average Load Capacity [kN]
        self.Fm_D: Optional[float] = None
        self.Fm_ID: Optional[float] = None
        # Ultimate displacement capacity [mm] (after initiation)
        self.du_D: Optional[float] = None
        self.du_ID: Optional[float] = None
        # Activation displacement [mm]
        self.di: Optional[float] = None

        self.displacement_split_factor: Optional[float] = None

        self.calculations: Optional['BoltCalculations'] = None

    def setFm_D(self, Fm_D: float) -> None:
        self.Fm_D = Fm_D

    def setFm_ID(self, Fm_ID: float) -> None:
        self.Fm_ID = Fm_ID

    def setDu_D(self, du_D: float) -> None:
        self.du_D = du_D
        self.calculations.checkCapacityCalculations()

    def setDu_ID(self, du_ID: float) -> None:
        self.du_ID = du_ID
        self.calculations.checkCapacityCalculations()

    def setDi(self, di: float) -> None:
        self.di = di
        self.calculations.checkCapacityCalculations()

    def setDisplacementSplitFactor(self, displacement_split_factor: float) -> None:
        self.displacement_split_factor = displacement_split_factor
        self.calculations.checkCapacityCalculations()

    def getFm_D(self) -> Optional[float]:
        return self.Fm_D

    def getFm_ID(self) -> Optional[float]:
        return self.Fm_ID

    def getDu_D(self) -> Optional[float]:
        return self.du_D

    def getDu_ID(self) -> Optional[float]:
        return self.du_ID

    def getDi(self) -> Optional[float]:
        return self.di

    def getDisplacementSplitFactor(self) -> Optional[float]:
        return self.displacement_split_factor

    def getDisplacementCapacity(self) -> Optional[float]:
        return self.calculations.getDisplacementCapacity()
