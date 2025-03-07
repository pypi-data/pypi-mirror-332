from typing import Optional


class StrainburstProperties(object):

    def __init__(self):

        self.strainburst_depth: Optional[float] = None
        self.rupture_time: Optional[float] = None  # Also known as bulking time, fracture time

    def setStrainburstDepth(self, strainburst_depth: float) -> None:
        self.strainburst_depth = strainburst_depth

    def setRuptureTime(self, rupture_time: float) -> None:
        self.rupture_time = rupture_time

    def getStrainburstDepth(self) -> Optional[float]:
        return self.strainburst_depth

    def getRuptureTime(self) -> Optional[float]:
        return self.rupture_time
