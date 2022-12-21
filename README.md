- [About](#org764f462)
- [Example Usage](#orgc15df8a)
- [Installation](#orgbd91757)
- [Development](#org2a2493c)

    <!-- This file is generated automatically from .metadata.org -->
    <!-- File edits may be overwritten! -->


<a id="org764f462"></a>

# About

```markdown
- Name: serial_interface
- Description: Extends pyserial to make serial device interfaces.
- Version: 2.3.1
- Release Date: 2022-12-21
- Creation Date: 2018-01-11
- License: BSD-3-Clause
- URL: https://github.com/janelia-pypi/serial_interface_python
- Author: Peter Polidoro
- Email: peter@polidoro.io
- Copyright: 2022 Howard Hughes Medical Institute
- References:
  - https://pyserial.readthedocs.io
- Dependencies:
  - pyserial
```


<a id="orgc15df8a"></a>

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


## Command Line

```sh

```


<a id="orgbd91757"></a>

# Installation

<https://github.com/janelia-pypi/python_setup>


## GNU/Linux


### Drivers

GNU/Linux computers usually have all of the necessary drivers already installed, but users need the appropriate permissions to open the device and communicate with it.

Udev is the GNU/Linux subsystem that detects when things are plugged into your computer.

Udev may be used to detect when a serial device is plugged into the computer and automatically give permission to open that device.

If you plug a sensor into your computer and attempt to open it and get an error such as: "FATAL: cannot open /dev/ttyUSB0: Permission denied", then you need to install udev rules to give permission to open that device.

Udev rules may be downloaded as a file and placed in the appropriate directory using these instructions:

[99-platformio-udev.rules](https://docs.platformio.org/en/stable/core/installation/udev-rules.html)

1.  Download rules into the correct directory

    ```sh
    curl -fsSL https://raw.githubusercontent.com/platformio/platformio-core/master/scripts/99-platformio-udev.rules | sudo tee /etc/udev/rules.d/99-platformio-udev.rules
    ```

2.  Restart udev management tool

    ```sh
    sudo service udev restart
    ```

3.  Ubuntu/Debian users may need to add own “username” to the “dialout” group

    ```sh
    sudo usermod -a -G dialout $USER
    sudo usermod -a -G plugdev $USER
    ```

4.  After setting up rules and groups

    You will need to log out and log back in again (or reboot) for the user group changes to take effect.
    
    After this file is installed, physically unplug and reconnect your board.


### Python Code

The Python code in this library may be installed in any number of ways, chose one.

1.  pip

    ```sh
    python3 -m venv ~/venvs/serial_interface
    source ~/venvs/serial_interface/bin/activate
    pip install serial_interface
    ```

2.  guix

    Setup guix-janelia channel:
    
    <https://github.com/guix-janelia/guix-janelia>
    
    ```sh
    guix install python-serial-interface
    ```


## Windows


### Drivers

Download and install driver for the specific serial device.


### Python Code

The Python code in this library may be installed in any number of ways, chose one.

1.  pip

    ```sh
    python3 -m venv C:\venvs\serial_interface
    C:\venvs\serial_interface\Scripts\activate
    pip install serial_interface
    ```


<a id="org2a2493c"></a>

# Development


## Install Guix

[Install Guix](https://guix.gnu.org/manual/en/html_node/Binary-Installation.html)


## Clone Repository

```sh
git clone https://github.com/janelia-pypi/serial_interface_python
cd serial_interface_python
```


## Edit .metadata.org

```sh
make metadata-edits
```


## Tangle .metadata.org

```sh
make metadata
```


## Test Python package using ipython shell

```sh
make ipython-shell # PORT=/dev/ttyUSB0
# make PORT=/dev/ttyUSB1 ipython-shell
import serial_interface
exit
```


## Test installation of Guix package

```sh
make installed-shell # PORT=/dev/ttyUSB0
# make PORT=/dev/ttyUSB1 installed-shell
exit
```


## Upload Python package to pypi

```sh
make upload
```


## Test direct device interaction using serial terminal

```sh
make serial-shell # PORT=/dev/ttyUSB0
# make PORT=/dev/ttyUSB1 serial-shell
? # help
settings
[C-a][C-x] # to exit
```