from typing import Literal, TYPE_CHECKING, Optional

import numpy as np

from geoassistant.shared.BaseBin import BaseBin
from geoassistant.shared.BaseCollection import BaseCollection

if TYPE_CHECKING:
    from geoassistant.seismic.SeismicEventsCollection import SeismicEventsCollection


class SeismicEventsBins(BaseCollection['SeismicEventsBins', 'BaseBin']):

    def __init__(self, name:  Optional[str] = None):
        super().__init__(name=name)

        # self.bins_array: np.ndarray = np.array([_bin.getLowerLimit() for _bin in self] + [self[-1].getUpperLimit()])
        # self.frequencies_array: np.ndarray = np.array([len(_bin) for _bin in self])

    def getMidValuesArray(self) -> np.ndarray:
        return np.array([_bin.getMidValue() for _bin in self])

    def getBinsArray(self) -> np.ndarray:
        return np.array([_bin.getLowerLimit() for _bin in self] + [self[-1].getUpperLimit()])

    def getFrequenciesArray(self) -> np.ndarray:
        return np.array([len(_bin) for _bin in self])

    @staticmethod
    def createBinsByLocalMagnitude(seismic_collection: 'SeismicEventsCollection', interval: float) -> 'SeismicEventsBins':

        lower = seismic_collection.getMinimumLocalMagnitude()
        upper = seismic_collection.getMaximumLocalMagnitude()

        # Generate bins from 0 to lower and upper values
        bins_lower = np.arange(0, lower - interval, -interval)[::-1]  # Descending to lower
        bins_upper = np.arange(0, upper + interval, interval)  # Ascending to upper
        bins = np.unique(np.concatenate((bins_lower, bins_upper)))

        c = SeismicEventsBins()
        for i, bin_start in enumerate(bins[:-1]):
            if (i+1) != len(bins)-1:
                bin_collection = seismic_collection.getSubsetWithinMagnitudes(lower_magnitude=bin_start,
                                                                              upper_magnitude=bins[i+1],
                                                                              include_lower_limit=True)
            else:
                bin_collection = seismic_collection.getSubsetWithinMagnitudes(lower_magnitude=bin_start,
                                                                              upper_magnitude=bins[i + 1],
                                                                              include_limits=True)
            _bin = BaseBin(variable_id='Local Magnitude')
            for ev in bin_collection:
                _bin.addElement(ev)
            _bin.setLowerLimit(lower_limit=bin_start)
            _bin.setUpperLimit(upper_limit=bins[i+1])
            _bin.calculateMidValue()
            c.addElement(element=_bin)

        return c
