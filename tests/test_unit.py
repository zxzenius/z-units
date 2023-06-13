from z_units import unit


def test_unit():
    print("")
    print(repr(unit.kilojoule_per_kilogram_celsius))
    print("Format Test")
    print(f"Default symbol: {unit.kilojoule_per_kilogram_celsius}")
    print(f"H-Style symbol: {unit.kilojoule_per_kilogram_celsius:h}")
    print(f"Defined symbol: {unit.kilojoule_per_kilogram_celsius:d}")
    # assert False
