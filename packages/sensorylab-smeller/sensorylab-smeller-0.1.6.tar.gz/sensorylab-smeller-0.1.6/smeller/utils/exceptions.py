class DeviceError(Exception):
    """Base class for device-related errors."""
    pass

class CommunicationError(DeviceError):
    """Raised when there is a problem communicating with the device."""
    pass

class ConnectionError(CommunicationError):
    """Raised when the connection to the device fails."""
    pass

class CommandError(DeviceError):
    """Raised when a command fails to execute."""
    pass

class InvalidResponseError(DeviceError):
    """Raised when the device returns an invalid response."""
    pass