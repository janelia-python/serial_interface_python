<!-- README.md is generated automatically from .single-source-of-truth.org
    File edits may be overwritten! -->


# About

```markdown
- Name: serial_interface
- Version: 2.3.0
- Description: Extends pyserial Serial to add convenience methods.
- License: BSD 3-Clause License
- URL: https://github.com/janelia-pypi/serial_interface_python
- Author: Peter Polidoro
- Email: peter@polidoro.io
- Copyright: 2022 Howard Hughes Medical Institute
- Dependencies:
  - pyserial
```


# Example Usage


## Python

```python
from serial_interface import SerialInterface, find_serial_interface_ports
find_serial_interface_ports() # Returns list of available serial ports

dev = SerialInterface() # Might automatically find device if one available

# if it is not found automatically, specify port directly
dev = SerialInterface(port='/dev/ttyUSB0') # Linux
dev = SerialInterface(port='/dev/tty.usbmodem262471') # Mac OS X
dev = SerialInterface(port='COM3') # Windows

dev.get_device_info()

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


# Installation

<https://github.com/janelia-pypi/python_setup>


## Linux


### udev rules

[99-platformio-udev.rules](https://docs.platformio.org/en/stable/core/installation/udev-rules.html)

```sh
# Recommended
curl -fsSL https://raw.githubusercontent.com/platformio/platformio-core/master/scripts/99-platformio-udev.rules | sudo tee /etc/udev/rules.d/99-platformio-udev.rules

# OR, manually download and copy this file to destination folder
sudo cp 99-platformio-udev.rules /etc/udev/rules.d/99-platformio-udev.rules

# Restart udev management tool
sudo service udev restart

# or
sudo udevadm control --reload-rules
sudo udevadm trigger

# Ubuntu/Debian users may need to add own “username” to the “dialout” group
sudo usermod -a -G dialout $USER
sudo usermod -a -G plugdev $USER
```


### pip

```sh
python3 -m venv ~/venvs/serial_interface
source ~/venvs/serial_interface/bin/activate
pip install serial_interface
```


### guix

Setup guix-janelia channel:

<https://github.com/guix-janelia/guix-janelia>

```sh
guix install python-serial-interface
```


## Windows


### pip

```sh
python3 -m venv C:\venvs\serial_interface
C:\venvs\serial_interface\Scripts\activate
pip install serial_interface
```


# Development

[DEVELOPMENT.md](./DEVELOPMENT.md)