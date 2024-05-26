from math import isclose

from zunits import quantity as q
from zunits.config import set_local_atmospheric_pressure, set_standard_temperature, get_standard_temperature


def test_length():
    x = q.Length(1)
    assert x.unit.symbol == 'm'
    assert x.unit == x.base_unit
    assert f'{x:u}' == '1 m'
    assert f'{x:uq}' == '1 m'
    assert f'{x:up}' == '1 m'
    print(f"Length(1) * 5 = {x * 5:u}")
    print(f"5 * Length(1) = {5 * x:u}")
    print(f"5 * Length(1, 'ft') = {5 * q.Length(1, 'ft'):u}")
    assert isclose(x.to('km').value, 1e-3, rel_tol=1e-4)
    assert isclose(x.to('dm').value, 1e1, rel_tol=1e-4)
    assert isclose(x.to('cm').value, 1e2, rel_tol=1e-4)
    assert isclose(x.to('mm').value, 1e3, rel_tol=1e-4)
    assert isclose(x.to('um').value, 1e6, rel_tol=1e-4)
    assert isclose(x.to('ft').value, 3.28084, rel_tol=1e-4)
    assert isclose(x.to('in').value, 39.37008, rel_tol=1e-4)


def test_area():
    x = q.Area(1)
    assert x.unit.symbol == 'm2'
    assert f'{x:u}' == '1 m2'
    assert f'{x:up}' == '1 m**2'
    assert x.unit == x.base_unit
    assert isclose(x.to('km2').value, 1e-6, rel_tol=1e-4)
    assert isclose(x.to('dm2').value, 1e2, rel_tol=1e-4)
    assert isclose(x.to('cm2').value, 1e4, rel_tol=1e-4)
    assert isclose(x.to('mm2').value, 1e6, rel_tol=1e-4)
    assert isclose(x.to('um2').value, 1e12, rel_tol=1e-4)
    assert isclose(x.to('ft2').value, 10.7639, rel_tol=1e-4)
    assert isclose(x.to('in2').value, 1550.0016000682, rel_tol=1e-4)


def test_volume():
    x = q.Volume(1)
    assert x.unit.symbol == 'm3'
    assert x.unit == x.base_unit
    assert isclose(x.to('cm3').value, 1e6, rel_tol=1e-4)
    assert isclose(x.to('mm3').value, 1e9, rel_tol=1e-4)
    assert isclose(x.to('L').value, 1e3, rel_tol=1e-4)
    assert isclose(x.to('mL').value, 1e6, rel_tol=1e-4)
    assert isclose(x.to('ft3').value, 35.3147, rel_tol=1e-4)
    assert isclose(x.to('in3').value, 61023.801579099, rel_tol=1e-4)
    assert isclose(x.to('gal').value, 264.1723012, rel_tol=1e-4)
    assert isclose(x.to('bbl').value, 6.28981, rel_tol=1e-4)


def test_time():
    x = q.Time(1)
    assert x.unit.symbol == 's'
    assert x.unit == x.base_unit
    assert isclose(x.to('min').value, 1 / 60, rel_tol=1e-4)
    assert isclose(x.to('hr').value, 1 / 3600, rel_tol=1e-4)
    assert isclose(x.to('day').value, 1 / 3600 / 24, rel_tol=1e-4)
    assert isclose(x.to('yr').value, 1 / 3600 / 8760, rel_tol=1e-4)
    assert isclose(x.to('mon').value, 1 / 3600 / 8760 * 12, rel_tol=1e-4)


def test_mass():
    x = q.Mass(1)
    assert x.unit.symbol == 'kg'
    assert x.unit == x.base_unit
    assert isclose(x.to('g').value, 1e3, rel_tol=1e-4)
    assert isclose(x.to('t').value, 1e-3, rel_tol=1e-4)
    assert isclose(x.to('lb').value, 2.20462, rel_tol=1e-4)


def test_force():
    x = q.Force(1)
    assert x.unit.symbol == 'N'
    assert x.unit == x.base_unit
    assert isclose(x.to('kg-m/s2').value, 1, rel_tol=1e-4)
    assert isclose(x.to('kN').value, 1e-3, rel_tol=1e-4)
    assert isclose(x.to('dyn').value, 1e5, rel_tol=1e-4)
    assert isclose(x.to('kgf').value, 0.101972, rel_tol=1e-4)
    assert isclose(x.to('tonf').value, 0.101972e-3, rel_tol=1e-4)
    assert isclose(x.to('lbf').value, 0.224809, rel_tol=1e-4)


def test_substance():
    x = q.Substance(1)
    assert x.unit.symbol == 'kmol'
    assert x.unit == x.base_unit
    assert isclose(x.to('mol').value, 1e3, rel_tol=1e-4)
    assert isclose(x.to('Nm3').value, 22.414, rel_tol=1e-4)
    assert isclose(x.to('Sm3_20C').value, 24.055149, rel_tol=1e-4)
    assert isclose(x.to('SCF').value, 836.56108, rel_tol=1e-4)
    assert isclose(x.to('MSCF').value, 836.56108e-3, rel_tol=1e-4)
    assert isclose(x.to('MMSCF').value, 836.56108e-6, rel_tol=1e-4)
    set_standard_temperature(0)
    assert isclose(x.to('Sm3').value, x.to('Nm3').value)


def test_energy():
    x = q.Energy(1)
    assert x.unit.symbol == 'kJ'
    assert x.unit == x.base_unit
    assert isclose(x.to('J').value, 1e3, rel_tol=1e-4)
    assert isclose(x.to('MJ').value, 1e-3, rel_tol=1e-4)
    assert isclose(x.to('GJ').value, 1e-6, rel_tol=1e-4)
    assert isclose(x.to('kW-h').value, 0.000277778, rel_tol=1e-4)
    assert isclose(x.to('kW-yr').value, 1 / 3600 / 8760, rel_tol=1e-4)
    assert isclose(x.to('cal').value, 0.239006e3, rel_tol=1e-4)
    assert isclose(x.to('kcal').value, 0.239006, rel_tol=1e-4)
    assert isclose(x.to('Mcal').value, 0.239006e-3, rel_tol=1e-4)
    assert isclose(x.to('Gcal').value, 0.239006e-6, rel_tol=1e-4)
    assert isclose(x.to('MMkcal').value, 0.239006e-6, rel_tol=1e-4)
    assert isclose(x.to('Btu').value, 0.947818, rel_tol=1e-4)
    assert isclose(x.to('MMBtu').value, 0.947818e-6, rel_tol=1e-4)
    assert isclose(x.to('lbf-ft').value, 737.562, rel_tol=1e-4)


def test_velocity():
    x = q.Velocity(1)
    assert x.unit.symbol == 'm/s'
    assert x.unit == x.base_unit
    assert isclose(x.to('m/min').value, 60, rel_tol=1e-4)
    assert isclose(x.to('m/hr').value, 3600, rel_tol=1e-4)
    assert isclose(x.to('km/hr').value, 1e-3 * 3600, rel_tol=1e-4)
    assert isclose(x.to('cm/s').value, 100, rel_tol=1e-4)
    assert isclose(x.to('ft/s').value, 3.28084, rel_tol=1e-4)
    assert isclose(x.to('ft/min').value, 3.28084 * 60, rel_tol=1e-4)
    assert isclose(x.to('ft/hr').value, 3.28084 * 3600, rel_tol=1e-4)


def test_temperature():
    x = q.Temperature(25)
    assert x.value == 25
    assert x.unit.symbol == 'C'
    assert isclose(x.to('K').value, 298.15)
    assert isclose(x.to('F').value, 77)
    assert isclose(x.to('R').value, 536.67)
    assert isclose(q.Temperature(300, 'K').to_base().value, 26.85)
    assert isclose(q.Temperature(200, 'C').to_base().value, 200)
    assert isclose(q.Temperature(100, 'F').to_base().value, 37.7777778)
    assert isclose(q.Temperature(50, 'R').to_base().value, -245.3722222)
    assert isclose(q.Temperature(300, 'K').to('F').value, 80.33)


def test_delta_temperature():
    x = q.DeltaTemperature(1)
    assert x.unit.symbol == 'C'
    assert x.unit == x.base_unit
    assert isclose(x.to('K').value, 1, rel_tol=1e-4)
    assert isclose(x.to('R').value, 1.8, rel_tol=1e-4)
    assert isclose(x.to('F').value, 1.8, rel_tol=1e-4)


def test_pressure():
    x = q.Pressure(100, 'kPa')
    assert x.value == 100
    assert x.unit.symbol == 'kPa'
    assert isclose(x.to('Pa').value, 100e3)
    assert isclose(x.to('MPa').value, 100e-3)
    assert isclose(x.to('bar').value, 100e-2)
    assert isclose(x.to('mbar').value, 1000)
    assert isclose(x.to('kgf/cm2').value, 1.019716, rel_tol=1e-4)
    assert isclose(x.to('atm').value, 0.9869233, rel_tol=1e-4)
    assert isclose(x.to('psi').value, 14.503774, rel_tol=1e-4)
    assert isclose(x.to('lbf/ft2').value, 2088.543, rel_tol=1e-4)
    assert isclose(x.to('torr').value, 750.06168, rel_tol=1e-4)
    assert isclose(x.to('mmHg_0C').value, 750.06168, rel_tol=1e-4)
    assert isclose(x.to('inHg_32F').value, 29.52998, rel_tol=1e-4)
    assert isclose(x.to('inHg_60F').value, 29.61340, rel_tol=1e-4)
    assert isclose(x.to('kPag').value, -1.325, rel_tol=1e-4)
    assert isclose(x.to('MPag').value * 1000, -1.325, rel_tol=1e-4)
    assert isclose(x.to('barg').value * 100, -1.325, rel_tol=1e-4)
    assert isclose(x.to('kgf/cm2_g').value, -0.0135112, rel_tol=1e-4)
    assert isclose(x.to('psig').value, -0.19218, rel_tol=1e-4)
    assert isclose(x.to('lbf/ft2_g').value, -27.673, rel_tol=1e-4)
    assert isclose(x.to('torr_g').value, -9.9385, rel_tol=1e-4)
    assert isclose(x.to('mmHg_0C_g').value, -9.9385, rel_tol=1e-4)
    assert isclose(x.to('inHg_32F_g').value, -0.39127, rel_tol=1e-4)
    assert isclose(x.to('inHg_60F_g').value, -0.39237, rel_tol=1e-4)
    assert isclose(q.Pressure(1, 'MPag').to('psi').value, 159.73368651, rel_tol=1e-4)
    set_local_atmospheric_pressure(50e3)
    assert isclose(x.to('kPag').value, 50)


def test_volume_flow():
    v = q.VolumeFlow(1)
    assert v.unit.symbol == 'm3/s'
    assert v.base_unit.symbol == v.unit.symbol
    assert isclose(v.to('m3/h').value, 3600, rel_tol=1e-6)
    assert isclose(v.to('m3/min').value, 60, rel_tol=1e-6)
    assert isclose(v.to('m3/d').value, 3600 * 24, rel_tol=1e-6)
    assert isclose(v.to('L/h').value, 3600000, rel_tol=1e-6)
    assert isclose(v.to('L/d').value, 3600000 * 24, rel_tol=1e-6)
    assert isclose(v.to('L/min').value, 60000, rel_tol=1e-6)
    assert isclose(v.to('L/s').value, 1000, rel_tol=1e-6)
    assert isclose(v.to('mL/h').value, 3600000000, rel_tol=1e-6)
    assert isclose(v.to('mL/min').value, 60e6, rel_tol=1e-6)
    assert isclose(v.to('mL/s').value, 1e6, rel_tol=1e-6)
    assert isclose(v.to('bbl/d').value, 6.2898106 * 24 * 3600, rel_tol=1e-6)
    assert isclose(v.to('bbl/h').value, 6.2898106 * 3600, rel_tol=1e-6)
    assert isclose(v.to('MMgal/d').value, 264.172 * 24 * 3600 / 1e6, rel_tol=1e-6)
    assert isclose(v.to('USGPM').value, 264.172 * 60, rel_tol=1e-6)
    assert isclose(v.to('USGPH').value, 264.172 * 3600, rel_tol=1e-6)
    assert isclose(v.to('ft3/h').value, 35.3147 * 3600, rel_tol=1e-6)
    assert isclose(v.to('ft3/d').value, 35.3147 * 24 * 3600, rel_tol=1e-6)


def test_mass_density():
    x = q.MassDensity(100)
    assert x.unit.symbol == 'kg/m3'
    assert x.unit == x.base_unit
    assert isclose(x.to('g/L').value, 100, rel_tol=1e-4)
    assert isclose(x.to('g/cm3').value, 0.1, rel_tol=1e-4)
    assert isclose(x.to('g/mL').value, 0.1, rel_tol=1e-4)


def test_heat_flow():
    h = q.HeatFlow(1)
    assert h.unit.symbol == 'kJ/s'
    assert h.unit == h.base_unit
    assert isclose(h.to('kJ/h').value, 3600, rel_tol=1e-6)
    assert isclose(h.to('kJ/min').value, 60, rel_tol=1e-6)
    assert isclose(h.to('MJ/h').value, 3.6, rel_tol=1e-6)
    assert isclose(h.to('GJ/h').value, 3.6e-3, rel_tol=1e-6)
    assert isclose(h.to('kW').value, 1, rel_tol=1e-6)
    assert isclose(h.to('MW').value, 1e-3, rel_tol=1e-6)
    assert isclose(h.to('kcal/h').value, 860.421, rel_tol=1e-6)
    assert isclose(h.to('kcal/min').value, 14.34, rel_tol=1e-4)
    assert isclose(h.to('kcal/s').value, 0.239006, rel_tol=1e-4)
    assert isclose(h.to('MMkcal/h').value, 860.421e-6, rel_tol=1e-4)
    assert isclose(h.to('cal/h').value, 860.421e3, rel_tol=1e-4)
    assert isclose(h.to('cal/min').value, 14.34e3, rel_tol=1e-4)
    assert isclose(h.to('cal/s').value, 0.239006e3, rel_tol=1e-4)
    assert isclose(h.to('Btu/h').value, 3412.14, rel_tol=1e-4)
    assert isclose(h.to('MMBtu/h').value, 3412.14e-6, rel_tol=1e-4)
    assert isclose(h.to('MMBtu/d').value, 3412.14e-6 * 24, rel_tol=1e-4)
    assert isclose(h.to('hp').value, 1.341022, rel_tol=1e-4)


def test_molar_flow():
    x = q.MolarFlow(1)
    assert x.unit.symbol == 'kmol/s'
    assert x.unit == x.base_unit
    assert isclose(x.to('kmol/h').value, 3600, rel_tol=1e-4)
    assert isclose(x.to('kmol/min').value, 60, rel_tol=1e-4)
    assert isclose(x.to('Nm3/h').value, 80690.4, rel_tol=1e-4)
    assert isclose(x.to('Nm3/d').value, 1936569.6, rel_tol=1e-4)
    set_standard_temperature(20)
    assert isclose(x.to('Sm3/h').value, 86598.538, rel_tol=1e-4)
    assert isclose(x.to('Sm3/d').value, 2078364.92, rel_tol=1e-4)
    assert isclose(x.to('mol/h').value, 3600e3, rel_tol=1e-4)
    assert isclose(x.to('mol/min').value, 60e3, rel_tol=1e-4)
    assert isclose(x.to('mol/s').value, 1e3, rel_tol=1e-4)
    assert isclose(x.to('SCFD').value, 7.22788776e7, rel_tol=1e-4)
    assert isclose(x.to('MSCFH').value, 3.0116196e3, rel_tol=1e-4)
    assert isclose(x.to('MSCFD').value, 7.22788776e4, rel_tol=1e-4)
    assert isclose(x.to('MMSCFH').value, 3.0116196, rel_tol=1e-4)
    assert isclose(x.to('MMSCFD').value, 72.2788776, rel_tol=1e-4)


def test_mass_flow():
    x = q.MassFlow(1)
    assert x.unit.symbol == 'kg/s'
    assert x.unit == x.base_unit
    assert isclose(x.to('kg/h').value, 3600, rel_tol=1e-4)
    assert isclose(x.to('kg/min').value, 60, rel_tol=1e-4)
    assert isclose(x.to('kg/d').value, 86400, rel_tol=1e-4)
    assert isclose(x.to('t/d').value, 86.4, rel_tol=1e-4)
    assert isclose(x.to('t/h').value, 3.6, rel_tol=1e-4)
    assert isclose(x.to('t/yr').value, 31536, rel_tol=1e-4)
    assert isclose(x.to('g/h').value, 3600e3, rel_tol=1e-4)
    assert isclose(x.to('g/min').value, 60e3, rel_tol=1e-4)
    assert isclose(x.to('g/s').value, 1e3, rel_tol=1e-4)
    assert isclose(x.to('lb/h').value, 7936.56, rel_tol=1e-4)
    assert isclose(x.to('lb/d').value, 190479.348, rel_tol=1e-4)
    assert isclose(x.to('klb/h').value, 7.93656, rel_tol=1e-4)
    assert isclose(x.to('klb/d').value, 190.47744, rel_tol=1e-4)
    assert isclose(x.to('MMlb/d').value, 0.19047744, rel_tol=1e-4)


def test_molar_density():
    x = q.MolarDensity(1)
    assert x.unit.symbol == 'kmol/m3'
    assert x.unit == x.base_unit
    assert isclose(x.to('mol/L').value, 1, rel_tol=1e-4)
    assert isclose(x.to('mol/cm3').value, 1e-3, rel_tol=1e-4)
    assert isclose(x.to('mol/mL').value, 1e-3, rel_tol=1e-4)


def test_molar_heat_capacity():
    x = q.MolarHeatCapacity(1)
    assert x.unit.symbol == 'kJ/kmol-C'
    assert x.unit == x.base_unit
    assert isclose(x.to('kJ/mol-C').value, 1e-3, rel_tol=1e-4)
    assert isclose(x.to('kJ/mol-K').value, 1e-3, rel_tol=1e-4)
    assert isclose(x.to('kJ/kmol-K').value, 1, rel_tol=1e-4)
    assert isclose(x.to('J/mol-C').value, 1, rel_tol=1e-4)
    assert isclose(x.to('J/mol-K').value, 1, rel_tol=1e-4)
    assert isclose(x.to('J/kmol-C').value, 1e3, rel_tol=1e-4)
    assert isclose(x.to('J/kmol-K').value, 1e3, rel_tol=1e-4)
    assert isclose(x.to('kcal/kmol-C').value, 0.239006, rel_tol=1e-4)
    assert isclose(x.to('kcal/kmol-K').value, 0.239006, rel_tol=1e-4)
    assert isclose(x.to('cal/mol-C').value, 0.239006, rel_tol=1e-4)
    assert isclose(x.to('cal/mol-K').value, 0.239006, rel_tol=1e-4)
    assert isclose(x.to('cal/kmol-C').value, 0.239006e3, rel_tol=1e-4)
    assert isclose(x.to('cal/kmol-K').value, 0.239006e3, rel_tol=1e-4)


def test_molar_entropy():
    x = q.MolarEntropy(1)
    assert x.unit.symbol == 'kJ/kmol-C'


def test_molar_heat():
    x = q.MolarHeat(1)
    assert x.unit.symbol == 'kJ/kmol'
    assert x.unit == x.base_unit
    assert isclose(x.to('kJ/mol').value, 1e-3, rel_tol=1e-4)
    assert isclose(x.to('J/mol').value, 1, rel_tol=1e-4)
    assert isclose(x.to('J/kmol').value, 1e3, rel_tol=1e-4)
    assert isclose(x.to('MJ/kmol').value, 1e-3, rel_tol=1e-4)
    assert isclose(x.to('kcal/mol').value, 0.239006e-3, rel_tol=1e-4)
    assert isclose(x.to('kcal/kmol').value, 0.239006, rel_tol=1e-4)
    assert isclose(x.to('cal/mol').value, 0.239006, rel_tol=1e-4)
    assert isclose(x.to('cal/kmol').value, 0.239006e3, rel_tol=1e-4)


def test_thermal_conductivity():
    x = q.ThermalConductivity(1)
    assert x.unit.symbol == 'W/m-K'
    assert x.unit == x.base_unit
    assert isclose(x.to('Btu/h-ft-F').value, 0.577789, rel_tol=1e-4)
    assert isclose(x.to('kcal/m-h-C').value, 0.8604216, rel_tol=1e-4)
    assert isclose(x.to('cal/cm-s-C').value, 0.00239, rel_tol=1e-4)


def test_viscosity():
    x = q.Viscosity(1)
    assert x.unit.symbol == 'cP'
    assert x.unit == x.base_unit
    assert isclose(x.to('mP').value, 10, rel_tol=1e-4)
    assert isclose(x.to('microP').value, 1e4, rel_tol=1e-4)
    assert isclose(x.to('P').value, 1e-2, rel_tol=1e-4)
    assert isclose(x.to('Pa-s').value, 1e-3, rel_tol=1e-4)
    assert isclose(x.to('lbf-s/ft2').value, 0.0000208854, rel_tol=1e-4)
    assert isclose(x.to('lbm/ft-s').value, 0.000671968994813, rel_tol=1e-4)
    assert isclose(x.to('lbm/ft-h').value, 2.4190883105, rel_tol=1e-4)


def test_surface_tension():
    x = q.SurfaceTension(1)
    assert x.unit.symbol == 'dyne/cm'
    assert x.unit == x.base_unit
    assert isclose(x.to('dyn/cm').value, 1, rel_tol=1e-4)
    assert isclose(x.to('lbf/ft').value, 6.8522e-5, rel_tol=1e-4)


def test_mass_heat_capacity():
    x = q.MassHeatCapacity(1)
    assert x.unit.symbol == 'kJ/kg-C'
    assert x.unit == x.base_unit
    assert isclose(x.to('kJ/g-C').value, 1e-3, rel_tol=1e-4)
    assert isclose(x.to('kJ/g-K').value, 1e-3, rel_tol=1e-4)
    assert isclose(x.to('kJ/kg-K').value, 1, rel_tol=1e-4)
    assert isclose(x.to('J/g-C').value, 1, rel_tol=1e-4)
    assert isclose(x.to('J/g-K').value, 1, rel_tol=1e-4)
    assert isclose(x.to('J/kg-C').value, 1e3, rel_tol=1e-4)
    assert isclose(x.to('J/kg-K').value, 1e3, rel_tol=1e-4)
    assert isclose(x.to('kcal/g-C').value, 0.239006e-3, rel_tol=1e-4)
    assert isclose(x.to('kcal/g-K').value, 0.239006e-3, rel_tol=1e-4)
    assert isclose(x.to('kcal/kg-C').value, 0.239006, rel_tol=1e-4)
    assert isclose(x.to('kcal/kg-K').value, 0.239006, rel_tol=1e-4)
    assert isclose(x.to('cal/g-C').value, 0.239006, rel_tol=1e-4)
    assert isclose(x.to('cal/g-K').value, 0.239006, rel_tol=1e-4)
    assert isclose(x.to('cal/kg-C').value, 0.239006e3, rel_tol=1e-4)
    assert isclose(x.to('cal/kg-K').value, 0.239006e3, rel_tol=1e-4)


def test_mass_entropy():
    x = q.MassEntropy(1)
    assert x.unit.symbol == 'kJ/kg-C'


def test_mass_heat():
    x = q.MassHeat(1)
    assert x.unit.symbol == 'kJ/kg'
    assert x.unit == x.base_unit
    assert isclose(x.to('kJ/g').value, 1e-3, rel_tol=1e-4)
    assert isclose(x.to('J/g').value, 1, rel_tol=1e-4)
    assert isclose(x.to('J/kg').value, 1e3, rel_tol=1e-4)
    assert isclose(x.to('MJ/kg').value, 1e-3, rel_tol=1e-4)
    assert isclose(x.to('kcal/g').value, 0.239006e-3, rel_tol=1e-4)
    assert isclose(x.to('kcal/kg').value, 0.239006, rel_tol=1e-4)
    assert isclose(x.to('cal/g').value, 0.239006, rel_tol=1e-4)
    assert isclose(x.to('cal/kg').value, 0.239006e3, rel_tol=1e-4)
    assert isclose(x.to('Btu/lb').value, 0.429923, rel_tol=1e-4)


def test_standard_gas_flow():
    x = q.StandardGasFlow(1)
    assert x.unit.symbol == 'Sm3/s'
    assert x.unit == x.base_unit
    assert isclose(x.to('Sm3/h').value, 3600, rel_tol=1e-4)
    assert isclose(x.to('Sm3/d').value, 3600 * 24, rel_tol=1e-4)
    assert isclose(x.to('Sm3/min').value, 60, rel_tol=1e-4)


def test_kinematic_viscosity():
    x = q.KinematicViscosity(1)
    assert x.unit.symbol == 'cSt'
    assert x.unit == x.base_unit


def test_molar_volume():
    x = q.MolarVolume(1)
    assert x.unit.symbol == 'm3/kmol'
    assert x.unit == x.base_unit
    assert isclose(x.to('m3/mol').value, 1e-3, rel_tol=1e-4)
    assert isclose(x.to('L/mol').value, 1, rel_tol=1e-4)
    assert isclose(x.to('mL/mol').value, 1e3, rel_tol=1e-4)
    assert isclose(x.to('cm3/mol').value, 1e3, rel_tol=1e-4)


def test_fraction():
    x = q.Fraction(1)
    assert x.unit.symbol == ''
    assert x.unit == x.base_unit
    assert isclose(x.to('%').value, 100, rel_tol=1e-4)
    assert isclose(x.to('ppm').value, 1e6, rel_tol=1e-4)


def test_dimensionless():
    x = q.Dimensionless(1)
    assert x.unit.symbol == ''
    assert x.unit == x.base_unit


def test_operation():
    x = q.Length(1)
    assert x == q.Length(1)
    assert x != q.Length(2)
    assert x < q.Length(2)
    assert x <= q.Length(1)
    assert x == q.Length(1000, 'mm')
    assert q.Length(100, 'cm') == q.Length(1000, 'mm')
    assert q.Length(200, 'cm') != q.Length(1000, 'mm')
    assert q.Length(200, 'cm') >= q.Length(1000, 'mm')
    assert q.Length(1, 'cm') * 100 == q.Length(1, 'm')
    assert 200 * q.Length(1, 'mm') == q.Length(2, 'dm')
