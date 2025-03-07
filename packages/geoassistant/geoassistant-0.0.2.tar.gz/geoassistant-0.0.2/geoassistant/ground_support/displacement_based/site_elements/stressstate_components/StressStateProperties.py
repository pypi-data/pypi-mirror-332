from typing import Optional


class StressStateProperties(object):

    def __init__(self):

        self.stress_level: Optional[float] = None

    def setStressLevel(self, stress_level: float) -> None:
        self.stress_level = stress_level

    def getStressLevel(self) -> Optional[float]:
        return self.stress_level
