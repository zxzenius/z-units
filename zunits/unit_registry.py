from __future__ import annotations
from typing import Iterable

from . import unit as u
from .unit import Unit, BaseUnit


class UnitRegistry:
    def __init__(self, units: Iterable[Unit], base_unit: Unit = None):
        self._base_unit = base_unit
        self._symbol_to_unit = {}
        if self._base_unit is None:
            for unit in units:
                self._symbol_to_unit[unit.symbol] = unit
                if isinstance(unit, BaseUnit):
                    self._base_unit = unit

        elif self._base_unit not in units:
            raise ValueError(f"Base unit {self._base_unit} is not in the list of units")

        if self._base_unit is None:
            raise ValueError("No base unit found")

        self._units = units

    @property
    def base_unit(self):
        return self._base_unit

    def get_unit(self, symbol: str):
        if unit := self._symbol_to_unit.get(symbol):
            return unit
        raise ValueError(f"Unit '{symbol}' not found")

    @property
    def units(self):
        return self._units

    @property
    def symbols(self):
        return list(self._symbol_to_unit.keys())


length = UnitRegistry(units=[
    u.meter,
    u.kilometer,
    u.decimeter,
    u.centimeter,
    u.millimeter,
    u.micrometer,
    u.foot,
    u.inch
])

area = UnitRegistry([
    u.square_meter,
    u.square_kilometer,
    u.square_decimeter,
    u.square_centimeter,
    u.square_millimeter,
    u.square_micrometer,
    u.square_foot,
    u.square_inch
])

volume = UnitRegistry(units=[
    u.cubic_meter,
    u.cubic_centimeter,
    u.cubic_millimeter,
    u.millimeter,
    u.liter,
    u.milliliter,
    u.cubic_foot,
    u.cubic_inch,
    u.gallon,
    u.barrel
])

time = UnitRegistry(units=[
    u.second,
    u.minute,
    u.hour,
    u.day,
    u.week,
    u.year,
    u.month
])

mass = UnitRegistry(units=[
    u.kilogram,
    u.gram,
    u.tonne,
    u.pound
])

force = UnitRegistry([
    u.newton,
    u.kilogram_meter_per_second_squared,
    u.kilo_newton,
    u.dyne,
    u.kilogram_force,
    u.tonne_force,
    u.pound_force,
])

substance = UnitRegistry(units=[
    u.kilomole,
    u.mole,
    u.normal_cubic_meter,
    u.standard_cubic_meter,
    u.standard_cubic_meter_20C,
    u.standard_cubic_meter_60F,
    u.standard_cubic_foot,
    u.kilo_standard_cubic_foot,
    u.million_standard_cubic_foot
])

energy = UnitRegistry(units=[
    u.kilojoule,
    u.joule,
    u.megajoule,
    u.gigajoule,
    u.kilowatt_hour,
    u.kilowatt_year,
    u.calorie,
    u.kilocalorie,
    u.megacalorie,
    u.gigacalorie,
    u.million_kilocalorie,
    u.british_thermal_unit,
    u.million_british_thermal_unit,
    u.pound_force_foot
])

velocity = UnitRegistry([
    u.meter_per_second,
    u.meter_per_minute,
    u.meter_per_hour,
    u.kilometer_per_hour,
    u.centimeter_per_second,
    u.foot_per_second,
    u.foot_per_minute,
    u.foot_per_hour
])

temperature = UnitRegistry(units=[
    u.celsius,
    u.kelvin,
    u.fahrenheit,
    u.rankine
])

delta_temperature = UnitRegistry([
    u.delta_celsius,
    u.delta_kelvin,
    u.delta_rankine,
    u.delta_fahrenheit
])

pressure = UnitRegistry(units=[
    u.kilopascal,
    u.megapascal,
    u.bar,
    u.millibar,
    u.pascal,
    u.atm,
    u.kg_force_per_square_centimeter,
    u.psi,
    u.pound_force_per_square_foot,
    u.torr,
    u.mm_Hg,
    u.inch_Hg,
    u.inch_Hg_60F,
    u.kilopascal_gauge,
    u.megapascal_gauge,
    u.bar_gauge,
    u.millibar_gauge,
    u.kg_force_per_square_centimeter_gauge,
    u.psi_gauge,
    u.pound_force_per_square_foot_gauge,
    u.torr_gauge,
    u.mm_Hg_gauge,
    u.inch_Hg_gauge,
    u.inch_Hg_60F_gauge
])

molar_flow = UnitRegistry(units=[
    u.kilomole_per_second,
    u.kilomole_per_hour,
    u.kilomole_per_minute,
    u.normal_cubic_meter_per_hour,
    u.normal_cubic_meter_per_day,
    u.standard_cubic_meter_per_hour,
    u.standard_cubic_meter_20C_per_hour,
    u.standard_cubic_meter_60F_per_hour,
    u.standard_cubic_meter_per_day,
    u.standard_cubic_meter_20C_per_day,
    u.standard_cubic_meter_60F_per_day,
    u.mole_per_hour,
    u.mole_per_minute,
    u.mole_per_second,
    u.standard_cubic_foot_per_day,
    u.kilo_standard_cubic_foot_per_hour,
    u.kilo_standard_cubic_foot_per_day,
    u.million_standard_cubic_foot_per_hour,
    u.million_standard_cubic_foot_per_day
])

mass_flow = UnitRegistry(units=[
    u.kilogram_per_hour,
    u.kilogram_per_minute,
    u.kilogram_per_second,
    u.kilogram_per_day,
    u.tonne_per_day,
    u.tonne_per_hour,
    u.tonne_per_year,
    u.gram_per_hour,
    u.gram_per_minute,
    u.gram_per_second,
    u.pound_per_hour,
    u.pound_per_day,
    u.kilo_pound_per_hour,
    u.kilo_pound_per_day,
    u.million_pound_per_day
])

volume_flow = UnitRegistry(units=[
    u.cubic_meter_per_hour,
    u.cubic_meter_per_minute,
    u.cubic_meter_per_second,
    u.cubic_meter_per_day,
    u.liter_per_hour,
    u.liter_per_day,
    u.liter_per_minute,
    u.liter_per_second,
    u.milliliter_per_hour,
    u.milliliter_per_minute,
    u.milliliter_per_second,
    u.barrel_per_day,
    u.barrel_per_hour,
    u.million_gallon_per_day,
    u.US_gallon_per_minute,
    u.US_gallon_per_hour,
    u.cubic_foot_per_hour,
    u.cubic_foot_per_day
])

energy_flow = UnitRegistry(units=[
    u.kilojoule_per_hour,
    u.kilojoule_per_minute,
    u.kilojoule_per_second,
    u.megajoule_per_hour,
    u.gigajoule_per_hour,
    u.kilowatt,
    u.megawatt,
    u.kilocalorie_per_hour,
    u.kilocalorie_per_minute,
    u.kilocalorie_per_second,
    u.million_kilocalorie_per_hour,
    u.calorie_per_hour,
    u.calorie_per_minute,
    u.calorie_per_second,
    u.Btu_per_hour,
    u.million_Btu_per_hour,
    u.million_Btu_per_day,
    u.horse_power
])

heat_flow = energy_flow

molar_density = UnitRegistry([
    u.kilomole_per_cubic_meter,
    u.mole_per_liter,
    u.mole_per_cubic_centimeter,
    u.mole_per_milliliter
])

molar_heat_capacity = UnitRegistry([
    u.kilojoule_per_mole_celsius,
    u.kilojoule_per_mole_kelvin,
    u.kilojoule_per_kilomole_celsius,
    u.kilojoule_per_kilomole_kelvin,
    u.joule_per_mole_celsius,
    u.joule_per_mole_kelvin,
    u.joule_per_kilomole_celsius,
    u.joule_per_kilomole_kelvin,
    u.kilocalorie_per_mole_celsius,
    u.kilocalorie_per_mole_kelvin,
    u.kilocalorie_per_kilomole_celsius,
    u.kilocalorie_per_kilomole_kelvin,
    u.calorie_per_mole_celsius,
    u.calorie_per_mole_kelvin,
    u.calorie_per_kilomole_celsius,
    u.calorie_per_kilomole_kelvin
])

molar_entropy = molar_heat_capacity

thermal_conductivity = UnitRegistry([
    u.watt_per_meter_kelvin,
    u.Btu_per_hour_foot_fahrenheit,
    u.kilocalorie_per_meter_hour_celsius,
    u.calorie_per_centimeter_second_celsius
])

viscosity = UnitRegistry([
    u.centipoise,
    u.millipoise,
    u.micropoise,
    u.poise,
    u.pascal_second,
    u.pound_force_second_per_square_foot,
    u.pound_mass_per_foot_second,
    u.pound_mass_per_foot_hour
])

surface_tension = UnitRegistry([
    u.dyne_per_centimeter,
    u.dyn_per_centimeter,
    u.pound_force_per_foot
])

mass_heat_capacity = UnitRegistry([
    u.kilojoule_per_gram_celsius,
    u.kilojoule_per_gram_kelvin,
    u.kilojoule_per_kilogram_celsius,
    u.kilojoule_per_kilogram_kelvin,
    u.joule_per_gram_celsius,
    u.joule_per_gram_kelvin,
    u.joule_per_kilogram_celsius,
    u.joule_per_kilogram_kelvin,
    u.kilocalorie_per_gram_celsius,
    u.kilocalorie_per_gram_kelvin,
    u.kilocalorie_per_kilogram_celsius,
    u.kilocalorie_per_kilogram_kelvin,
    u.calorie_per_gram_celsius,
    u.calorie_per_gram_kelvin,
    u.calorie_per_kilogram_celsius,
    u.calorie_per_kilogram_kelvin
])

mass_density = UnitRegistry([
    u.kilogram_per_cubic_meter,
    u.gram_per_liter,
    u.gram_per_cubic_centimeter,
    u.gram_per_milliliter
])

standard_gas_flow = UnitRegistry([
    u.Unit('Sm**3/h', factor=1 / u.hour.factor),
    u.Unit('Sm**3/d', factor=1 / u.day.factor),
    u.Unit('Sm**3/min', factor=1 / u.minute.factor),
    u.BaseUnit('Sm**3/s')
])

molar_enthalpy = UnitRegistry([
    u.kilojoule_per_mole,
    u.kilojoule_per_kilomole,
    u.joule_per_mole,
    u.joule_per_kilomole,
    u.megajoule_per_kilomole,
    u.kilocalorie_per_mole,
    u.kilocalorie_per_kilomole,
    u.calorie_per_mole,
    u.calorie_per_kilomole
])

molar_heat = molar_enthalpy

molar_energy = molar_heat

molar_volume = UnitRegistry([
    u.cubic_meter_per_mole,
    u.cubic_meter_per_kilomole,
    u.liter_per_mole,
    u.cubic_centimeter_per_mole,
    u.milliliter_per_mole
])

mass_entropy = mass_heat_capacity

mass_heat = UnitRegistry([
    u.kilojoule_per_gram,
    u.kilojoule_per_kilogram,
    u.joule_per_gram,
    u.joule_per_kilogram,
    u.megajoule_per_kilogram,
    u.kilocalorie_per_gram,
    u.kilocalorie_per_kilogram,
    u.calorie_per_gram,
    u.calorie_per_kilogram,
    u.Btu_per_pound,
])

mass_enthalpy = mass_heat

mass_energy = mass_heat

kinematic_viscosity = UnitRegistry([
    u.BaseUnit('cSt')
])

fraction = UnitRegistry([
    u.dimensionless,
    u.percent,
    u.parts_per_million
])

dimensionless = UnitRegistry([
    u.dimensionless
])
