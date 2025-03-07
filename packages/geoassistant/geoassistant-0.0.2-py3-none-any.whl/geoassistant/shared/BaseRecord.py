from typing import Optional, Union

import numpy as np

ValueType = Optional[Union[float, int, str, np.ndarray]]


class BaseRecord(object):

    def __init__(self,
                 value: ValueType,
                 units: Optional[str],
                 original_value: ValueType = None):
        self.value: ValueType = value
        self.units: Optional[str] = units
        self.original_value: ValueType = original_value

    def getValue(self) -> ValueType:
        return self.value

    def getUnits(self) -> Optional[str]:
        return self.units

    def getOriginalValue(self) -> ValueType:
        return self.original_value
