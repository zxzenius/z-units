from __future__ import annotations
from typing import Iterable, Optional

from z_units import unit as u
from z_units.unit import Unit


class UnitRegistry:
    def __init__(self, name: str):
        self._name = name
        self._units: dict[str, Unit] = {}
        self._base_unit: Optional[Unit] = None
        

    def register(self, unit: Unit, is_base: bool = False):
        """
        Register a unit in the registry.

        Args:
            unit: The unit to register.
            is_base: Whether the unit is the base unit.

        Raises:
            ValueError: If the unit is already registered or if the base unit is already set.
        """
        if unit.symbol in self._units:
            raise ValueError(f"Unit {unit.symbol} already registered")

        unit._registry = self
        self._units[unit.symbol] = unit

        if is_base:
            if self._base_unit is not None:
                raise ValueError(f"Base unit already set to {self._base_unit.symbol}")
            self._base_unit = unit

    @property
    def base_unit(self) -> Optional[Unit]:
        return self._base_unit

    def get_unit(self, symbol: str) -> Unit:
        if symbol not in self._units:
            raise ValueError(f"Unit '{symbol}' not found")
        return self._units[symbol]        

    @property
    def units(self) -> list[Unit]:
        return list(self._units.values())

    @property
    def symbols(self) -> list[str]:
        return list(self._units.keys())


length = UnitRegistry(name="length")
length.register(u.meter, is_base=True)
length.register(u.kilometer)
length.register(u.decimeter)
length.register(u.centimeter)
length.register(u.millimeter)
length.register(u.micrometer)
length.register(u.foot)
length.register(u.inch)

area = UnitRegistry(name="area")
area.register(u.square_meter, is_base=True)
area.register(u.square_kilometer)
area.register(u.square_decimeter)
area.register(u.square_centimeter)
area.register(u.square_millimeter)
area.register(u.square_micrometer)
area.register(u.square_foot)
area.register(u.square_inch)

volume = UnitRegistry(name="volume")
volume.register(u.cubic_meter, is_base=True)
volume.register(u.cubic_centimeter)
volume.register(u.cubic_millimeter)
volume.register(u.millimeter)
volume.register(u.liter)
volume.register(u.milliliter)
volume.register(u.cubic_foot)
volume.register(u.cubic_inch)
volume.register(u.gallon)
volume.register(u.barrel)

time = UnitRegistry(name="time")
time.register(u.second, is_base=True)
time.register(u.minute)
time.register(u.hour)
time.register(u.day)
time.register(u.week)
time.register(u.year)
time.register(u.month)

mass = UnitRegistry(name="mass")
mass.register(u.kilogram, is_base=True)
mass.register(u.gram)
mass.register(u.tonne)
mass.register(u.pound)

force = UnitRegistry(name="force")
force.register(u.newton, is_base=True)
force.register(u.kilogram_meter_per_second_squared)
force.register(u.kilo_newton)
force.register(u.dyne)
force.register(u.kilogram_force)
force.register(u.tonne_force)
force.register(u.pound_force)

substance = UnitRegistry(name="substance")  
substance.register(u.kilomole, is_base=True)
substance.register(u.mole)
substance.register(u.normal_cubic_meter)
substance.register(u.standard_cubic_meter)
substance.register(u.standard_cubic_meter_20C)
substance.register(u.standard_cubic_meter_60F)
substance.register(u.standard_cubic_foot)
substance.register(u.kilo_standard_cubic_foot)
substance.register(u.million_standard_cubic_foot)

energy = UnitRegistry(name="energy")
energy.register(u.kilojoule, is_base=True)
energy.register(u.joule)
energy.register(u.megajoule)
energy.register(u.gigajoule)
energy.register(u.kilowatt_hour)
energy.register(u.kilowatt_year)
energy.register(u.calorie)
energy.register(u.kilocalorie)
energy.register(u.megacalorie)
energy.register(u.gigacalorie)
energy.register(u.million_kilocalorie)
energy.register(u.british_thermal_unit)
energy.register(u.million_british_thermal_unit)
energy.register(u.pound_force_foot)

velocity = UnitRegistry(name="velocity")
velocity.register(u.meter_per_second, is_base=True)
velocity.register(u.meter_per_minute)
velocity.register(u.meter_per_hour)
velocity.register(u.kilometer_per_hour)
velocity.register(u.centimeter_per_second)
velocity.register(u.foot_per_second)
velocity.register(u.foot_per_minute)
velocity.register(u.foot_per_hour)

temperature = UnitRegistry(name="temperature")
temperature.register(u.celsius, is_base=True)
temperature.register(u.kelvin)
temperature.register(u.fahrenheit)
temperature.register(u.rankine)

delta_temperature = UnitRegistry(name="delta_temperature")
delta_temperature.register(u.delta_celsius, is_base=True)
delta_temperature.register(u.delta_kelvin)
delta_temperature.register(u.delta_rankine)
delta_temperature.register(u.delta_fahrenheit)

pressure = UnitRegistry(name="pressure")
pressure.register(u.pascal, is_base=True)
pressure.register(u.kilopascal)
pressure.register(u.megapascal)
pressure.register(u.bar)
pressure.register(u.millibar)
pressure.register(u.atm)
pressure.register(u.kg_force_per_square_centimeter)
pressure.register(u.psi)
pressure.register(u.pound_force_per_square_foot)
pressure.register(u.torr)
pressure.register(u.mm_Hg)
pressure.register(u.inch_Hg)
pressure.register(u.inch_Hg_60F)
pressure.register(u.kilopascal_gauge)
pressure.register(u.megapascal_gauge)
pressure.register(u.bar_gauge)
pressure.register(u.millibar_gauge)
pressure.register(u.kg_force_per_square_centimeter_gauge)
pressure.register(u.psi_gauge)
pressure.register(u.pound_force_per_square_foot_gauge)
pressure.register(u.torr_gauge)
pressure.register(u.mm_Hg_gauge)
pressure.register(u.inch_Hg_gauge)
pressure.register(u.inch_Hg_60F_gauge)

molar_flow = UnitRegistry(name="molar_flow")
molar_flow.register(u.kilomole_per_second, is_base=True)
molar_flow.register(u.kilomole_per_hour)
molar_flow.register(u.kilomole_per_minute)
molar_flow.register(u.normal_cubic_meter_per_hour)
molar_flow.register(u.normal_cubic_meter_per_day)
molar_flow.register(u.standard_cubic_meter_per_hour)
molar_flow.register(u.standard_cubic_meter_20C_per_hour)
molar_flow.register(u.standard_cubic_meter_60F_per_hour)
molar_flow.register(u.standard_cubic_meter_per_day)
molar_flow.register(u.standard_cubic_meter_20C_per_day)
molar_flow.register(u.standard_cubic_meter_60F_per_day)
molar_flow.register(u.mole_per_hour)
molar_flow.register(u.mole_per_minute)
molar_flow.register(u.mole_per_second)
molar_flow.register(u.standard_cubic_foot_per_day)
molar_flow.register(u.kilo_standard_cubic_foot_per_hour)
molar_flow.register(u.kilo_standard_cubic_foot_per_day)
molar_flow.register(u.million_standard_cubic_foot_per_hour)
molar_flow.register(u.million_standard_cubic_foot_per_day)

mass_flow = UnitRegistry(name="mass_flow")
mass_flow.register(u.kilogram_per_hour)
mass_flow.register(u.kilogram_per_minute)
mass_flow.register(u.kilogram_per_second, is_base=True)
mass_flow.register(u.kilogram_per_day)
mass_flow.register(u.tonne_per_day)
mass_flow.register(u.tonne_per_hour)
mass_flow.register(u.tonne_per_year)
mass_flow.register(u.gram_per_hour)
mass_flow.register(u.gram_per_minute)
mass_flow.register(u.gram_per_second)
mass_flow.register(u.pound_per_hour)
mass_flow.register(u.pound_per_day)
mass_flow.register(u.kilo_pound_per_hour)
mass_flow.register(u.kilo_pound_per_day)
mass_flow.register(u.million_pound_per_day)

volume_flow = UnitRegistry(name="volume_flow")
volume_flow.register(u.cubic_meter_per_hour)
volume_flow.register(u.cubic_meter_per_minute)
volume_flow.register(u.cubic_meter_per_second, is_base=True)
volume_flow.register(u.cubic_meter_per_day)
volume_flow.register(u.liter_per_hour)
volume_flow.register(u.liter_per_day)
volume_flow.register(u.liter_per_minute)
volume_flow.register(u.liter_per_second)
volume_flow.register(u.milliliter_per_hour)
volume_flow.register(u.milliliter_per_minute)
volume_flow.register(u.milliliter_per_second)
volume_flow.register(u.barrel_per_day)
volume_flow.register(u.barrel_per_hour)
volume_flow.register(u.million_gallon_per_day)
volume_flow.register(u.US_gallon_per_minute)
volume_flow.register(u.US_gallon_per_hour)
volume_flow.register(u.cubic_foot_per_hour)
volume_flow.register(u.cubic_foot_per_day)

energy_flow = UnitRegistry(name="energy_flow")
energy_flow.register(u.kilojoule_per_hour)
energy_flow.register(u.kilojoule_per_minute)
energy_flow.register(u.kilojoule_per_second, is_base=True)
energy_flow.register(u.megajoule_per_hour)
energy_flow.register(u.gigajoule_per_hour)
energy_flow.register(u.kilowatt)
energy_flow.register(u.megawatt)
energy_flow.register(u.kilocalorie_per_hour)
energy_flow.register(u.kilocalorie_per_minute)
energy_flow.register(u.kilocalorie_per_second)
energy_flow.register(u.million_kilocalorie_per_hour)
energy_flow.register(u.calorie_per_hour)
energy_flow.register(u.calorie_per_minute)
energy_flow.register(u.calorie_per_second)
energy_flow.register(u.Btu_per_hour)
energy_flow.register(u.million_Btu_per_hour)
energy_flow.register(u.million_Btu_per_day)
energy_flow.register(u.horse_power)

heat_flow = energy_flow

molar_density = UnitRegistry(name="molar_density")
molar_density.register(u.kilomole_per_cubic_meter, is_base=True)
molar_density.register(u.mole_per_liter)
molar_density.register(u.mole_per_cubic_centimeter)
molar_density.register(u.mole_per_milliliter)

molar_heat_capacity = UnitRegistry(name="molar_heat_capacity")
molar_heat_capacity.register(u.kilojoule_per_mole_celsius)
molar_heat_capacity.register(u.kilojoule_per_mole_kelvin)
molar_heat_capacity.register(u.kilojoule_per_kilomole_celsius, is_base=True)
molar_heat_capacity.register(u.kilojoule_per_kilomole_kelvin)
molar_heat_capacity.register(u.joule_per_mole_celsius)
molar_heat_capacity.register(u.joule_per_mole_kelvin)
molar_heat_capacity.register(u.joule_per_kilomole_celsius)
molar_heat_capacity.register(u.joule_per_kilomole_kelvin)
molar_heat_capacity.register(u.kilocalorie_per_mole_celsius)
molar_heat_capacity.register(u.kilocalorie_per_mole_kelvin)
molar_heat_capacity.register(u.kilocalorie_per_kilomole_celsius)
molar_heat_capacity.register(u.kilocalorie_per_kilomole_kelvin)
molar_heat_capacity.register(u.calorie_per_mole_celsius)
molar_heat_capacity.register(u.calorie_per_mole_kelvin)
molar_heat_capacity.register(u.calorie_per_kilomole_celsius)
molar_heat_capacity.register(u.calorie_per_kilomole_kelvin)

molar_entropy = molar_heat_capacity

thermal_conductivity = UnitRegistry(name="thermal_conductivity")
thermal_conductivity.register(u.watt_per_meter_kelvin, is_base=True)
thermal_conductivity.register(u.Btu_per_hour_foot_fahrenheit)
thermal_conductivity.register(u.kilocalorie_per_meter_hour_celsius)
thermal_conductivity.register(u.calorie_per_centimeter_second_celsius)

viscosity = UnitRegistry(name="viscosity")
viscosity.register(u.centipoise, is_base=True)
viscosity.register(u.millipoise)
viscosity.register(u.micropoise)
viscosity.register(u.poise)
viscosity.register(u.pascal_second)
viscosity.register(u.pound_force_second_per_square_foot)
viscosity.register(u.pound_mass_per_foot_second)
viscosity.register(u.pound_mass_per_foot_hour)

surface_tension = UnitRegistry(name="surface_tension")
surface_tension.register(u.dyne_per_centimeter, is_base=True)
surface_tension.register(u.dyn_per_centimeter)
surface_tension.register(u.pound_force_per_foot)

mass_heat_capacity = UnitRegistry(name="mass_heat_capacity")    
mass_heat_capacity.register(u.kilojoule_per_gram_celsius)
mass_heat_capacity.register(u.kilojoule_per_gram_kelvin)
mass_heat_capacity.register(u.kilojoule_per_kilogram_celsius, is_base=True)
mass_heat_capacity.register(u.kilojoule_per_kilogram_kelvin)
mass_heat_capacity.register(u.joule_per_gram_celsius)
mass_heat_capacity.register(u.joule_per_gram_kelvin)
mass_heat_capacity.register(u.joule_per_kilogram_celsius)
mass_heat_capacity.register(u.joule_per_kilogram_kelvin)
mass_heat_capacity.register(u.kilocalorie_per_gram_celsius)
mass_heat_capacity.register(u.kilocalorie_per_gram_kelvin)
mass_heat_capacity.register(u.kilocalorie_per_kilogram_celsius)
mass_heat_capacity.register(u.kilocalorie_per_kilogram_kelvin)
mass_heat_capacity.register(u.calorie_per_gram_celsius)
mass_heat_capacity.register(u.calorie_per_gram_kelvin)
mass_heat_capacity.register(u.calorie_per_kilogram_celsius)
mass_heat_capacity.register(u.calorie_per_kilogram_kelvin)

mass_density = UnitRegistry(name="mass_density")
mass_density.register(u.kilogram_per_cubic_meter, is_base=True)
mass_density.register(u.gram_per_liter)
mass_density.register(u.gram_per_cubic_centimeter)
mass_density.register(u.gram_per_milliliter)

standard_gas_flow = UnitRegistry(name="standard_gas_flow")
standard_gas_flow.register(u.Unit('Sm**3/h', factor=1 / u.hour.factor))
standard_gas_flow.register(u.Unit('Sm**3/d', factor=1 / u.day.factor))
standard_gas_flow.register(u.Unit('Sm**3/min', factor=1 / u.minute.factor))
standard_gas_flow.register(u.Unit('Sm**3/s'), is_base=True)

molar_enthalpy = UnitRegistry(name="molar_enthalpy")
molar_enthalpy.register(u.kilojoule_per_mole)
molar_enthalpy.register(u.kilojoule_per_kilomole, is_base=True)
molar_enthalpy.register(u.joule_per_mole)
molar_enthalpy.register(u.joule_per_kilomole)
molar_enthalpy.register(u.megajoule_per_kilomole)
molar_enthalpy.register(u.kilocalorie_per_mole)
molar_enthalpy.register(u.kilocalorie_per_kilomole)
molar_enthalpy.register(u.calorie_per_mole)
molar_enthalpy.register(u.calorie_per_kilomole)

molar_heat = molar_enthalpy

molar_energy = molar_heat

molar_volume = UnitRegistry(name="molar_volume")
molar_volume.register(u.cubic_meter_per_mole)
molar_volume.register(u.cubic_meter_per_kilomole, is_base=True)
molar_volume.register(u.liter_per_mole)
molar_volume.register(u.cubic_centimeter_per_mole)
molar_volume.register(u.milliliter_per_mole)

mass_entropy = mass_heat_capacity

mass_heat = UnitRegistry(name="mass_heat")
mass_heat.register(u.kilojoule_per_gram)
mass_heat.register(u.kilojoule_per_kilogram, is_base=True)
mass_heat.register(u.joule_per_gram)
mass_heat.register(u.joule_per_kilogram)
mass_heat.register(u.megajoule_per_kilogram)
mass_heat.register(u.kilocalorie_per_gram)
mass_heat.register(u.kilocalorie_per_kilogram)
mass_heat.register(u.calorie_per_gram)
mass_heat.register(u.calorie_per_kilogram)
mass_heat.register(u.Btu_per_pound)

mass_enthalpy = mass_heat

mass_energy = mass_heat

kinematic_viscosity = UnitRegistry(name="kinematic_viscosity")
kinematic_viscosity.register(u.Unit('cSt'), is_base=True)

fraction = UnitRegistry(name="fraction")
fraction.register(u.dimensionless, is_base=True)
fraction.register(u.percent)
fraction.register(u.parts_per_million)

dimensionless = UnitRegistry(name="dimensionless")
dimensionless.register(u.dimensionless, is_base=True)
