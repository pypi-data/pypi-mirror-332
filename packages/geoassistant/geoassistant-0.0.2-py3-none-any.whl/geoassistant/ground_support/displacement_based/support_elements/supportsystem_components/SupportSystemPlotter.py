from typing import TYPE_CHECKING

from geoassistant.ground_support.displacement_based.plots.CapacityPlot import CapacityPlot

if TYPE_CHECKING:
    from geoassistant.ground_support.displacement_based.support_elements.SupportSystem import SupportSystem


class SupportSystemPlotter(object):

    def __init__(self, support_system: 'SupportSystem'):
        self.support_system: 'SupportSystem' = support_system

    def plotCapacityCurve(self) -> None:
        capacity_plot = CapacityPlot()
        capacity_plot.addSupportSystem(support_system=self.support_system)
        capacity_plot.plot()
