from typing import Union, List, Optional, Tuple

import numpy as np


class NumericalMetrics(object):

    def __init__(self, values: Union[List, np.ndarray],
                 limits: Optional[Tuple[float, float]] = None,
                 include_limits: bool = False,
                 include_lower_limit: bool = False,
                 include_upper_limit: bool = False):

        self.limits: Optional[Tuple[float, float]] = limits
        self.include_limits: bool = include_limits
        self.include_lower_limit: bool = include_lower_limit
        self.include_upper_limit: bool = include_upper_limit

        self.n_original_values: Optional[int] = None
        self.n_valid_values: Optional[int] = None
        self.n_invalid_values: Optional[int] = None

        self.minimum: Optional[float] = None
        self.maximum: Optional[float] = None
        self.average: Optional[float] = None
        self.std: Optional[float] = None

        self._calculateMetrics(values=values, valid_values=self._calculateValidValues(values))

    def _calculateValidValues(self, values: Union[List, np.ndarray]) -> np.ndarray:

        valid_values = [v for v in values if v is not None]

        if self.limits is None:
            return np.array(valid_values)

        if self.include_limits:
            valid_values = valid_values[(valid_values >= self.limits[0]) & (valid_values <= self.limits[1])]
            return np.array(valid_values)

        if self.include_lower_limit:
            valid_values = valid_values[(valid_values >= self.limits[0]) & (valid_values < self.limits[1])]
            return np.array(valid_values)

        if self.include_upper_limit:
            valid_values = valid_values[(valid_values > self.limits[0]) & (valid_values <= self.limits[1])]
            return np.array(valid_values)

    def _calculateMetrics(self, values: np.ndarray, valid_values: np.ndarray) -> None:

        self.n_original_values = len(values)

        if len(valid_values) < 2:
            self.n_valid_values = 0
            self.n_invalid_values = self.n_original_values
            return

        self.n_original_values = len(values)
        self.n_valid_values = len(valid_values)
        self.n_invalid_values = self.n_original_values - self.n_valid_values

        self.minimum = np.min(valid_values)
        self.maximum = np.max(valid_values)
        self.average = np.average(valid_values)
        self.std = np.std(valid_values)

    def getMinimum(self) -> Optional[float]:
        return self.minimum

    def getMaximum(self) -> Optional[float]:
        return self.maximum

    def getAverage(self) -> Optional[float]:
        return self.average

    def getStd(self) -> Optional[float]:
        return self.std
