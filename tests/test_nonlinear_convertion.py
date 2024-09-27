from math import isclose

from z_unit import config
from z_unit import quantity as q


def test_convert():
    config.set_standard_temperature(20)
    f = q.MolarFlow(1, 'Nm3/h')
    f1 = f.to('Sm3/h').value
    config.set_standard_temperature(15)
    f2 = f.to('Sm3/h').value
    assert not isclose(f1, f2)
    config.set_standard_temperature(20)
