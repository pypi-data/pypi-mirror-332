from typing import Optional


class BulkingFactorsProperties(object):

    def __init__(self):

        self.static_bulking_factor: Optional[float] = None
        self.dynamic_bulking_factor: Optional[float] = None

    def setStaticBulkingFactor(self, static_bulking_factor: float) -> None:
        self.static_bulking_factor = static_bulking_factor

    def setDynamicBulkingFactor(self, dynamic_bulking_factor: float) -> None:
        self.dynamic_bulking_factor = dynamic_bulking_factor

    def getStaticBulkingFactor(self) -> Optional[float]:
        return self.static_bulking_factor

    def getDynamicBulkingFactor(self) -> Optional[float]:
        return self.dynamic_bulking_factor
