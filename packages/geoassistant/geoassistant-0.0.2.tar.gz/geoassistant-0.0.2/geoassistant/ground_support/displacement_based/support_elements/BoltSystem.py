from typing import Optional, TYPE_CHECKING, List, Iterator, Union, Tuple

from geoassistant.ground_support.displacement_based.support_elements.SupportElement import SupportElement
from geoassistant.ground_support.displacement_based.support_elements.boltsystem_components.BoltSystemProperties import BoltSystemProperties
from geoassistant.ground_support.displacement_based.support_elements.boltsystem_components.BoltSystemCalculations import BoltSystemCalculations
from geoassistant.ground_support.displacement_based.support_elements.boltsystem_components.BoltSystemPlotter import BoltSystemPlotter

if TYPE_CHECKING:
    from geoassistant.ground_support.displacement_based.support_elements.BoltSet import BoltSet


class BoltSystem(SupportElement, BoltSystemProperties):

    def __init__(self, name: Optional[str]):
        super().__init__(name=name)

        self.calculations: BoltSystemCalculations = BoltSystemCalculations(self)
        self.plotter: BoltSystemPlotter = BoltSystemPlotter(self)

    def __iter__(self) -> Iterator['BoltSet']:
        for b in self.bolt_sets:
            yield b

    def __len__(self) -> int:
        return len(self.bolt_sets)

    def __getitem__(self, key: Union[int, str]) -> Optional['BoltSet']:
        if isinstance(key, int):
            return self.bolt_sets[key]
        else:
            bs = [bs for bs in self if bs.getName() == key]
            if not len(bs):
                raise ValueError(f"Bolt set '{key}' not found in system.")
            elif len(bs) > 1:
                raise ValueError(f"Bolt set '{key}' found more than once in system.")

            return bs[0]

    def getUsedEnergyCapacityCurve(self) -> Tuple[List[float], List[float]]:
        xs = [0, self.getDi()]
        ys = [0, 0]

        sorted_bs = sorted(self, key=lambda _bs: _bs.getDisplacementCapacity())
        for bs in sorted_bs:
            x = bs.getDisplacementCapacity()
            y = self.calculateUsedEnergyAtDisplacement(displacement=x)

            xs += [x]
            ys += [y]

        return xs, ys

    def calculateUsedEnergyAtDisplacement(self, displacement: float) -> Optional[float]:
        return self.calculations.calculateUsedEnergyAtDisplacement(displacement=displacement)

    def plotCapacityCurve(self) -> None:
        self.plotter.plotCapacityCurve()
