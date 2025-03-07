from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from geoassistant.ground_support.displacement_based.support_elements.SurfaceSupport import SurfaceSupport


class SurfaceSupportCalculations(object):

    def __init__(self, surface_support: 'SurfaceSupport'):
        self.surface_support: 'SurfaceSupport' = surface_support

        self.displacement_capacity: Optional[float] = None
        self.energy_capacity: Optional[float] = None

        self.equivalent_spacing_before: Optional[float] = None
        self.equivalent_spacing_after: Optional[float] = None

    def getDisplacementCapacity(self) -> Optional[float]:
        return self.displacement_capacity

    def getEnergyCapacity(self) -> Optional[float]:
        return self.energy_capacity

    def getEquivalentSpacingBefore(self) -> Optional[float]:
        return self.equivalent_spacing_before

    def getEquivalentSpacingAfter(self) -> Optional[float]:
        return self.equivalent_spacing_after

    def calculateEquivalentSpacings(self) -> None:

        bolt_system = self.surface_support.support_system.getBoltSystem()

        self.equivalent_spacing_before = bolt_system.getEquivalentSpacing()

        if len(bolt_system) == 1:
            self.equivalent_spacing_after = self.equivalent_spacing_before
        else:
            bs1 = bolt_system[0]
            bs2 = bolt_system[1]

            if bs1.bolt.getDisplacementCapacity() < bs2.bolt.getDisplacementCapacity():
                remaining_bs = bs2
            else:
                remaining_bs = bs1

            self.equivalent_spacing_after = remaining_bs.getNormalizedSpacing()

    def calculateEffectiveDisplacementCapacity(self) -> None:
        nominal_displacement_capacity = self.surface_support.getNominalDisplacementCapacity()

        if self.surface_support.support_system is not None:

            bsys = self.surface_support.support_system.getBoltSystem()

            if bsys.getDisplacementCapacity() < nominal_displacement_capacity:
                self.displacement_capacity = bsys.getDisplacementCapacity()
            else:
                self.displacement_capacity = nominal_displacement_capacity
        else:
            self.displacement_capacity = nominal_displacement_capacity

    def calculateEffectiveEnergyCapacity(self) -> None:
        """
        If surface support is part of a support system, then its capacities are tied to the bolt system capacities.
        """
        nominal_energy_capacity = self.surface_support.getNominalEnergyCapacity()
        if self.surface_support.support_system is not None:

            bsys = self.surface_support.support_system.getBoltSystem()

            nominal_displacement_capacity = self.surface_support.getNominalDisplacementCapacity()

            if bsys.getDisplacementCapacity() < nominal_displacement_capacity:
                self.energy_capacity = nominal_energy_capacity * (bsys.getDisplacementCapacity() / nominal_displacement_capacity)
            else:
                self.energy_capacity = nominal_energy_capacity
        else:
            self.energy_capacity = nominal_energy_capacity

    def calculateUsedEnergyAtDisplacement(self, displacement: float) -> Optional[float]:
        if displacement < 0.:
            raise ValueError(f"Trying to evaluate using negative displacement: {displacement} [mm]")

        if not displacement:
            return 0

        if displacement >= self.displacement_capacity:
            return self.energy_capacity

        y = self.energy_capacity * (displacement / self.displacement_capacity)

        return y

