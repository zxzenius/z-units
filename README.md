# z-units

A simple unit converter for chemical engineering

## Usage

```python
import z_units.quantity as q

# take a quantity
f = q.MolarFlow(3)
# to base unit
f.to_base()
# convert
f.to('kmol/s')
# list available units
f.units
# get value
unit, value = f.unit, f.value
# gauge pressure
p = q.Pressure(5, 'bar').to('MPag')
# change local atmospheric pressure (default: 101.325 kPa)
from z_units.config import set_local_atmospheric_pressure
set_local_atmospheric_pressure(50)
q.Pressure(100, 'kPa').to('kPag')
```