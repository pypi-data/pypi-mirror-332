# neuroairAPI/utils/utils.py

import asyncio
import re, time
import json
import subprocess
import logging
from typing import List, Optional, Tuple, NamedTuple, Any
import serial
import bluetooth as bt
import serial.tools.list_ports

logging.basicConfig(
    level=logging.DEBUG,  # Понижаем уровень до DEBUG
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("device_debug.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Типовые константы
DEFAULT_CACHE_TIMEOUT = 5 # Уменьшил таймаут кеширования

class ListPortInfo(NamedTuple):
    device: str
    name: Optional[str]
    description: Optional[str]
    hwid: Optional[str]
    vid: Optional[int]
    pid: Optional[int]
    serial_number: Optional[str]
    location: Optional[str]
    manufacturer: Optional[str]
    product: Optional[str]
    interface: Optional[str]
    
class COMPortManager:
    
    def __init__(self, cache_timeout: float = DEFAULT_CACHE_TIMEOUT):
        self._ports_cache = None
        self._last_update = 0
        self.cache_timeout = cache_timeout  # seconds

    def get_com_ports(self, refresh=False) -> List[ListPortInfo]:
        logger.debug(f"Getting COM ports (refresh={refresh})...")
        
        if not refresh and self._ports_cache and (time.time() - self._last_update) < self.cache_timeout:
            logger.debug("Returning cached COM ports")
            return self._ports_cache

        logger.debug("Refreshing COM ports list")
        try:
            self._ports_cache: List[ListPortInfo] = list(serial.tools.list_ports.comports())
            self._last_update = time.time()
            
            logger.debug(f"Found {len(self._ports_cache)} ports: {[p.device for p in self._ports_cache]}")
            return self._ports_cache
        except serial.SerialException as e: # Улучшение: обрабатываем исключения
            logger.error(f"Error getting COM port list: {e}", exc_info=True)
            self._ports_cache = [] # Сбрасываем кэш при ошибке
            self._last_update = 0
            return []
        
    def filter_bluetooth_ports(self, ports: List[ListPortInfo]) -> List[ListPortInfo]:
        logger.warning("Filtering Bluetooth ports based on description keywords. This method might not be reliable on all systems.")
        return [
        port for port in ports
            if port.description and any( # Добавлена проверка на None
                    keyword in port.description.upper()
                    for keyword in {"BLUETOOTH", "BTHENUM"}
            )
        ]
    def extract_mac_from_port(self, port: Any) -> Optional[str]:
        logger.debug(f"Extracting MAC from port: {port}")
        
        if not port.hwid:
            logger.debug("No hwid available")
            return None
            
        logger.debug(f"Processing hwid: {port.hwid}")
        match = re.search(r"&([0-9A-F]{12})", port.hwid.upper())
        if match:
            mac_str = match.group(1)
            formatted_mac = ":".join(mac_str[i:i+2] for i in range(0, 12, 2))
            logger.debug(f"Formatted MAC: {formatted_mac}")
            return formatted_mac
            
        logger.debug("No MAC found in hwid")
        return None