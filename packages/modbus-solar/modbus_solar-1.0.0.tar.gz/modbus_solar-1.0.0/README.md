# Modbus Solar

[![pypi](https://img.shields.io/pypi/v/modbus-solar.svg)](https://pypi.org/project/modbus-solar/)
[![python](https://img.shields.io/pypi/pyversions/modbus-solar.svg)](https://pypi.org/project/modbus-solar/)
[![built with nix](https://builtwithnix.org/badge.svg)](https://builtwithnix.org)

## Intro

This project is to pull stats out of a Renogy DCC50S solar charge controller.

The connection will be made via Modbus/RS485.

The end state will be to output stats in `json` format ready to be ingested into something like an InfluxDb instance or to publish to a MQTT Topic.

## Pre-Reqs

You require a Modbus/RS485 connector, most probably will be a USB varient. Most applications will be using a small IoT device or Raspberry Pi to serve the USB device and then connect back to a logging system of some sort.

The Modbus parameters are hard coded but variabalised for the device ID and the salve address which could change.

## Using

### To install

```bash
pip install modbus-solar
```

### To Use

1. `Python`

    ```python
    from modbus_solar import get_all

    stats = get_all()
    print(stats)
    ```

1. `bash`

    ```bash
    modbus-solar-get-all
    ```
