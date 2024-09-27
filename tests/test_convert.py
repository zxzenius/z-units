from z_unit import convert
from z_unit import quantity as q


def test_convert():
    assert convert(1, 'm', 'mm') == q.Length('1000 mm')
