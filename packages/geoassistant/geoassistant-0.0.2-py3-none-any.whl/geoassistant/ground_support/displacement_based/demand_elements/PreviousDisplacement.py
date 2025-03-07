from typing import Optional


class PreviousDisplacement(object):

    def __init__(self):
        self.d0: Optional[float] = None

    def setD0(self, d0: float) -> None:
        self.d0 = d0

    def getD0(self) -> Optional[float]:
        return self.d0
