# neuroairAPI/config.py
from dataclasses import dataclass, field
from typing import List

@dataclass
class DeviceConfig:
    """
    Configuration for the NeuroAir device.
    """
    baudrate: int = 115200
    timeout: float = 2.0
    command_terminator: str = "\n"
    ping_interval: int = 10
    discovery_duration: int = 4
    