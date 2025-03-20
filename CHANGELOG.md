## Release v0.1.9 (2025.0320)

- Fix package name bug (z_unit -> z_units)

## Release v0.1.8 (2025.0312)

### Features & Improvements

- `environment` module for global configuration management

### Breaking Changes

- Removed `config` module in favor of new `environment` module
- Changed configuration interface: use `get_env()` instead of direct config functions

### Migration Guide

Old configuration:

```python
from z_units import config

config.set_local_atmospheric_pressure(100e3)
config.set_standard_temperature(15)
```

New configuration:

```python
from z_units.environment import get_env

env = get_env()
env.atmospheric_pressure = 100e3  # in Pa
env.standard_temperature = 273.15 + 15  # in K
```

## Release v0.1.7 (2024.0616)


### Features & Improvements

- `convert()` method for shortcut.
- `Quantity` can parse str value with unit, ie: `Length("1m")`.