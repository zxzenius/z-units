from __future__ import annotations
from collections import namedtuple

from z_units.constant import ATM

STP = namedtuple('STP', ['temperature', 'pressure'])


class Environment:
    """Global environment parameters"""
    def __init__(self):
        self.reset()
    
    def reset(self):
        """Reset environment parameters"""
        self._atmospheric_pressure = ATM
        self._standard_temperature = 293.15 # 20 degC
        self._standard_pressure = ATM

    @property
    def atmospheric_pressure(self) -> float:
        """Atmospheric pressure in Pa"""
        return self._atmospheric_pressure

    @atmospheric_pressure.setter
    def atmospheric_pressure(self, value: float):
        """Atmospheric pressure in Pa"""
        if value <= 0:
            raise ValueError("Atmospheric pressure shall be positive")
        self._atmospheric_pressure = value

    @property
    def stp(self) -> STP:
        """Standard temperature in K and pressure in Pa"""
        return STP(self.standard_temperature, self.standard_pressure)
    
    @property
    def standard_condition(self) -> STP:
        return self.stp
    
    @property
    def standard_temperature(self) -> float:
        """Standard temperature in K"""
        return self._standard_temperature
    
    @standard_temperature.setter
    def standard_temperature(self, value: float):
        """Standard temperature in K"""
        if value <= 0:
            raise ValueError("Standard temperature shall be positive")
        self._standard_temperature = value
    
    @property
    def standard_pressure(self) -> float:
        """Standard pressure in Pa"""
        return self._standard_pressure
    
    @standard_pressure.setter
    def standard_pressure(self, value: float):
        """Standard pressure in Pa"""
        if value <= 0:
            raise ValueError("Standard pressure shall be positive")
        self._standard_pressure = value
    
    def set_stp(self, *, temperature: float = 273.15, pressure: float = ATM):
        """Set standard temperature in K and pressure in Pa"""
        self.standard_temperature = temperature
        self.standard_pressure = pressure


# Global environment instance
_default_env = Environment()

def get_env() -> Environment:
    """Get the global environment instance"""
    return _default_env