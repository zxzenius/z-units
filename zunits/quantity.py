from __future__ import annotations

import re
from functools import cached_property

from .unit import Unit
from .unit_registry import UnitRegistry
from . import unit_registry as reg
from .util import camel_to_snake


class Quantity:
    """
    Class used to represent a Quantity

    A quantity has a value and a unit
    """

    # unit_registry: UnitRegistry = None

    def __init__(self, value, unit: str | Unit = None):
        if isinstance(value, str):
            match = re.match(r"(?P<v>[+-]?((\d+\.\d*)|(\.\d+)|(\d+))([eE][+-]?\d+)?)(?P<u>.*)", value.strip())
            if match:
                res_dict = match.groupdict()
                self.value = float(res_dict['v'])
                if not unit:
                    self.unit = res_dict['u'].strip()
                else:
                    self.unit = unit
        else:
            self.value = value
            self.unit = unit

    def to(self, unit: str | Unit):
        if self.value is None:
            return None
        unit = self.unit_registry.get_unit(str(unit))
        if unit == self.unit:
            return self
        ref_value = self._unit.to_base_unit(self.value)
        value = unit.from_base_unit(ref_value)
        return self.__class__(value, unit)

    @classmethod
    def get_unit_registry(cls) -> UnitRegistry:
        return getattr(reg, camel_to_snake(cls.__name__))

    @cached_property
    def unit_registry(self):
        return self.get_unit_registry()

    @property
    def base_unit(self) -> Unit:
        return self.unit_registry.base_unit

    @property
    def units(self) -> list[Unit]:
        return self.unit_registry.units

    def to_base(self):
        return self.to(self.base_unit)

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

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.to_base().value == other.to_base().value

        return False

    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self.to_base().value > other.to_base().value

    def __ge__(self, other):
        if isinstance(other, self.__class__):
            return self.to_base().value >= other.to_base().value

    @property
    def unit(self) -> Unit:
        return self._unit

    @unit.setter
    def unit(self, value):
        if not value:
            self._unit = self.unit_registry.base_unit
        else:
            self._unit = self.unit_registry.get_unit(str(value))


class Length(Quantity):
    pass


class Area(Quantity):
    pass


class Volume(Quantity):
    pass


class Time(Quantity):
    pass


class Mass(Quantity):
    pass


class Force(Quantity):
    pass


class Substance(Quantity):
    pass


class Energy(Quantity):
    pass


class Velocity(Quantity):
    pass


class Temperature(Quantity):
    pass


class DeltaTemperature(Quantity):
    pass


class Pressure(Quantity):
    pass


class VolumeFlow(Quantity):
    pass


class MassDensity(Quantity):
    pass


class HeatFlow(Quantity):
    pass


class MolarFlow(Quantity):
    pass


class MassFlow(Quantity):
    pass


class MolarDensity(Quantity):
    pass


class MolarHeatCapacity(Quantity):
    pass


class MolarEntropy(Quantity):
    pass


class MolarHeat(Quantity):
    pass


class ThermalConductivity(Quantity):
    pass


class Viscosity(Quantity):
    pass


class SurfaceTension(Quantity):
    pass


class MassHeatCapacity(Quantity):
    pass


class MassEntropy(Quantity):
    pass


class MassHeat(Quantity):
    pass


class StandardGasFlow(Quantity):
    pass


class KinematicViscosity(Quantity):
    pass


class MolarVolume(Quantity):
    pass


class Fraction(Quantity):
    pass


class Dimensionless(Quantity):
    pass
