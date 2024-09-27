from z_unit import unit


def test_unit():
    print("")
    print(repr(unit.kilojoule_per_kilogram_celsius))
    print("Format Test")
    print(f"Default Style: {unit.kilojoule_per_kilogram_celsius}")
    print(f"Quick Style: {unit.kilojoule_per_kilogram_celsius:q}")
    print(f"Python Style: {unit.kilojoule_per_kilogram_celsius:p}")
    print("multiply")
    print((unit.minute * unit.minute).factor)
    print((10 * unit.minute).factor)
    # assert False
