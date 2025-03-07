from typing import Optional, List, TYPE_CHECKING, Literal

from matplotlib import pyplot as plt

if TYPE_CHECKING:
    from geoassistant.ground_support.displacement_based.support_elements.SupportElement import SupportElement
    from geoassistant.ground_support.displacement_based.support_elements.SupportSystem import SupportSystem
    from geoassistant.ground_support.displacement_based.demand_elements.DemandSystem import DemandSystem


class CapacityPlot(object):

    def __init__(self):
        self.figure: Optional[plt.Figure] = None
        self.ax: Optional[plt.Axes] = None

        self.support_elements: List['SupportElement'] = []
        self.demand_systems: List['DemandSystem'] = []

    def addSupportElement(self, support_element: 'SupportElement') -> None:
        self.support_elements += [support_element]

    def addSupportSystem(self, support_system: 'SupportSystem') -> None:
        bsys = support_system.getBoltSystem()

        self.addSupportElement(bsys)
        for bs in bsys:
            self.addSupportElement(support_element=bs)

        ss = support_system.getSurfaceSupport()
        self.addSupportElement(support_element=ss)

        self.addSupportElement(support_element=support_system)

    def addDemandSystem(self, demand_system: 'DemandSystem') -> None:
        self.demand_systems += [demand_system]

    def getFigure(self) -> Optional[plt.Figure]:
        return self.figure

    def getAx(self) -> Optional[plt.Axes]:
        return self.ax

    def plot(self, capacity_type: Literal['used', 'remnant'] = 'remnant') -> None:
        self.figure = plt.figure()
        self.ax = self.figure.add_subplot(111)

        max_x, max_y = -1e6, -1e6
        for supp_element in self.support_elements:
            if capacity_type == 'remnant':
                xs, ys = supp_element.getRemnantEnergyCapacityCurve()
            else:
                xs, ys = supp_element.getUsedEnergyCapacityCurve()

            if max(xs) > max_x:
                max_x = max(xs)
            if max(ys) > max_y:
                max_y = max(ys)

            xs += [1e6]
            ys += [ys[-1]]

            self.ax.plot(xs, ys)

        for demand_system in self.demand_systems:
            demand_curve = demand_system.getEnergyDemandCurve()
            self.ax.plot(demand_curve[0], demand_curve[1], c='blue')

        self.ax.set_xlim(0, max_x * 1.2)
        self.ax.set_ylim(0, max_y * 1.2)

        self.ax.set_xlabel("Bolt Head Deflection [mm]")
        self.ax.set_ylabel(f"{capacity_type.capitalize()} Energy Capacity [kJ/m2]")

        self.ax.grid()

        plt.show()
