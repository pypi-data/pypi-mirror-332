from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from geoassistant.ground_support.displacement_based.support_elements.SupportSystem import SupportSystem
    from geoassistant.ground_support.displacement_based.support_elements.surfacesupport_components.SurfaceSupportCalculations import SurfaceSupportCalculations


class SurfaceSupportProperties(object):

    def __init__(self):
        self.nominal_energy_capacity: Optional[float] = None
        self.nominal_displacement_capacity: Optional[float] = None

        self.support_system: Optional['SupportSystem'] = None

        self.calculations: Optional['SurfaceSupportCalculations'] = None

    def setNominalEnergyCapacity(self, nominal_energy_capacity: float) -> None:
        self.nominal_energy_capacity = nominal_energy_capacity

    def setNominalDisplacementCapacity(self, nominal_displacement_capacity: float) -> None:
        self.nominal_displacement_capacity = nominal_displacement_capacity

    def setSupportSystem(self, support_system: 'SupportSystem') -> None:
        self.support_system = support_system

        self.calculations.calculateEquivalentSpacings()
        self.calculations.calculateEffectiveDisplacementCapacity()
        self.calculations.calculateEffectiveEnergyCapacity()

    def getNominalDisplacementCapacity(self) -> Optional[float]:
        return self.nominal_displacement_capacity

    def getNominalEnergyCapacity(self) -> Optional[float]:
        return self.nominal_energy_capacity

    def getDisplacementCapacity(self) -> Optional[float]:
        return self.calculations.getDisplacementCapacity()

    def getEnergyCapacity(self) -> Optional[float]:
        return self.calculations.getEnergyCapacity()

    def getEquivalentSpacingBefore(self) -> Optional[float]:
        return self.calculations.getEquivalentSpacingBefore()

    def getEquivalentSpacingAfter(self) -> Optional[float]:
        return self.calculations.getEquivalentSpacingAfter()
