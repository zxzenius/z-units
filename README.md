# z-units

A simple unit converter for chemical engineering

## install

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
unit, value = f.unit, f.value
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
```