# z-units

A simple unit-converter for chemical engineers

## Features

* Gauge pressure units (MPag, kPag, psig, ...) with configurable atmospheric pressure
* Standard volume units (Sm³, Nm³) with configurable STP conditions
* Friendly to HYSYS users
* Rich formatting options

## Installation

```shell
pip install z-units
```

## Quickstart

```python
>>> from z_unit import quantity as q
>>> f = q.MolarFlow(3)
>>> f
<MolarFlow(3, 'kmol/s')>
>>> f.value, f.unit
(3, <Unit('kmol/s')>)
>>> f.to('kmol/h')
<MolarFlow(10800.0, 'kmol/h')>
>>> q.Length(100, 'cm') == q.Length(1000, 'mm')
True
>>> q.Temperature('100C')
<Temperature(1, 'C')>
>>> q.Pressure(15, 'psi').to('MPag')
<Pressure(0.0020963594, 'MPag')>
>>> from z_unit import convert
>>> convert(1, 'm', 'ft')
<Length(3.2808399, 'ft')>
```

## Advanced Features

### Gauge Pressure Handling

The atmospheric pressure reference (default: 101325 Pa) can be configured globally:

```python
>>> from z_unit.environment import get_env
# Before
>>> q.Pressure(100, 'kPa').to('kPag')
<Pressure(-1.325, 'kPag')>
# Set to 100 kPa
# atmospheric_pressure in Pa
>>> env = get_env()
>>> env.atmospheric_pressure = 100e3
# After
>>> q.Pressure(100, 'kPa').to('kPag')
<Pressure(0.0, 'kPag')>
```

### Standard Volume Units

Standard temperature and pressure (STP) conditions can be configured for standard volume conversions:

```python
>>> from z_unit.environment import get_env
# Default STP: 20°C, 101325 Pa
>>> q.Substance(100, 'Nm³').to('Sm³')
<Substance(107.321984, 'Sm³')>
# Change to 15°C, set value in K
>>> get_env().standard_temperature = 273.15 + 15
>>> q.Substance(100, 'Nm³').to('Sm³')
<Substance(105.491488, 'Sm³')>
```

### Unit Formatting

Multiple formatting styles are supported:

```python
>>> x = q.MolarEntropy(100)
# Only value
>>> f"{x}"
'100'
# Quick style (simplified)
>>> f"{x:q}"
'100 kJ/kmol-C'
# Python style (full)
>>> f"{x:p}"
'100 kJ/(kmol*C)'
```

## Predefined Quantities

* Length (m, km, cm, mm, ft, in, ...)
* Area (m², km², ...)
* Volume (m³, L, mL, ...)
* Time (s, min, h, ...)
* Mass (kg, g, lb, ...)
* Force (N, kN, ...)
* Substance (mol, kmol, ...)
* Energy (J, kJ, kWh, ...)
* Velocity (m/s, km/h, ...)
* Temperature (K, °C, °F)
* DeltaTemperature (K, °C, °F)
* Pressure (Pa, kPa, MPa, bar, psi, ...) including gauge variants
* VolumeFlow (m³/s, L/min, ...)
* StandardGasFlow (Nm³/h, Sm³/h, ...)
* MolarFlow (mol/s, kmol/h, ...)
* MassFlow (kg/s, t/h, ...)
* Density (kg/m³, g/cm³, ...)
* MolarDensity (mol/m³, kmol/m³)
* HeatCapacity (J/(kg·K), kJ/(kg·K))
* MolarHeatCapacity (J/(mol·K), kJ/(kmol·K))
* Entropy (J/(kg·K), kJ/(kg·K))
* MolarEntropy (J/(mol·K), kJ/(kmol·K))
* ThermalConductivity (W/(m·K))
* Viscosity (Pa·s, cP)
* KinematicViscosity (m²/s, cSt)
* SurfaceTension (N/m)
* Dimensionless (-, %)

## Environment Configuration

Global environment parameters can be configured:

```python
>>> from z_unit.environment import get_env
# Set atmospheric pressure
>>> get_env().atmospheric_pressure = 100e3  # 100 kPa
# Set standard conditions
>>> get_env().standard_temperature = 273.15  # 0°C
>>> get_env().standard_pressure = 101325  # 1 atm
# Reset to defaults
>>> get_env().reset()
```

## About

As a chemical engineer, the Gauge-Pressure units are very useful to me. Unfortunately 
those units are not supported in some popular modules, so I reinvent the wheel.

## License

MIT License
