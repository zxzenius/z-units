from z_unit import quantity
from z_unit import unit
from z_unit.quantity import Quantity

quantity_registry = {cls: cls.get_unit_registry().symbols for cls in quantity.Quantity.__subclasses__()}


def convert(value, from_unit: str, to_unit: str) -> Quantity:
    """
    Convert value with unit to target unit
    :param value:
    :param from_unit:
    :param to_unit:
    :return: Quantity instance if units match, otherwise return None.

    >>> convert(1, 'm', 'ft')
    <Length(3.2808399, 'ft')>
    """
    for Q, symbols in quantity_registry.items():
        if {from_unit, to_unit}.issubset(symbols):
            return Q(value, from_unit).to(to_unit)
        
    raise ValueError(f"Cannot convert from '{from_unit}' to '{to_unit}'")
