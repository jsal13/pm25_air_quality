# airquality

## Description

A script that will allow for reading and streaming from PM-25 attached to a Raspberry Pi.

## Quickstart

```shell
pip3 install just
just venv
. .venv/bin/activate
python airquality/main.py
```

## Testing

Use the docker image at: <https://github.com/ptrsr/pi-ci>

On Docker...

```shell
pip3 install adafruit-python-shell adafruit-circuitpython-pm25
```