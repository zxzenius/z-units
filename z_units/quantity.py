from __future__ import annotations
from typing import List, Union

from .unit import Unit
from .unit_registry import UnitRegistry
from . import unit_registry as reg


class Quantity:
    """
    Class used to represent a Quantity

    A quantity has a value and a unit
    """

    def __init__(self, value, unit: Union[str, Unit] = None):
        self.value = value
        if unit is None:
            self._unit = self.unit_registry.base_unit
        else:
            self._unit = self.unit_registry.get_unit(str(unit))

    def to(self, unit: Union[str, Unit]):
        if self.value is None:
            return None
        ref_value = self._unit.to_base_unit(self.value)
        value = self.unit_registry.get_unit(str(unit)).from_base_unit(ref_value)
        return self.__class__(value, unit)

    @property
    def unit_registry(self) -> UnitRegistry:
        return self.get_unit_registry()

    def get_unit_registry(self):
        return UnitRegistry(reg.dimensionless)

    @property
    def base_unit(self) -> Unit:
        return self.unit_registry.base_unit

    @property
    def units(self) -> List[Unit]:
        return self.unit_registry.units

    def to_base(self):
        return self.to(self.base_unit.symbol)

    def __repr__(self):
        if isinstance(self.value, float):
            return f"<{self.__class__.__name__}({self.value:.9}, '{self.unit.symbol}')>"
        return f"<{self.__class__.__name__}({self.value}, '{self.unit.symbol}')>"

    def __str__(self):
        return f'{self.value}'

    def __format__(self, format_spec=''):
        if (pos := format_spec.find('u')) > -1:
            unit = format(self.unit, format_spec[pos + 1:])
            format_spec = format_spec[0:pos]
            if unit:
                return ' '.join([format(self.value, format_spec), unit])

        return format(self.value, format_spec)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return self.__class__(self.value * other, self.unit)

        return NotImplemented

    def __rmul__(self, other):
        return self * other

    @property
    def unit(self) -> Unit:
        return self._unit


class Length(Quantity):
    def get_unit_registry(self):
        return reg.length


class Area(Quantity):
    def get_unit_registry(self):
        return reg.area


class Volume(Quantity):
    def get_unit_registry(self):
        return reg.volume


class Time(Quantity):
    def get_unit_registry(self):
        return reg.time


class Mass(Quantity):
    def get_unit_registry(self):
        return reg.mass


class Force(Quantity):
    def get_unit_registry(self):
        return reg.force


class Substance(Quantity):
    def get_unit_registry(self):
        return reg.substance


class Energy(Quantity):
    def get_unit_registry(self):
        return reg.energy


class Velocity(Quantity):
    def get_unit_registry(self):
        return reg.velocity


class Temperature(Quantity):
    def get_unit_registry(self):
        return reg.temperature


class DeltaTemperature(Quantity):
    def get_unit_registry(self):
        return reg.delta_temperature


class Pressure(Quantity):
    def get_unit_registry(self):
        return reg.pressure


class VolumeFlow(Quantity):
    def get_unit_registry(self):
        return reg.volume_flow


class MassDensity(Quantity):
    def get_unit_registry(self):
        return reg.mass_density


class HeatFlow(Quantity):
    def get_unit_registry(self):
        return reg.heat_flow


class MolarFlow(Quantity):
    def get_unit_registry(self):
        return reg.molar_flow


class MassFlow(Quantity):
    def get_unit_registry(self):
        return reg.mass_flow


class MolarDensity(Quantity):
    def get_unit_registry(self):
        return reg.molar_density


class MolarHeatCapacity(Quantity):
    def get_unit_registry(self):
        return reg.molar_heat_capacity


class MolarEntropy(Quantity):
    def get_unit_registry(self):
        return reg.molar_entropy


class MolarHeat(Quantity):
    def get_unit_registry(self):
        return reg.molar_heat


class ThermalConductivity(Quantity):
    def get_unit_registry(self):
        return reg.thermal_conductivity


class Viscosity(Quantity):
    def get_unit_registry(self):
        return reg.viscosity


class SurfaceTension(Quantity):
    def get_unit_registry(self):
        return reg.surface_tension


class MassHeatCapacity(Quantity):
    def get_unit_registry(self):
        return reg.mass_heat_capacity


class MassEntropy(Quantity):
    def get_unit_registry(self):
        return reg.mass_entropy


class MassHeat(Quantity):
    def get_unit_registry(self):
        return reg.mass_heat


class StandardGasFlow(Quantity):
    def get_unit_registry(self):
        return reg.standard_gas_flow


class KinematicViscosity(Quantity):
    def get_unit_registry(self):
        return reg.kinematic_viscosity


class MolarVolume(Quantity):
    def get_unit_registry(self):
        return reg.molar_volume


class Fraction(Quantity):
    def get_unit_registry(self):
        return reg.fraction


class Dimensionless(Quantity):
    def get_unit_registry(self):
        return reg.dimensionless
