from typing import List, Literal

from pydantic import BaseModel
from serial import Serial
from serial.tools import list_ports

from .generic_stream import GenericStreamTransport, AsyncGenericStreamTransport
import aioserial


class SerialPortInfo(BaseModel):
    port: str
    description: str
    pid: int | None
    vid: int | None
    serial_number: str | None


def get_serial_ports(pid: str | int | None = None, vid: str | int | None = None) -> List[SerialPortInfo]:
    """Get a list of serial ports

    Args:
        pid (str, optional): Filter by product id. Defaults to None.
        vid (str, optional): Filter by vendor id. Defaults to None.

    Returns:
        List[serial_port_info]: List of serial ports

    """
    if isinstance(pid, str):
        pid = int(pid, 16)
    if isinstance(vid, str):
        vid = int(vid, 16)

    discovered_ports = []
    for port in list_ports.comports():
        # Check if the port should be filtered
        if pid is not None and port.pid != pid:
            continue

        if vid is not None and port.vid != vid:
            continue

        discovered_ports.append(
            SerialPortInfo(
                port=port.device,
                description=port.description,
                pid=port.pid,
                vid=port.vid,
                serial_number=port.serial_number,
            )
        )
    return discovered_ports


class SerialStream(GenericStreamTransport):
    class Config(GenericStreamTransport.Config):
        type: Literal["serial_stream"] = "serial_stream"
        baudrate: int = 115200
        port: str
        rx_buffer_size: int = 16 * 1024
        tx_buffer_size: int = 16 * 1024

    config: Config

    serial: Serial | None = None

    def __init__(self, config: Config):
        super().__init__(config)
        self.config = config

    def init(self):
        super().init()
        self.serial = Serial(port=self.config.port, baudrate=self.config.baudrate)
        self.serial.set_buffer_size(rx_size=self.config.rx_buffer_size, tx_size=self.config.tx_buffer_size)

    def deinit(self):
        if self.serial is not None:
            self.serial.close()

        self.serial = None
        super().deinit()

    def read(self) -> bytes:
        assert self.serial is not None, "Serial port not initialized"

        data = self.serial.read_all()

        if data:
            return data

        return b""

    def write(self, data: bytes):
        assert self.serial is not None, "Serial port not initialized"
        self.serial.write(data)
        self.serial.flush()
