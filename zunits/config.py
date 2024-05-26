from . import constant

_config = {
    'local_atmospheric_pressure': constant.ATM,
    'standard_temperature': 20
}


def set_standard_temperature(temperature):
    """
    Set standard temperature for standard volume rate conversion,
    default value is 20 degC
    :param temperature: number in 'C'
    :return:
    """
    if isinstance(temperature, (int, float)):
        _config['standard_temperature'] = temperature
    else:
        raise ValueError(f"{temperature} is not a number.")


def get_standard_temperature():
    return _config['standard_temperature']


def set_local_atmospheric_pressure(pressure):
    """
    Set local atmospheric pressure for gauge pressure conversion,
    default value is 101325 Pa
    :param pressure: number in 'Pa'
    :return:
    """
    if isinstance(pressure, (int, float)):
        value = pressure
    else:
        raise ValueError(f"{pressure} is not a number.")
    _config['local_atmospheric_pressure'] = value


def get_local_atmospheric_pressure():
    return _config['local_atmospheric_pressure']
