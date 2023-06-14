import numbers
import re
from typing import Union, Callable

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

    Example: kilometer = Unit('km', factor=1e3)

    Which meter is base unit

    Property
    ----------
    symbol: str
        the quick style name(symbol) of the unit.

    factor: float
        factor value

    offset: float
        offset value
    """

    def __init__(self, symbol: str, factor: Union[float, Callable] = 1, offset: Union[float, Callable] = 0):
        self._symbol = symbol.replace(' ', '')
        self._factor = factor
        self._offset = offset

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
    def quick_style(self):
        """
        The default style, used for indexing

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
    def defined_style(self):
        """
        Defined Style shows formula
        :return: defined style symbol in str
        """
        if self._symbol:
            return re.sub(r'(\*{2}|\*|/)', r' \g<0> ', self._symbol)

        return self._symbol

    @property
    def symbol(self):
        return self.quick_style

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

    def __repr__(self):
        return f"<Unit('{self}')>"

    def __format__(self, format_spec=''):
        if format_spec.startswith('q'):
            return self.quick_style
        if format_spec.startswith('d'):
            return self.defined_style

        return self.symbol


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
kilometer = Unit('km', factor=1e3)
decimeter = Unit('dm', factor=1e-1)
centimeter = Unit('cm', factor=1e-2)
millimeter = Unit('mm', factor=1e-3)
micrometer = Unit('um', factor=1e-6)
foot = Unit('ft', factor=3.048e-1)
inch = Unit('in', factor=2.54e-2)

# area, m2
square_meter = BaseUnit('m**2')
square_kilometer = Unit('km**2', factor=kilometer.factor ** 2)
square_decimeter = Unit('dm**2', factor=decimeter.factor ** 2)
square_centimeter = Unit('cm**2', factor=centimeter.factor ** 2)
square_millimeter = Unit('mm**2', factor=millimeter.factor ** 2)
square_micrometer = Unit('um**2', factor=micrometer.factor ** 2)
square_foot = Unit('ft**2', factor=foot.factor ** 2)
square_inch = Unit('in**2', factor=inch.factor ** 2)

# volume, m3
cubic_meter = BaseUnit('m**3')
cubic_centimeter = Unit('cm**3', factor=centimeter.factor ** 3)
cubic_millimeter = Unit('mm**3', factor=millimeter.factor ** 3)
liter = Unit('L', factor=decimeter.factor ** 3)
milliliter = Unit('mL', factor=centimeter.factor ** 3)
cubic_foot = Unit('ft**3', factor=foot.factor ** 3)
cubic_inch = Unit('in**3', factor=inch.factor ** 3)
# US_gallon
gallon = Unit('gal', factor=231 * cubic_inch.factor)
barrel = Unit('bbl', factor=42 * gallon.factor)

# time, s
second = BaseUnit('s')
minute = Unit('min', factor=60)
hour = Unit('hr', factor=60 * minute.factor)
day = Unit('day', factor=24 * hour.factor)
week = Unit('week', factor=7 * day.factor)
# year = Unit('yr', factor=365.25 * day.factor)
year = Unit('yr', factor=8760 * hour.factor)
month = Unit('mon', factor=year.factor / 12)

# velocity, m/s
meter_per_second = BaseUnit('m/s')
meter_per_minute = Unit('m/min', factor=1 / minute.factor)
meter_per_hour = Unit('m/hr', factor=1 / hour.factor)
kilometer_per_hour = Unit('km/hr', factor=kilometer.factor / hour.factor)
centimeter_per_second = Unit('cm/s', factor=centimeter.factor / second.factor)
foot_per_second = Unit('ft/s', factor=foot.factor / second.factor)
foot_per_minute = Unit('ft/min', factor=foot.factor / minute.factor)
foot_per_hour = Unit('ft/hr', factor=foot.factor / hour.factor)

# temperature base unit
celsius = BaseUnit('C')
kelvin = Unit('K', offset=-273.15)
rankine = Unit('R', factor=5 / 9, offset=-273.15)
fahrenheit = Unit('F', factor=5 / 9, offset=-32 * 5 / 9)

# mass, kg
kilogram = BaseUnit('kg')
gram = Unit('g', factor=1e-3)
tonne = Unit('t', factor=1e3)
pound = Unit('lb', factor=0.45359237)

# force, N
newton = BaseUnit('N')
kilogram_meter_per_second_squared = Unit('kg*m/s**2', factor=1)
kilo_newton = Unit('kN', factor=1e3)
dyne = Unit('dyn', factor=1e-5)
kilogram_force = Unit('kgf', factor=constant.G)
tonne_force = Unit('tonf', factor=tonne.factor * constant.G)
pound_force = Unit('lbf', factor=pound.factor * constant.G)

# substance, kmol
kilomole = BaseUnit('kmol')
mole = Unit('mol', factor=1e-3)
normal_cubic_meter = Unit('Nm**3', factor=1 / 22.414)
# @20 degC
standard_cubic_meter = Unit('Sm**3',
                            factor=lambda: normal_cubic_meter.factor * 273.15 / (273.15 + get_standard_temperature()))
# scf is @60 degF, so some math need to be done
T_60F_inK = kelvin.from_base_unit(fahrenheit.to_base_unit(60))
T_0C_inK = kelvin.from_base_unit(0)
standard_cubic_foot = Unit('SCF', factor=normal_cubic_meter.factor * cubic_foot.factor * T_0C_inK / T_60F_inK)
kilo_standard_cubic_foot = Unit('MSCF', factor=1e3 * standard_cubic_foot.factor)
million_standard_cubic_foot = Unit('MMSCF', factor=1e6 * standard_cubic_foot.factor)

# energy, kJ
kilojoule = BaseUnit('kJ')
joule = Unit('J', factor=1e-3)
megajoule = Unit('MJ', factor=1e3)
gigajoule = Unit('GJ', factor=1e6)
kilowatt_hour = Unit('kW*h', factor=hour.factor)
kilowatt_year = Unit('kW*yr', factor=year.factor)
calorie = Unit('cal', factor=4.184e-3)
kilocalorie = Unit('kcal', factor=1e3 * calorie.factor)
megacalorie = Unit('Mcal', factor=1e6 * calorie.factor)
gigacalorie = Unit('Gcal', factor=1e9 * calorie.factor)
million_kilocalorie = Unit('MMkcal', factor=1e6 * kilocalorie.factor)
british_thermal_unit = Unit('Btu', factor=1.055056)
million_british_thermal_unit = Unit('MMBtu', factor=1e6 * british_thermal_unit.factor)
pound_force_foot = Unit('lbf*ft', factor=1e-3 * pound_force.factor * foot.factor)

# delta temperature
delta_celsius = BaseUnit('C')
delta_kelvin = Unit('K', factor=1)
delta_rankine = Unit('R', factor=5 / 9)
delta_fahrenheit = Unit('F', factor=5 / 9)

# pressure base unit
kilopascal = BaseUnit('kPa')
megapascal = Unit('MPa', factor=1e3)
bar = Unit('bar', factor=1e2)
millibar = Unit('mbar', factor=0.1)
pascal = Unit('Pa', factor=1e-3)
atm = Unit('atm', factor=constant.ATM)
kg_force_per_square_centimeter = Unit('kgf/cm**2', factor=1e-3 * kilogram_force.factor / square_centimeter.factor)
# psi = Unit('psi', factor=6.894757)
psi = Unit('psi', factor=1e-3 * pound_force.factor / square_inch.factor)
pound_force_per_square_foot = Unit('lbf/ft**2', factor=1e-3 * pound_force.factor / square_foot.factor)
torr = Unit('torr', factor=101.325 / 760)
mm_Hg = Unit('mmHg_0C', factor=torr.factor)
inch_Hg = Unit('inHg_32F', factor=3.386389)
inch_Hg_60F = Unit('inHg_60F', factor=3.37685)
kilopascal_gauge = Unit('kPag', offset=get_local_atmospheric_pressure)
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
kilomole_per_hour = Unit('kmol/h', factor=1 / hour.factor)
kilomole_per_minute = Unit('kmol/min', factor=1 / minute.factor)
normal_cubic_meter_per_hour = Unit('Nm**3/h', factor=normal_cubic_meter.factor / hour.factor)
normal_cubic_meter_per_day = Unit('Nm**3/d', factor=normal_cubic_meter.factor / day.factor)
standard_cubic_meter_per_hour = Unit('Sm**3/h', factor=standard_cubic_meter.factor / hour.factor)
standard_cubic_meter_per_day = Unit('Sm**3/d', factor=standard_cubic_meter.factor / day.factor)
mole_per_hour = Unit('mol/h', factor=mole.factor / hour.factor)
mole_per_minute = Unit('mol/min', factor=mole.factor / minute.factor)
mole_per_second = Unit('mol/s', factor=mole.factor)
standard_cubic_foot_per_day = Unit('SCFD', factor=standard_cubic_foot.factor / day.factor)
kilo_standard_cubic_foot_per_hour = Unit('MSCFH', factor=kilo_standard_cubic_foot.factor / hour.factor)
kilo_standard_cubic_foot_per_day = Unit('MSCFD', factor=kilo_standard_cubic_foot.factor / day.factor)
million_standard_cubic_foot_per_hour = Unit('MMSCFH', factor=million_standard_cubic_foot.factor / hour.factor)
million_standard_cubic_foot_per_day = Unit('MMSCFD', factor=million_standard_cubic_foot.factor / day.factor)

# mass flow, base: kg/s
kilogram_per_second = BaseUnit('kg/s')
kilogram_per_hour = Unit('kg/h', factor=1 / hour.factor)
kilogram_per_minute = Unit('kg/min', factor=1 / minute.factor)
kilogram_per_day = Unit('kg/d', factor=1 / day.factor)
tonne_per_day = Unit('t/d', factor=tonne.factor / day.factor)
tonne_per_hour = Unit('t/h', factor=tonne.factor / hour.factor)
tonne_per_year = Unit('t/yr', factor=tonne.factor / year.factor)
gram_per_hour = Unit('g/h', factor=gram.factor / hour.factor)
gram_per_minute = Unit('g/min', factor=gram.factor / minute.factor)
gram_per_second = Unit('g/s', factor=gram.factor)
pound_per_hour = Unit('lb/h', factor=pound.factor / hour.factor)
kilo_pound_per_hour = Unit('klb/h', factor=1e3 * pound.factor / hour.factor)
pound_per_day = Unit('lb/d', factor=pound.factor / day.factor)
kilo_pound_per_day = Unit('klb/d', factor=1e3 * pound.factor / day.factor)
million_pound_per_day = Unit('MMlb/d', factor=1e6 * pound.factor / day.factor)

# volume flow, base: m3/s
cubic_meter_per_second = BaseUnit('m**3/s')
cubic_meter_per_hour = Unit('m**3/h', factor=1 / hour.factor)
cubic_meter_per_minute = Unit('m**3/min', factor=1 / minute.factor)
cubic_meter_per_day = Unit('m**3/d', factor=1 / day.factor)
liter_per_hour = Unit('L/h', factor=liter.factor / hour.factor)
liter_per_day = Unit('L/d', factor=liter.factor / day.factor)
liter_per_minute = Unit('L/min', factor=liter.factor / minute.factor)
liter_per_second = Unit('L/s', factor=liter.factor)
milliliter_per_hour = Unit('mL/h', factor=milliliter.factor / hour.factor)
milliliter_per_minute = Unit('mL/min', factor=milliliter.factor / minute.factor)
milliliter_per_second = Unit('mL/s', factor=milliliter.factor)
barrel_per_day = Unit('bbl/d', factor=barrel.factor / day.factor)
barrel_per_hour = Unit('bbl/h', factor=barrel.factor / hour.factor)
million_gallon_per_day = Unit('MMgal/d', factor=1e6 * gallon.factor / day.factor)
US_gallon_per_minute = Unit('USGPM', factor=gallon.factor / minute.factor)
US_gallon_per_hour = Unit('USGPH', factor=gallon.factor / hour.factor)
cubic_foot_per_hour = Unit('ft**3/h', factor=cubic_foot.factor / hour.factor)
cubic_foot_per_day = Unit('ft**3/d', factor=cubic_foot.factor / day.factor)

# Energy 'kJ/s'
kilojoule_per_second = BaseUnit('kJ/s')
kilojoule_per_hour = Unit('kJ/h', factor=1 / hour.factor)
kilojoule_per_minute = Unit('kJ/min', factor=1 / minute.factor)
megajoule_per_hour = Unit('MJ/h', factor=megajoule.factor / hour.factor)
gigajoule_per_hour = Unit('GJ/h', factor=gigajoule.factor / hour.factor)
kilowatt = Unit('kW', factor=1)
megawatt = Unit('MW', factor=1e3)
kilocalorie_per_hour = Unit('kcal/h', factor=kilocalorie.factor / hour.factor)
kilocalorie_per_minute = Unit('kcal/min', factor=kilocalorie.factor / minute.factor)
kilocalorie_per_second = Unit('kcal/s', factor=kilocalorie.factor)
million_kilocalorie_per_hour = Unit('MMkcal/h', factor=million_kilocalorie.factor / hour.factor)
calorie_per_hour = Unit('cal/h', factor=calorie.factor / hour.factor)
calorie_per_minute = Unit('cal/min', factor=calorie.factor / minute.factor)
calorie_per_second = Unit('cal/s', factor=calorie.factor / second.factor)
Btu_per_hour = Unit('Btu/h', factor=british_thermal_unit.factor / hour.factor)
million_Btu_per_hour = Unit('MMBtu/h', factor=million_british_thermal_unit.factor / hour.factor)
million_Btu_per_day = Unit('MMBtu/d', factor=million_british_thermal_unit.factor / day.factor)
horse_power = Unit('hp', factor=0.745699)

# molar density, 'kmol/m3
kilomole_per_cubic_meter = BaseUnit('kmol/m**3')
mole_per_liter = Unit('mol/L', factor=mole.factor / liter.factor)
mole_per_cubic_centimeter = Unit('mol/cm**3', factor=mole.factor / cubic_centimeter.factor)
mole_per_milliliter = Unit('mol/mL', factor=mole.factor / milliliter.factor)

# heat capacity, entropy, 'kJ/kmol-C'
kilojoule_per_mole_celsius = Unit('kJ/(mol*C)', factor=1 / mole.factor)
kilojoule_per_mole_kelvin = Unit('kJ/(mol*K)', factor=1 / mole.factor)
kilojoule_per_kilomole_celsius = BaseUnit('kJ/(kmol*C)')
kilojoule_per_kilomole_kelvin = Unit('kJ/(kmol*K)', factor=1)
joule_per_mole_celsius = Unit('J/(mol*C)', factor=1)
joule_per_mole_kelvin = Unit('J/(mol*K)', factor=1)
joule_per_kilomole_celsius = Unit('J/(kmol*C)', factor=joule.factor / kilomole.factor)
joule_per_kilomole_kelvin = Unit('J/(kmol*K)', factor=joule.factor / kilomole.factor)
kilocalorie_per_mole_celsius = Unit('kcal/(mol*C)', factor=kilocalorie.factor / mole.factor)
kilocalorie_per_mole_kelvin = Unit('kcal/(mol*K)', factor=kilocalorie.factor / mole.factor)
kilocalorie_per_kilomole_celsius = Unit('kcal/(kmol*C)', factor=kilocalorie.factor)
kilocalorie_per_kilomole_kelvin = Unit('kcal/(kmol*K)', factor=kilocalorie.factor)
calorie_per_mole_celsius = Unit('cal/(mol*C)', factor=calorie.factor / mole.factor)
calorie_per_mole_kelvin = Unit('cal/(mol*K)', factor=calorie.factor / mole.factor)
calorie_per_kilomole_celsius = Unit('cal/(kmol*C)', factor=calorie.factor / kilomole.factor)
calorie_per_kilomole_kelvin = Unit('cal/(kmol*K)', factor=calorie.factor / kilomole.factor)

# thermal conductivity, W/m-K
watt_per_meter_kelvin = BaseUnit('W/(m*K)')
Btu_per_hour_foot_fahrenheit = Unit('Btu/(h*ft*F)', factor=1e3 * british_thermal_unit.factor / (
            hour.factor * foot.factor * delta_fahrenheit.factor))
kilocalorie_per_meter_hour_celsius = Unit('kcal/(m*h*C)', factor=1e3 * kilocalorie.factor / hour.factor)
calorie_per_centimeter_second_celsius = Unit('cal/(cm*s*C)', factor=1e3 * calorie.factor / centimeter.factor)

# viscosity, cP
centipoise = BaseUnit('cP')
millipoise = Unit('mP', factor=0.1)
micropoise = Unit('microP', factor=1e-3 * millipoise.factor)
poise = Unit('P', factor=100)
pascal_second = Unit('Pa-s', factor=1000)
pound_force_second_per_square_foot = Unit('lbf*s/ft**2', factor=1e3 * pound_force.factor / square_foot.factor)
pound_mass_per_foot_second = Unit('lbm/(ft*s)', factor=1e3 * pound.factor / foot.factor)
pound_mass_per_foot_hour = Unit('lbm/(ft*h)', factor=1e3 * pound.factor / (foot.factor * hour.factor))

# surface tension, dyne/cm
dyne_per_centimeter = BaseUnit('dyne/cm')
dyn_per_centimeter = Unit('dyn/cm', factor=1)
pound_force_per_foot = Unit('lbf/ft', factor=1e3 * pound_force.factor / foot.factor)

# mass capacity, kJ/kg-C
kilojoule_per_gram_celsius = Unit('kJ/(g*C)', factor=kilojoule.factor / gram.factor)
kilojoule_per_gram_kelvin = Unit('kJ/(g*K)', factor=kilojoule.factor / gram.factor)
kilojoule_per_kilogram_celsius = BaseUnit('kJ/(kg*C)')
kilojoule_per_kilogram_kelvin = Unit('kJ/(kg*K)', factor=1)
joule_per_gram_celsius = Unit('J/(g*C)', factor=1)
joule_per_gram_kelvin = Unit('J/(g*K)', factor=1)
joule_per_kilogram_celsius = Unit('J/(kg*C)', factor=joule.factor / kilogram.factor)
joule_per_kilogram_kelvin = Unit('J/(kg*K)', factor=joule.factor / kilogram.factor)
kilocalorie_per_gram_celsius = Unit('kcal/(g*C)', factor=kilocalorie.factor / gram.factor)
kilocalorie_per_gram_kelvin = Unit('kcal/(g*K)', factor=kilocalorie.factor / gram.factor)
kilocalorie_per_kilogram_celsius = Unit('kcal/(kg*C)', factor=kilocalorie.factor / kilogram.factor)
kilocalorie_per_kilogram_kelvin = Unit('kcal/(kg*K)', factor=kilocalorie.factor / kilogram.factor)
calorie_per_gram_celsius = Unit('cal/(g*C)', factor=calorie.factor / gram.factor)
calorie_per_gram_kelvin = Unit('cal/(g*K)', factor=calorie.factor / gram.factor)
calorie_per_kilogram_celsius = Unit('cal/(kg*C)', factor=calorie.factor / kilogram.factor)
calorie_per_kilogram_kelvin = Unit('cal/(kg*K)', factor=calorie.factor / kilogram.factor)

# mass density, kg/m3
kilogram_per_cubic_meter = BaseUnit('kg/m**3')
gram_per_liter = Unit('g/L', factor=gram.factor / liter.factor)
gram_per_cubic_centimeter = Unit('g/cm**3', factor=gram.factor / cubic_centimeter.factor)
gram_per_milliliter = Unit('g/mL', factor=gram.factor / milliliter.factor)

# molar_enthalpy
kilojoule_per_mole = Unit('kJ/mol', factor=1e3)
kilojoule_per_kilomole = BaseUnit('kJ/kmol')
joule_per_mole = Unit('J/mol', factor=1)
joule_per_kilomole = Unit('J/kmol', factor=1e-3)
megajoule_per_kilomole = Unit('MJ/kmol', factor=1e3)
kilocalorie_per_mole = Unit('kcal/mol', factor=kilocalorie.factor / mole.factor)
kilocalorie_per_kilomole = Unit('kcal/kmol', factor=kilocalorie.factor)
calorie_per_mole = Unit('cal/mol', factor=calorie.factor / mole.factor)
calorie_per_kilomole = Unit('cal/kmol', factor=calorie.factor / kilomole.factor)

# molar_volume
cubic_meter_per_mole = Unit('m**3/mol', factor=1 / mole.factor)
cubic_meter_per_kilomole = BaseUnit('m**3/kmol')
liter_per_mole = Unit('L/mol', factor=liter.factor / mole.factor)
cubic_centimeter_per_mole = Unit('cm**3/mol', factor=cubic_centimeter.factor / mole.factor)
milliliter_per_mole = Unit('mL/mol', factor=milliliter.factor / mole.factor)

# mass_heat
kilojoule_per_gram = Unit('kJ/g', factor=1e3)
kilojoule_per_kilogram = BaseUnit('kJ/kg')
joule_per_gram = Unit('J/g', factor=1)
joule_per_kilogram = Unit('J/kg', factor=1e-3)
megajoule_per_kilogram = Unit('MJ/kg', factor=1e3)
kilocalorie_per_gram = Unit('kcal/g', factor=kilocalorie.factor / gram.factor)
kilocalorie_per_kilogram = Unit('kcal/kg', factor=kilocalorie.factor)
calorie_per_gram = Unit('cal/g', factor=calorie.factor / gram.factor)
calorie_per_kilogram = Unit('cal/kg', factor=calorie.factor)
Btu_per_pound = Unit('Btu/lb', factor=british_thermal_unit.factor / pound.factor)

# fraction
dimensionless = BaseUnit('')
percent = Unit('%', factor=1e-2)
parts_per_million = Unit('ppm', factor=1e-6)

# molecular_weight
gram_per_mole = Unit('g/mol', factor=1)
kilogram_per_kilomole = BaseUnit('kg/kmol')
kilogram_per_mole = Unit('kg/mol', factor=1e3)
