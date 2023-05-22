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
```