# z-units

A simple unit-converter for chemical engineers

## Feature

* Gauge pressure (MPag, kPag, psig, ...) can be used
* Friendly to HYSYS user

## Install

```shell
pip install z-units
```

## Usage

```python
from z_units import quantity as q
# pick a quantity
f = q.MolarFlow(3)
# to base unit
f.to_base()
# convert
f.to('kmol/s')
# list available units
print(f.units)
# get value
value, unit = f.value, f.unit
# gauge pressure
p = q.Pressure(5, 'bar').to('MPag')
# change local atmospheric pressure (default: 101325 Pa)
from z_units import config
config.set_local_atmospheric_pressure(50e3)
q.Pressure(100, 'kPa').to('kPag')
# change standard temperature (default: 20 degC)
# affect standard cubic meter "Sm**3"
config.set_standard_temperature(15)
q.Substance(100, 'Nm3').to('Sm3')
# formatting
# with unit in styles, format spec starts with "u"
format(q.MolarEntropy(100), 'u')
# '100 kJ/kmol-C' (quick-style)
format(q.MolarEntropy(100), 'up')
# '100 kJ/(kmol*C)' (expression-style)
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