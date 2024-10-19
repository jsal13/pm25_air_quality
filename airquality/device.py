"""Adapted from https://github.com/adafruit/Adafruit_CircuitPython_PM25/blob/f5e374c3d7e2d675b29c030b70a49f5c2d1effd3/examples/pm25_simpletest.py."""

from typing import Any

import board
import busio
from adafruit_pm25.i2c import PM25_I2C


def device_setup() -> 'PM25_I2C':
    """Set up PM Device."""
    # GPIO connects to a reset pin (TODO: ??)
    reset_pin: Any = None
    # reset_pin = DigitalInOut(board.G0)
    # reset_pin.direction = Direction.OUTPUT
    # reset_pin.value = False
    # uart: serial.Serial = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=0.25)

    i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)
    return PM25_I2C(i2c, reset_pin)

def read_data(pm25_i2c: PM25_I2C) -> dict[str, int]:
    """Read data from the PM25, return dict of values."""
    air_quality_data: dict[str, int] = None

    try:
        air_quality_data = pm25_i2c.read()
    except RuntimeError as error:
        print("Could not read from sensor.")
        raise (error)

    return air_quality_data
