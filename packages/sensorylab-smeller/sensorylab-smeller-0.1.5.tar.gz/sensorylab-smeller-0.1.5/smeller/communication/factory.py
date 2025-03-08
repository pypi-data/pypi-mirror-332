# communication/factory.py
from communication.base import CommunicationInterface
from communication.serial_com import SerialCommunication
from communication.bluetooth_com import BluetoothCommunication  # Импортируем новую реализацию
from config import DeviceConfig
from utils.manager import COMPortManager  # Убедись в правильности импорта
from typing import Optional

def create_communication(config: DeviceConfig, connection_type: str, port_manager: Optional[COMPortManager] = None) -> CommunicationInterface:
    if connection_type == "serial":
        return SerialCommunication(config, port_manager)
    elif connection_type == "bluetooth":
        return BluetoothCommunication(config, port_manager) #Добавляем блютуз
    else:
        raise ValueError(f"Invalid connection type: {connection_type}")