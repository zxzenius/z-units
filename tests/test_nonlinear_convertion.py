from math import isclose

from z_units.environment import get_env
from z_units import quantity as q


def test_convert():
    env = get_env()
    env.reset()
    env.standard_temperature = 293.15
    f = q.MolarFlow(1, 'Nm3/h')
    f1 = f.to('Sm3/h').value
    env.standard_temperature = 273.15
    f2 = f.to('Sm3/h').value
    assert not isclose(f1, f2)
    env.reset()
