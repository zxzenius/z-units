from __future__ import annotations
from typing import Union, Callable, Iterable

from .config import get_local_atmospheric_pressure, get_standard_temperature
from .util import multi_replace
from . import constant


class Unit:
    """
    Class used to represent a Unit.

    For unit conversion, units belong to same 'family' (unit set)
    shall be converted from/to one 'base unit' as reference.

    Creation: unit = Unit(name[, factor, offset])

    name: str
        the quick style name(symbol) of the unit,
        example: 'kg/s', 'm3/s', 'kJ/mol-C'

        Simple form used to represent definition, as:
        'm3' = 'm**3', 'mol-C' = 'mol*C'

    factor, offset: numeric value or function,
        for converting this unit to base unit.

        unit * factor + offset = base unit

    If unit conversion is nonlinear, to_base_unit() & from_base_unit()
    have to be overridden.

    Example
    -------
    >>> kilometer = Unit('km', factor=1e3)

    Which meter is base unit

    Properties
    ----------
    symbol: str
        the quick style name(symbol) of the unit.

    factor: float
        factor value

    offset: float
        offset value
    """

    def __init__(self, symbol: str, defined_by=None, factor: Union[float, Callable] = 1,
                 offset: Union[float, Callable] = 0, aliases: Iterable[str] = []):
        if isinstance(defined_by, Unit):
            factor = defined_by.factor

        if factor == 0:
            raise ValueError("Factor shall not be 0")

        self._symbol = symbol.replace(' ', '')
        self._factor = factor
        self._offset = offset
        self.aliases = aliases

    def to_base_unit(self, value: float):
        """
        Convert value from this unit to base unit
        :param value: numerical value
        :return: converted value
        """
        return self.factor * value + self.offset

    def from_base_unit(self, value: float):
        """
        Convert value from base unit to this unit
        :param value: numerical valve
        :return: converted valve
        """
        return (value - self.offset) / self.factor

    @property
    def symbol_quick_style(self):
        """
        The default style, quick & easy to typing

        Quick Style Convention:

        * No space separator
        * Power:    x ** y -> xy
        * Multiply: x * y  -> x-y
        * Parentheses will be omitted:  x / (y * z) -> x/y-z

        Examples:

            m ** 2 -> m2
            m * s -> m-s
            kJ / (C * kg) -> kJ/C-kg

        :return: quick style symbol in str
        """
        if self._symbol:
            return multi_replace(self._symbol, {
                '**': '',
                '*': '-',
                '(': '',
                ')': '',
            })

        return self._symbol

    @property
    def symbol_python_style(self):
        """
        Defined Style shows formula
        :return: defined style symbol in str
        """
        return self._symbol

    @property
    def symbol(self):
        return self.symbol_quick_style

    @property
    def factor(self):
        if callable(self._factor):
            return self._factor()

        return self._factor

    @property
    def offset(self):
        if callable(self._offset):
            return self._offset()

        return self._offset

    @property
    def aliases(self) -> list[str]:
        return self._aliases

    @aliases.setter
    def aliases(self, alist: Iterable[str]):
        self._aliases = list(set(alist).union([self.symbol]))

    def __repr__(self):
        return f"<Unit('{self}')>"

    def __str__(self):
        return self.symbol

    def __format__(self, format_spec=''):
        if format_spec == '':
            return self.symbol
        if format_spec == 'q':
            return self.symbol_quick_style
        if format_spec == 'p':
            return self.symbol_python_style

        raise ValueError('Invalid format specifier')

    def __mul__(self, other):
        # only for factor definition
        if isinstance(other, Unit):
            factor = self.factor * other.factor
            symbol = f"{self.symbol_python_style}*{other.symbol_python_style}"
            return Unit(symbol, factor=factor)

        if isinstance(other, (int, float)):
            factor = self.factor * other
            return Unit('dummy', factor=factor)

        return NotImplemented

    def __rmul__(self, other):
        factor = other * self.factor
        return Unit('dummy', factor=factor)

    def __truediv__(self, other):
        if isinstance(other, Unit):
            symbol = f"{self.symbol_python_style}/{other.symbol_python_style}"
            factor = self.factor / other.factor
            return Unit(symbol, factor=factor)

        if isinstance(other, (int, float)):
            factor = self.factor / other
            return Unit('dummy', factor=factor)

        return NotImplemented

    def __rtruediv__(self, other):
        if isinstance(other, (int, float)):
            factor = other / self.factor
            return Unit('dummy', factor=factor)

        return NotImplemented

    def __pow__(self, power, modulo=None):
        if isinstance(power, (int, float)):
            symbol = f"{self.symbol_python_style}**{power}"
            factor = self.factor ** power
            return Unit(symbol, factor=factor)

        return NotImplemented


class BaseUnit(Unit):
    """
    A class used to represent Base Unit.

    Creation:
        base_unit= BaseUnit(name)
        return a Unit instance with .is_base = True
    """

    def __init__(self, symbol: str):
        super().__init__(symbol)


# basic unit
# length, m
meter = BaseUnit('m')
kilometer = Unit('km', defined_by=1e3 * meter)
decimeter = Unit('dm', defined_by=1e-1 * meter)
centimeter = Unit('cm', defined_by=1e-2 * meter)
millimeter = Unit('mm', defined_by=1e-3 * meter)
micrometer = Unit('um', defined_by=1e-6 * meter)
foot = Unit('ft', factor=3.048e-1)
inch = Unit('in', factor=2.54e-2)

# area, m2
square_meter = BaseUnit('m**2')
square_kilometer = Unit('km**2', defined_by=kilometer**2)
square_decimeter = Unit('dm**2', defined_by=decimeter**2)
square_centimeter = Unit('cm**2', defined_by=centimeter**2)
square_millimeter = Unit('mm**2', defined_by=millimeter**2)
square_micrometer = Unit('um**2', defined_by=micrometer**2)
square_foot = Unit('ft**2', defined_by=foot**2)
square_inch = Unit('in**2', defined_by=inch**2)

# volume, m3
cubic_meter = BaseUnit('m**3')
cubic_centimeter = Unit('cm**3', defined_by=centimeter**3)
cubic_millimeter = Unit('mm**3', defined_by=millimeter**3)
liter = Unit('L', defined_by=decimeter**3)
milliliter = Unit('mL', defined_by=centimeter**3)
cubic_foot = Unit('ft**3', defined_by=foot**3)
cubic_inch = Unit('in**3', defined_by=inch**3)
# US_gallon
gallon = Unit('gal', defined_by=231 * cubic_inch)
barrel = Unit('bbl', defined_by=42 * gallon)

# time, s
second = BaseUnit('s')
minute = Unit('min', defined_by=60 * second)
hour = Unit('hr', defined_by=60 * minute)
day = Unit('day', defined_by=24 * hour)
week = Unit('week', defined_by=7 * day)
year = Unit('yr', defined_by=365 * day)
month = Unit('mon', defined_by=year / 12)

# velocity, m/s
meter_per_second = BaseUnit('m/s')
meter_per_minute = Unit('m/min', defined_by=meter / minute)
meter_per_hour = Unit('m/hr', defined_by=meter / hour)
kilometer_per_hour = Unit('km/hr', defined_by=kilometer / hour)
centimeter_per_second = Unit('cm/s', defined_by=centimeter / second)
foot_per_second = Unit('ft/s', defined_by=foot / second)
foot_per_minute = Unit('ft/min', defined_by=foot / minute)
foot_per_hour = Unit('ft/hr', defined_by=foot / hour)

# temperature base unit
celsius = BaseUnit('C')
kelvin = Unit('K', offset=-273.15)
rankine = Unit('R', factor=5 / 9, offset=-273.15)
fahrenheit = Unit('F', factor=5 / 9, offset=-32 * 5 / 9)

# mass, kg
kilogram = BaseUnit('kg')
gram = Unit('g', defined_by=1e-3 * kilogram)
tonne = Unit('t', defined_by=1e3 * kilogram)
pound = Unit('lb', defined_by=0.45359237 * kilogram)

# force, N
newton = BaseUnit('N')
kilogram_meter_per_second_squared = Unit('kg*m/s**2', defined_by=newton)
kilo_newton = Unit('kN', defined_by=1e3 * newton)
dyne = Unit('dyn', defined_by=1e-5 * newton)
kilogram_force = Unit('kgf', defined_by=constant.G * kilogram)
tonne_force = Unit('tonf', defined_by=constant.G * tonne)
pound_force = Unit('lbf', defined_by=constant.G * pound)

# substance, kmol
kilomole = BaseUnit('kmol')
mole = Unit('mol', defined_by=1e-3 * kilomole)
normal_cubic_meter = Unit('Nm**3', factor=1 / 22.414)
# @20 degC
T_60F = kelvin.from_base_unit(fahrenheit.to_base_unit(60))
T_0C = kelvin.from_base_unit(0)
T_20C = kelvin.from_base_unit(20)
standard_cubic_meter = Unit('Sm**3',
                            factor=lambda: normal_cubic_meter.factor * T_0C / (T_0C + get_standard_temperature()))
standard_cubic_meter_20C = Unit('Sm**3_20C', defined_by=normal_cubic_meter * T_0C / T_20C)
standard_cubic_meter_60F = Unit('Sm**3_60F', defined_by=normal_cubic_meter * T_0C / T_60F)
# scf is @60 degF
standard_cubic_foot = Unit('SCF', defined_by=normal_cubic_meter * cubic_foot * T_0C / T_60F)
kilo_standard_cubic_foot = Unit('MSCF', defined_by=1e3 * standard_cubic_foot)
million_standard_cubic_foot = Unit('MMSCF', defined_by=1e6 * standard_cubic_foot)

# energy, kJ
kilojoule = BaseUnit('kJ')
joule = Unit('J', defined_by=1e-3 * kilojoule)
megajoule = Unit('MJ', defined_by=1e6 * joule)
gigajoule = Unit('GJ', defined_by=1e9 * joule)
kilowatt_hour = Unit('kW*h', defined_by=kilojoule * hour)
kilowatt_year = Unit('kW*yr', defined_by=kilojoule * year)
calorie = Unit('cal', factor=4.184e-3)
kilocalorie = Unit('kcal', defined_by=1e3 * calorie)
megacalorie = Unit('Mcal', defined_by=1e6 * calorie)
gigacalorie = Unit('Gcal', defined_by=1e9 * calorie)
million_kilocalorie = Unit('MMkcal', defined_by=1e6 * kilocalorie)
british_thermal_unit = Unit('Btu', factor=1.055056)
million_british_thermal_unit = Unit('MMBtu', defined_by=1e6 * british_thermal_unit)
pound_force_foot = Unit('lbf*ft', defined_by=1e-3 * pound_force * foot)

# delta temperature
delta_celsius = BaseUnit('C')
delta_kelvin = Unit('K', factor=1)
delta_rankine = Unit('R', factor=5 / 9)
delta_fahrenheit = Unit('F', factor=5 / 9)

# pressure base unit
pascal = BaseUnit('Pa')
kilopascal = Unit('kPa', defined_by=1e3 * pascal)
megapascal = Unit('MPa', defined_by=1e6 * pascal)
bar = Unit('bar', defined_by=1e5 * pascal)
millibar = Unit('mbar', defined_by=1e-3 * bar)
atm = Unit('atm', factor=constant.ATM)
kg_force_per_square_centimeter = Unit('kgf/cm**2', defined_by=kilogram_force / square_centimeter)
psi = Unit('psi', defined_by=pound_force / square_inch)
pound_force_per_square_foot = Unit('lbf/ft**2', defined_by=pound_force / square_foot)
torr = Unit('torr', defined_by=atm / 760)
mm_Hg = Unit('mmHg_0C', defined_by=torr)
inch_Hg = Unit('inHg_32F', factor=1e3 * 3.386389)
inch_Hg_60F = Unit('inHg_60F', factor=1e3 * 3.37685)
kilopascal_gauge = Unit('kPag', factor=kilopascal.factor, offset=get_local_atmospheric_pressure)
megapascal_gauge = Unit('MPag', factor=megapascal.factor, offset=get_local_atmospheric_pressure)
bar_gauge = Unit('barg', factor=bar.factor, offset=get_local_atmospheric_pressure)
millibar_gauge = Unit('mbarg', factor=millibar.factor, offset=get_local_atmospheric_pressure)
kg_force_per_square_centimeter_gauge = Unit('kgf/cm**2_g', factor=kg_force_per_square_centimeter.factor,
                                            offset=get_local_atmospheric_pressure)
psi_gauge = Unit('psig', factor=psi.factor, offset=get_local_atmospheric_pressure)
pound_force_per_square_foot_gauge = Unit('lbf/ft**2_g', factor=pound_force_per_square_foot.factor,
                                         offset=get_local_atmospheric_pressure)
torr_gauge = Unit('torr_g', factor=torr.factor, offset=get_local_atmospheric_pressure)
mm_Hg_gauge = Unit('mmHg_0C_g', factor=mm_Hg.factor, offset=get_local_atmospheric_pressure)
inch_Hg_gauge = Unit('inHg_32F_g', factor=inch_Hg.factor, offset=get_local_atmospheric_pressure)
inch_Hg_60F_gauge = Unit('inHg_60F_g', factor=inch_Hg_60F.factor, offset=get_local_atmospheric_pressure)

# molar flow, base: kmol/s
kilomole_per_second = BaseUnit('kmol/s')
kilomole_per_hour = Unit('kmol/h', defined_by=kilomole / hour)
kilomole_per_minute = Unit('kmol/min', defined_by=kilomole / minute)
normal_cubic_meter_per_hour = Unit('Nm**3/h', defined_by=normal_cubic_meter / hour)
normal_cubic_meter_per_day = Unit('Nm**3/d', defined_by=normal_cubic_meter / day)
# standard_cubic_meter_per_hour = Unit('Sm**3/h', defined_by=standard_cubic_meter / hour)
standard_cubic_meter_per_hour = Unit(
    'Sm**3/h',
    factor=lambda: normal_cubic_meter.factor * T_0C / (T_0C + get_standard_temperature()) / hour.factor)
standard_cubic_meter_20C_per_hour = Unit('Sm**3_20C/h', defined_by=standard_cubic_meter_20C / hour)
standard_cubic_meter_60F_per_hour = Unit('Sm**3_60F/h', defined_by=standard_cubic_meter_60F / hour)
# standard_cubic_meter_per_day = Unit('Sm**3/d', defined_by=standard_cubic_meter / day)
standard_cubic_meter_per_day = Unit(
    'Sm**3/d',
    factor=lambda: normal_cubic_meter.factor * T_0C / (T_0C + get_standard_temperature()) / day.factor)
standard_cubic_meter_20C_per_day = Unit('Sm**3_20C/d', defined_by=standard_cubic_meter_20C / day)
standard_cubic_meter_60F_per_day = Unit('Sm**3_60F/d', defined_by=standard_cubic_meter_60F / day)
mole_per_hour = Unit('mol/h', defined_by=mole / hour)
mole_per_minute = Unit('mol/min', defined_by=mole / minute)
mole_per_second = Unit('mol/s', defined_by=mole)
standard_cubic_foot_per_day = Unit('SCFD', defined_by=standard_cubic_foot / day)
kilo_standard_cubic_foot_per_hour = Unit('MSCFH', defined_by=kilo_standard_cubic_foot / hour)
kilo_standard_cubic_foot_per_day = Unit('MSCFD', defined_by=kilo_standard_cubic_foot / day)
million_standard_cubic_foot_per_hour = Unit('MMSCFH', defined_by=million_standard_cubic_foot / hour)
million_standard_cubic_foot_per_day = Unit('MMSCFD', defined_by=million_standard_cubic_foot / day)

# mass flow, base: kg/s
kilogram_per_second = BaseUnit('kg/s')
kilogram_per_hour = Unit('kg/h', defined_by=kilogram / hour)
kilogram_per_minute = Unit('kg/min', defined_by=kilogram / minute)
kilogram_per_day = Unit('kg/d', defined_by=kilogram / day)
tonne_per_day = Unit('t/d', defined_by=tonne / day)
tonne_per_hour = Unit('t/h', defined_by=tonne / hour)
tonne_per_year = Unit('t/yr', defined_by=tonne / year)
gram_per_hour = Unit('g/h', defined_by=gram / hour)
gram_per_minute = Unit('g/min', defined_by=gram / minute)
gram_per_second = Unit('g/s', defined_by=gram / second)
pound_per_hour = Unit('lb/h', defined_by=pound / hour)
kilo_pound_per_hour = Unit('klb/h', defined_by=1e3 * pound / hour)
pound_per_day = Unit('lb/d', defined_by=pound / day)
kilo_pound_per_day = Unit('klb/d', defined_by=1e3 * pound / day)
million_pound_per_day = Unit('MMlb/d', defined_by=1e6 * pound / day)

# volume flow, base: m3/s
cubic_meter_per_second = BaseUnit('m**3/s')
cubic_meter_per_hour = Unit('m**3/h', defined_by=cubic_meter / hour)
cubic_meter_per_minute = Unit('m**3/min', defined_by=cubic_meter / minute)
cubic_meter_per_day = Unit('m**3/d', defined_by=cubic_meter / day)
liter_per_hour = Unit('L/h', defined_by=liter / hour)
liter_per_day = Unit('L/d', defined_by=liter / day)
liter_per_minute = Unit('L/min', defined_by=liter / minute)
liter_per_second = Unit('L/s', defined_by=liter / second)
milliliter_per_hour = Unit('mL/h', defined_by=milliliter / hour)
milliliter_per_minute = Unit('mL/min', defined_by=milliliter / minute)
milliliter_per_second = Unit('mL/s', defined_by=milliliter / second)
barrel_per_day = Unit('bbl/d', defined_by=barrel / day)
barrel_per_hour = Unit('bbl/h', defined_by=barrel / hour)
million_gallon_per_day = Unit('MMgal/d', defined_by=1e6 * gallon / day)
US_gallon_per_minute = Unit('USGPM', defined_by=gallon / minute)
US_gallon_per_hour = Unit('USGPH', defined_by=gallon / hour)
cubic_foot_per_hour = Unit('ft**3/h', defined_by=cubic_foot / hour)
cubic_foot_per_day = Unit('ft**3/d', defined_by=cubic_foot / day)

# Energy 'kJ/s'
kilojoule_per_second = BaseUnit('kJ/s')
kilojoule_per_hour = Unit('kJ/h', defined_by=kilojoule / hour)
kilojoule_per_minute = Unit('kJ/min', defined_by=kilojoule / minute)
megajoule_per_hour = Unit('MJ/h', defined_by=megajoule / hour)
gigajoule_per_hour = Unit('GJ/h', defined_by=gigajoule / hour)
kilowatt = Unit('kW', defined_by=kilojoule / second)
megawatt = Unit('MW', defined_by=1e3 * kilowatt)
kilocalorie_per_hour = Unit('kcal/h', defined_by=kilocalorie / hour)
kilocalorie_per_minute = Unit('kcal/min', defined_by=kilocalorie / minute)
kilocalorie_per_second = Unit('kcal/s', defined_by=kilocalorie / second)
million_kilocalorie_per_hour = Unit('MMkcal/h', defined_by=million_kilocalorie / hour)
calorie_per_hour = Unit('cal/h', defined_by=calorie / hour)
calorie_per_minute = Unit('cal/min', defined_by=calorie / minute)
calorie_per_second = Unit('cal/s', defined_by=calorie / second)
Btu_per_hour = Unit('Btu/h', defined_by=british_thermal_unit / hour)
million_Btu_per_hour = Unit('MMBtu/h', defined_by=million_british_thermal_unit / hour)
million_Btu_per_day = Unit('MMBtu/d', defined_by=million_british_thermal_unit / day)
horse_power = Unit('hp', defined_by=0.745699 * kilowatt)

# molar density, 'kmol/m3
kilomole_per_cubic_meter = BaseUnit('kmol/m**3')
mole_per_liter = Unit('mol/L', defined_by=mole / liter)
mole_per_cubic_centimeter = Unit('mol/cm**3', defined_by=mole / cubic_centimeter)
mole_per_milliliter = Unit('mol/mL', defined_by=mole / milliliter)

# heat capacity, entropy, 'kJ/kmol-C'
kilojoule_per_mole_celsius = Unit('kJ/(mol*C)', defined_by=kilojoule / (mole * delta_celsius))
kilojoule_per_mole_kelvin = Unit('kJ/(mol*K)', defined_by=kilojoule / (mole * delta_kelvin))
kilojoule_per_kilomole_celsius = BaseUnit('kJ/(kmol*C)')
kilojoule_per_kilomole_kelvin = Unit('kJ/(kmol*K)', defined_by=kilojoule / (kilomole * delta_kelvin))
joule_per_mole_celsius = Unit('J/(mol*C)', defined_by=joule / (mole * delta_celsius))
joule_per_mole_kelvin = Unit('J/(mol*K)', defined_by=joule / (mole * delta_kelvin))
joule_per_kilomole_celsius = Unit('J/(kmol*C)', defined_by=joule / (kilomole * delta_celsius))
joule_per_kilomole_kelvin = Unit('J/(kmol*K)', defined_by=joule / (kilomole * delta_kelvin))
kilocalorie_per_mole_celsius = Unit('kcal/(mol*C)', defined_by=kilocalorie / (mole * delta_celsius))
kilocalorie_per_mole_kelvin = Unit('kcal/(mol*K)', defined_by=kilocalorie / (mole * delta_kelvin))
kilocalorie_per_kilomole_celsius = Unit('kcal/(kmol*C)', defined_by=kilocalorie / (kilomole * delta_celsius))
kilocalorie_per_kilomole_kelvin = Unit('kcal/(kmol*K)', defined_by=kilocalorie / (kilomole * delta_kelvin))
calorie_per_mole_celsius = Unit('cal/(mol*C)', defined_by=calorie / (mole * delta_celsius))
calorie_per_mole_kelvin = Unit('cal/(mol*K)', defined_by=calorie / (mole * delta_kelvin))
calorie_per_kilomole_celsius = Unit('cal/(kmol*C)', defined_by=calorie / (kilomole * delta_celsius))
calorie_per_kilomole_kelvin = Unit('cal/(kmol*K)', defined_by=calorie / (kilomole * delta_kelvin))

# thermal conductivity, W/m-K
watt_per_meter_kelvin = BaseUnit('W/(m*K)')
Btu_per_hour_foot_fahrenheit = Unit('Btu/(h*ft*F)', defined_by=1e3 * british_thermal_unit / (
        hour * foot * delta_fahrenheit))
kilocalorie_per_meter_hour_celsius = Unit('kcal/(m*h*C)', defined_by=1e3 * kilocalorie / hour)
calorie_per_centimeter_second_celsius = Unit('cal/(cm*s*C)', defined_by=1e3 * calorie / centimeter)

# viscosity, cP
centipoise = BaseUnit('cP')
millipoise = Unit('mP', factor=0.1)
micropoise = Unit('microP', defined_by=1e-3 * millipoise)
poise = Unit('P', factor=100)
pascal_second = Unit('Pa-s', factor=1000)
pound_force_second_per_square_foot = Unit('lbf*s/ft**2', defined_by=1e3 * pound_force / square_foot)
pound_mass_per_foot_second = Unit('lbm/(ft*s)', defined_by=1e3 * pound / foot)
pound_mass_per_foot_hour = Unit('lbm/(ft*h)', defined_by=1e3 * pound / (foot * hour))

# surface tension, dyne/cm
dyne_per_centimeter = BaseUnit('dyne/cm')
dyn_per_centimeter = Unit('dyn/cm', factor=1)
pound_force_per_foot = Unit('lbf/ft', defined_by=1e3 * pound_force / foot)

# mass capacity, kJ/kg-C
kilojoule_per_gram_celsius = Unit('kJ/(g*C)', defined_by=kilojoule / (gram * delta_celsius))
kilojoule_per_gram_kelvin = Unit('kJ/(g*K)', defined_by=kilojoule / (gram * delta_kelvin))
kilojoule_per_kilogram_celsius = BaseUnit('kJ/(kg*C)')
kilojoule_per_kilogram_kelvin = Unit('kJ/(kg*K)', defined_by=kilojoule / (kilogram * delta_kelvin))
joule_per_gram_celsius = Unit('J/(g*C)', defined_by=joule / (gram * delta_celsius))
joule_per_gram_kelvin = Unit('J/(g*K)', defined_by=joule / (gram * delta_kelvin))
joule_per_kilogram_celsius = Unit('J/(kg*C)', defined_by=joule / (kilogram * delta_celsius))
joule_per_kilogram_kelvin = Unit('J/(kg*K)', defined_by=joule / (kilogram * delta_kelvin))
kilocalorie_per_gram_celsius = Unit('kcal/(g*C)', defined_by=kilocalorie / (gram * delta_celsius))
kilocalorie_per_gram_kelvin = Unit('kcal/(g*K)', defined_by=kilocalorie / (gram * delta_kelvin))
kilocalorie_per_kilogram_celsius = Unit('kcal/(kg*C)', defined_by=kilocalorie / (kilogram * delta_celsius))
kilocalorie_per_kilogram_kelvin = Unit('kcal/(kg*K)', defined_by=kilocalorie / (kilogram * delta_kelvin))
calorie_per_gram_celsius = Unit('cal/(g*C)', defined_by=calorie / (gram * delta_celsius))
calorie_per_gram_kelvin = Unit('cal/(g*K)', defined_by=calorie / (gram * delta_kelvin))
calorie_per_kilogram_celsius = Unit('cal/(kg*C)', defined_by=calorie / (kilogram * delta_celsius))
calorie_per_kilogram_kelvin = Unit('cal/(kg*K)', defined_by=calorie / (kilogram * delta_kelvin))

# mass density, kg/m3
kilogram_per_cubic_meter = BaseUnit('kg/m**3')
gram_per_liter = Unit('g/L', defined_by=gram / liter)
gram_per_cubic_centimeter = Unit('g/cm**3', defined_by=gram / cubic_centimeter)
gram_per_milliliter = Unit('g/mL', defined_by=gram / milliliter)

# molar_enthalpy
kilojoule_per_mole = Unit('kJ/mol', defined_by=kilojoule / mole)
kilojoule_per_kilomole = BaseUnit('kJ/kmol')
joule_per_mole = Unit('J/mol', defined_by=joule / mole)
joule_per_kilomole = Unit('J/kmol', defined_by=joule / kilomole)
megajoule_per_kilomole = Unit('MJ/kmol', defined_by=megajoule / kilomole)
kilocalorie_per_mole = Unit('kcal/mol', defined_by=kilocalorie / mole)
kilocalorie_per_kilomole = Unit('kcal/kmol', defined_by=kilocalorie / kilomole)
calorie_per_mole = Unit('cal/mol', defined_by=calorie / mole)
calorie_per_kilomole = Unit('cal/kmol', defined_by=calorie / kilomole)

# molar_volume
cubic_meter_per_mole = Unit('m**3/mol', defined_by=cubic_meter / mole)
cubic_meter_per_kilomole = BaseUnit('m**3/kmol')
liter_per_mole = Unit('L/mol', defined_by=liter / mole)
cubic_centimeter_per_mole = Unit('cm**3/mol', defined_by=cubic_centimeter / mole)
milliliter_per_mole = Unit('mL/mol', defined_by=milliliter / mole)

# mass_heat
kilojoule_per_gram = Unit('kJ/g', defined_by=kilojoule / gram)
kilojoule_per_kilogram = BaseUnit('kJ/kg')
joule_per_gram = Unit('J/g', defined_by=joule / gram)
joule_per_kilogram = Unit('J/kg', defined_by=joule / kilogram)
megajoule_per_kilogram = Unit('MJ/kg', defined_by=megajoule / kilogram)
kilocalorie_per_gram = Unit('kcal/g', defined_by=kilocalorie / gram)
kilocalorie_per_kilogram = Unit('kcal/kg', defined_by=kilocalorie / kilogram)
calorie_per_gram = Unit('cal/g', defined_by=calorie / gram)
calorie_per_kilogram = Unit('cal/kg', defined_by=calorie / kilogram)
Btu_per_pound = Unit('Btu/lb', defined_by=british_thermal_unit / pound)

# fraction
dimensionless = BaseUnit('')
percent = Unit('%', factor=1e-2)
parts_per_million = Unit('ppm', factor=1e-6)

# molecular_weight
gram_per_mole = Unit('g/mol', factor=1)
kilogram_per_kilomole = BaseUnit('kg/kmol')
kilogram_per_mole = Unit('kg/mol', factor=1e3)
