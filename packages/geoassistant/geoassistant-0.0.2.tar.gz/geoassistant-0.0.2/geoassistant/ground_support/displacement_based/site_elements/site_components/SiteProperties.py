from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from geoassistant.ground_support.displacement_based.site_elements.RockMass import RockMass
    from geoassistant.ground_support.displacement_based.site_elements.StressState import StressState
    from geoassistant.ground_support.displacement_based.site_elements.Excavation import Excavation


class SiteProperties(object):

    def __init__(self):
        self.rock_mass: Optional['RockMass'] = None
        self.excavation: Optional['Excavation'] = None
        self.stress_state: Optional['StressState'] = None

    def setRockMass(self, rock_mass: 'RockMass') -> None:
        self.rock_mass = rock_mass

    def setExcavation(self, excavation: 'Excavation') -> None:
        self.excavation = excavation

    def setStressState(self, stress_state: 'StressState') -> None:
        self.stress_state = stress_state

    def getRockMass(self) -> Optional['RockMass']:
        return self.rock_mass

    def getExcavation(self) -> Optional['Excavation']:
        return self.excavation

    def getStressState(self) -> Optional['StressState']:
        return self.stress_state
