from typing import TYPE_CHECKING, Optional, Dict, Tuple

import matplotlib.pyplot as plt
import numpy as np

from geoassistant.ground_support.displacement_based.plots.CapacityPlot import CapacityPlot

if TYPE_CHECKING:
    from geoassistant.ground_support.displacement_based.support_elements.BoltSystem import BoltSystem


class BoltSystemPlotter(object):

    def __init__(self, bolt_system: 'BoltSystem'):
        self.bolt_system: 'BoltSystem' = bolt_system

    def plotCapacityCurve(self) -> None:

        capacity_plot = CapacityPlot()

        capacity_plot.addSupportElement(self.bolt_system)
        for bs in self.bolt_system:
            capacity_plot.addSupportElement(support_element=bs)

        capacity_plot.plot()
