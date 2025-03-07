from typing import TYPE_CHECKING, Optional

import matplotlib.pyplot as plt

from geoassistant.ground_support.displacement_based.plots.CapacityPlot import CapacityPlot

if TYPE_CHECKING:
    from geoassistant.ground_support.displacement_based.support_elements.BoltSet import BoltSet


class BoltSetPlotter(object):

    def __init__(self, bolt_set: 'BoltSet'):
        self.bolt_set: 'BoltSet' = bolt_set

    def plotCapacityCurve(self) -> None:

        capacity_plot = CapacityPlot()

        capacity_plot.addSupportElement(support_element=self.bolt_set)

        capacity_plot.plot()

