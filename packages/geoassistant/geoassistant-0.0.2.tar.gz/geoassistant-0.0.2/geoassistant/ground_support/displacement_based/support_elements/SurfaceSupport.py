import json
import pkgutil
from typing import Optional, TYPE_CHECKING, Tuple, List

from geoassistant.ground_support.displacement_based.support_elements.SupportElement import SupportElement

from geoassistant.ground_support.displacement_based.support_elements.surfacesupport_components.SurfaceSupportProperties import SurfaceSupportProperties
from geoassistant.ground_support.displacement_based.support_elements.surfacesupport_components.SurfaceSupportCalculations import SurfaceSupportCalculations

if TYPE_CHECKING:
    pass


class SurfaceSupport(SupportElement, SurfaceSupportProperties):

    def __init__(self, name: Optional[str]):
        super().__init__(name=name)

        self.calculations: SurfaceSupportCalculations = SurfaceSupportCalculations(self)

    def getUsedEnergyCapacityCurve(self) -> Tuple[List[float], List[float]]:
        xs = [0, self.getDisplacementCapacity()]
        ys = [0, self.getEnergyCapacity()]

        return xs, ys

    def calculateUsedEnergyAtDisplacement(self, displacement: float) -> Optional[float]:
        return self.calculations.calculateUsedEnergyAtDisplacement(displacement=displacement)

    @staticmethod
    def loadFromBaseCatalog(surface_support_id: str) -> Optional['SurfaceSupport']:
        data = pkgutil.get_data('geoassistant.ground_support.displacement_based.catalogs', 'surface_support_catalog.json')

        cat = json.loads(data.decode('utf-8'))

        if cat.get(surface_support_id) is None:
            raise ValueError(f"SurfaceSupport '{surface_support_id}' not found in base catalog.")

        surface_support_info = cat[surface_support_id]

        ss = SurfaceSupport(name=surface_support_id)
        ss.setNominalEnergyCapacity(nominal_energy_capacity=surface_support_info['nominal_energy_capacity'])
        ss.setNominalDisplacementCapacity(nominal_displacement_capacity=surface_support_info['nominal_displacement_capacity'])

        return ss
