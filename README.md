# serial_interface_python

This Python package (serial_interface) creates a class named
SerialInterface, which inherits from serial.Serial and adds methods to
it, like auto discovery of available serial ports in Linux, Windows,
and Mac OS X. The SerialInterface class can be used by itself, but it is
mostly intended to be a base class for other serial port devices with
higher level functions. SerialInterfaces creates a list of SerialInterface
instances from all available serial ports.

Authors:

    Peter Polidoro <polidorop@janelia.hhmi.org>

Contributors:

    James Pells <https://github.com/jpells>
    Roger Zatkoff <https://github.com/rpzatkoff>

License:

    BSD

## Example Usage


```python
from serial_interface import SerialInterface, find_serial_interface_ports
find_serial_interface_ports() # Returns list of available serial ports
dev = SerialInterface() # Might automatically find device if one available
# if it is not found automatically, specify port directly
dev = SerialInterface(port='/dev/ttyUSB0') # Linux
dev = SerialInterface(port='/dev/tty.usbmodem262471') # Mac OS X
dev = SerialInterface(port='COM3') # Windows
dev.get_device_info()
```

```python
from serial_interface import SerialInterfaces
devs = SerialInterfaces()  # Might automatically find all available devices
# if they are not found automatically, specify ports to use
devs = SerialInterfaces(use_ports=['/dev/ttyUSB0','/dev/ttyUSB1']) # Linux
devs = SerialInterfaces(use_ports=['/dev/tty.usbmodem262471','/dev/tty.usbmodem262472']) # Mac OS X
devs = SerialInterfaces(use_ports=['COM3','COM4']) # Windows
devs.get_devices_info()
devs.sort_by_port()
dev = devs[0]
dev.get_device_info()
```

## Installation

[Setup Python](https://github.com/janelia-pypi/python_setup)

### Linux and Mac OS X

```shell
mkdir -p ~/virtualenvs/serial_interface
virtualenv ~/virtualenvs/serial_interface
#Python3
virtualenv -p python3 ~/virtualenvs/serial_interface
source ~/virtualenvs/serial_interface/bin/activate
pip install serial_interface
```

### Windows

```shell
virtualenv C:\virtualenvs\serial_interface
C:\virtualenvs\serial_interface\Scripts\activate
pip install serial_interface
```
