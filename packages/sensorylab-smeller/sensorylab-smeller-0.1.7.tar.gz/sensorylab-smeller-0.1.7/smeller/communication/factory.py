# communication/factory.py
from smeller.communication.base import CommunicationInterface
from smeller.communication.serial_com import SerialCommunication
from smeller.communication.bluetooth_com import BluetoothCommunication  # Импортируем новую реализацию
from smeller.config import DeviceConfig
from smeller.utils.manager import COMPortManager  # Убедись в правильности импорта
from typing import Optional

def create_communication(config: DeviceConfig, connection_type: str, port_manager: Optional[COMPortManager] = None) -> CommunicationInterface:
    if connection_type == "serial":
        return SerialCommunication(config, port_manager)
    elif connection_type == "bluetooth":
        return BluetoothCommunication(config, port_manager) #Добавляем блютуз
    else:
        raise ValueError(f"Invalid connection type: {connection_type}")