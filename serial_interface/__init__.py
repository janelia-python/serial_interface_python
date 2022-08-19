'''
Extends serial.Serial to add methods such as auto discovery of available serial ports in Linux, Windows, and Mac OS X.
'''

# __init__.py is generated automatically from .single-source-of-truth.org
# File edits may be overwritten!
from serial_interface.__about__ import (
    __author__,
    __copyright__,
    __email__,
    __license__,
    __description__,
    __url__,
    __version__,
)

from .serial_interface import SerialInterface, SerialInterfaces, find_serial_interface_ports, find_serial_interface_port, WriteFrequencyError, WriteError, ReadError, __version__
