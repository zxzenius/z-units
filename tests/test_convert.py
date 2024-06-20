from zunits import convert
from zunits import quantity as q


def test_convert():
    assert convert(1, 'm', 'mm') == q.Length('1000 mm')
