from z_units import quantity
from z_units import unit
from z_units.quantity import (
    Quantity,
    Length,
    Area,
    Volume,
    Time,
    Mass,
    Force,
    Substance,
    Energy,
    Velocity,
    Temperature,
    DeltaTemperature,
    Pressure,
    VolumeFlow,
    MassDensity,
    HeatFlow,
    MolarFlow,
    MassFlow,
    MolarDensity,
    MolarHeatCapacity,
    MolarEntropy,
    MolarHeat,
    ThermalConductivity,
    Viscosity,
    SurfaceTension,
    MassHeatCapacity,
    MassEntropy,
    MassHeat,
    StandardGasFlow,
    KinematicViscosity,
    MolarVolume,
    Fraction,
    Dimensionless,
)

__all__ = [
    "quantity",
    "unit",
    "Quantity",
    "Length",
    "Area",
    "Volume",
    "Time",
    "Mass",
    "Force",
    "Substance",
    "Energy",
    "Velocity",
    "Temperature",
    "DeltaTemperature",
    "Pressure",
    "VolumeFlow",
    "MassDensity",
    "HeatFlow",
    "MolarFlow",
    "MassFlow",
    "MolarDensity",
    "MolarHeatCapacity",
    "MolarEntropy",
    "MolarHeat",
    "ThermalConductivity",
    "Viscosity",
    "SurfaceTension",
    "MassHeatCapacity",
    "MassEntropy",
    "MassHeat",
    "StandardGasFlow",
    "KinematicViscosity",
    "MolarVolume",
    "Fraction",
    "Dimensionless",
    "convert",
]

quantity_registry = {
    cls: cls.get_unit_registry().symbols for cls in quantity.Quantity.__subclasses__()
}


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
