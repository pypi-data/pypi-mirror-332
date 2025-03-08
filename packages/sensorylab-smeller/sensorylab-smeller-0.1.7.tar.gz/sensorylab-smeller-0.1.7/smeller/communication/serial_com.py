# neuroairAPI/communication/serial_com.py
import asyncio
import logging
from typing import List, Optional
import sys
from pathlib import Path

# Добавляем директорию, содержащую neuroairAPI, в sys.path
project_root = Path(__file__).resolve().parents[1]  # Поднимаемся на два уровня вверх
sys.path.append(str(project_root))
project_root = Path(__file__).resolve().parents[3]  # Поднимаемся на два уровня вверх
sys.path.append(str(project_root))

import serial
import serial.tools.list_ports

from smeller.communication.base import CommunicationInterface
from smeller.config import DeviceConfig  # Исправленный импорт
from smeller.utils.manager import COMPortManager

logger = logging.getLogger(__name__)

class SerialCommunication(CommunicationInterface):


    def __init__(self, config: DeviceConfig, port_manager=None):

        self.config = config
        print('LOL')
        self.connection: Optional[serial.Serial] = None
        self._running = False
        if port_manager is None:
            self.port_manager = COMPortManager()
        else:
            self.port_manager = port_manager
    async def connect(self, com_port: Optional[str] = None, **kwargs) -> bool:
        """
        Establishes a serial connection.
                :param com_port:
        """
        if not com_port:
            com_ports = self.port_manager.get_com_ports()
            if not com_ports:
                logger.error("No COM ports found.")
                return False
            com_port = com_ports[0].device  # Выбираем первый доступный порт

        try:
            self.connection = serial.Serial(
                port=com_port,
                baudrate=self.config.baudrate,
                timeout=self.config.timeout
            )
            self._running = True
            logger.info(f"Connected to {com_port}")
            return True

        except serial.SerialException as e:
            logger.error(f"Connection error: {e}")
            return False
    async def disconnect(self) -> None:
        """Closes the serial connection."""
        self._running = False
        if self.connection and self.connection.is_open:
            self.connection.close()
            logger.info("Connection closed")
    async def send_command(self, command_str: str) -> Optional[List[str]]:
        if not self.connection or not self.connection.is_open:
            logger.warning("No active connection")
            return None

        try:
            # Очистка буферов перед отправкой
            self.connection.reset_input_buffer()
            self.connection.reset_output_buffer()

            # Отправка команды
            full_command = f"{command_str.strip()}{self.config.command_terminator}"
            self.connection.write(full_command.encode())
            return await self.read_response()  # Исправленное имя метода
        except Exception as e:
            logger.error(f"Command failed: {e}")
            return None
    async def read_response(self, timeout: float = 3.0, inter_byte_timeout: float = 0.5) -> list[str]:  # Исправленное имя метода
        """Читает все данные до достижения таймаута между байтами"""
        buffer = []
        loop = asyncio.get_running_loop()
        last_byte_time = loop.time()

        try:
            while True:
                # Читаем все доступные байты
                data = await loop.run_in_executor(
                    None,
                    lambda: self.connection.read(self.connection.in_waiting or 1)
                )

                if data:
                    buffer.append(data.decode(errors="replace"))
                    last_byte_time = loop.time()

                # Проверяем таймаут между байтами
                if (loop.time() - last_byte_time) >= inter_byte_timeout:
                    break

                await asyncio.sleep(0)

        except (serial.SerialException, asyncio.CancelledError) as e:
            logger.error(f"Read error: {e}")
            return []

        full_response = "".join(buffer)
        return [line.strip() for line in full_response.splitlines() if line.strip()]