# z-units

A simple unit-converter for chemical engineers

## Feature

* Gauge pressure units (MPag, kPag, psig, ...) are ready for use
* Friendly to HYSYS user

## Install

```shell
pip install z-units
```

## Quickstart

```python
>>> from zunits import quantity as q
>>> f = q.MolarFlow(3)
>>> f
<MolarFlow(3, 'kmol/s')>
f.value, f.unit
(3, <Unit('kmol/s')>)
>>> f.to('kmol/h')
<MolarFlow(10800.0, 'kmol/h')>
>>> q.Length(100, 'cm') == q.Length(1000, 'mm')
True
>>> q.Temperature('100C')
<Temperature(1, 'C')>
>>> q.Pressure(15, 'psi').to('MPag')
<Pressure(0.0020963594, 'MPag')>
>>> from zunits import convert
>>> convert(1, 'm', 'ft')
<Length(3.2808399, 'ft')>
```
Related to gauge pressure, local atmospheric pressure (default: 101325 Pa) can be altered:

```python
>>> from zunits import config
# Before
>>> q.Pressure(100, 'kPa').to('kPag')
<Pressure(-1.325, 'kPag')>
# Set to 50e3 Pa (50 kPa)
>>> config.set_local_atmospheric_pressure(50e3)
# After
>>> q.Pressure(100, 'kPa').to('kPag')
<Pressure(50.0, 'kPag')>
```

Standard temperature (default: 20 degC) can be redefined, affecting standard cubic meter "Sm**3":

```python
# Before
>>> q.Substance(100, 'Nm3').to('Sm3')
<Substance(107.321984, 'Sm3')>
# Set to 15 degC
>>> config.set_standard_temperature(15)
# After
>>> q.Substance(100, 'Nm3').to('Sm3')
<Substance(105.491488, 'Sm3')>
```

Format quantity to string with styles:  
```python
# Only value
>>> format(q.MolarEntropy(100))
'100'
# With unit, quick style
>>> format(q.MolarEntropy(100), 'u')
'100 kJ/kmol-C'
# With unit, definition style
>>> format(q.MolarEntropy(100), 'up')
'100 kJ/(kmol*C)'
```

## Predefined Quantities

* Length
* Area
* Volume
* Time
* Mass
* Force
* Substance
* Energy
* Velocity
* Temperature
* DeltaTemperature
* Pressure
* VolumeFlow
* MassDensity
* HeatFlow
* MolarFlow
* MassFlow
* MolarDensity
* MolarHeatCapacity
* MolarEntropy
* MolarHeat
* ThermalConductivity
* Viscosity
* SurfaceTension
* MassHeatCapacity
* MassEntropy
* MassHeat
* StandardGasFlow
* KinematicViscosity
* MolarVolume
* Fraction
* Dimensionless

## About it

As a chemical engineer, the Gauge-Pressure units are very useful to me. Unfortunately those units are not supported in some popular modules, so I reinvent the wheel.
