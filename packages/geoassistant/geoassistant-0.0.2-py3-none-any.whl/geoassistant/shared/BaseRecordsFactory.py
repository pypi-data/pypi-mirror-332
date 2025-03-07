from typing import Union, List, Type, Any, Optional

import datetime

import numpy as np

from geoassistant.shared.BaseRecord import BaseRecord

ExpectedType = Union[Type[float], Type[int], Type[str], Type[datetime.datetime], Type[np.ndarray]]


class BaseRecordsFactory(object):

    def __init__(self,
                 field_name: str,
                 expected_type: ExpectedType,
                 expected_units: Optional[List[str]]):

        self.field_name: str = field_name
        self.type: ExpectedType = expected_type
        self.expected_units: Optional[List[str]] = expected_units

    def create(self, value: Any, units: Optional[str] = None) -> BaseRecord:

        if units is None:
            if self.expected_units is not None:
                raise ValueError(f"'No units' not valid for field '{self.field_name}'")
        else:
            if self.expected_units is None:
                raise ValueError(f"Units '[{units}]' set for 'No units' field '{self.field_name}')")

            if units not in self.expected_units:
                raise ValueError(f"Units '[{units}]' not valid for field '{self.field_name}'")

        if self.type == datetime.datetime:
            if isinstance(value, datetime.datetime):
                valid_value = value
            else:
                valid_value = None
        elif self.type == np.ndarray:
            if isinstance(value, np.ndarray):
                valid_value = value
            else:
                valid_value = None
        else:
            try:
                valid_value = self.type(value)
            except ValueError:
                valid_value = None

        return BaseRecord(value=valid_value, units=units, original_value=value)
