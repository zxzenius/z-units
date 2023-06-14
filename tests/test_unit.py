from z_units import unit


def test_unit():
    print("")
    print(repr(unit.kilojoule_per_kilogram_celsius))
    print("Format Test")
    print(f"Default Style: {unit.kilojoule_per_kilogram_celsius}")
    print(f"Quick Style: {unit.kilojoule_per_kilogram_celsius:q}")
    print(f"Defined Style: {unit.kilojoule_per_kilogram_celsius:d}")
    # assert False
