import json
import pkgutil

from typing import Optional, Tuple, List

from geoassistant.ground_support.displacement_based.support_elements.SupportElement import SupportElement
# from geoassistant.shared.BaseObject import BaseObject

from geoassistant.ground_support.displacement_based.support_elements.bolt_components.BoltProperties import BoltProperties
from geoassistant.ground_support.displacement_based.support_elements.bolt_components.BoltCalculations import BoltCalculations


class Bolt(SupportElement, BoltProperties):

    def __init__(self, name: Optional[str]):
        super().__init__(name=name)

        self.calculations: BoltCalculations = BoltCalculations(self)

    def getUsedEnergyCapacityCurve(self) -> Tuple[List[float], List[float]]: ...

    def getEnergyCapacity(self) -> Optional[float]: ...

    def calculateUsedEnergyAtDisplacement(self, displacement: float) -> Optional[float]: ...

    @staticmethod
    def loadFromBaseCatalog(bolt_id: str) -> Optional['Bolt']:
        data = pkgutil.get_data('geoassistant.ground_support.displacement_based.catalogs', 'bolt_catalog.json')

        cat = json.loads(data.decode('utf-8'))

        if cat.get(bolt_id) is None:
            raise ValueError(f"Bolt '{bolt_id}' not found in base catalog.")

        bolt_info = cat[bolt_id]

        b = Bolt(name=bolt_id)
        b.setFm_D(Fm_D=bolt_info['Fm_D'])
        b.setFm_ID(Fm_ID=bolt_info['Fm_ID'])
        b.setDu_D(du_D=bolt_info['du_D'])
        b.setDu_ID(du_ID=bolt_info['du_ID'])
        b.setDi(di=bolt_info['di'])

        return b
