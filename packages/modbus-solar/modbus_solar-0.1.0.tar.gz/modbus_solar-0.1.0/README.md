# Modbus Solar

[![pypi](https://img.shields.io/pypi/v/modbus-solar.svg)](https://pypi.org/project/modbus-solar/)
[![python](https://img.shields.io/pypi/pyversions/modbus-solar.svg)](https://pypi.org/project/modbus-solar/)
[![built with nix](https://builtwithnix.org/badge.svg)](https://builtwithnix.org)

This project is to pull stats out of a Renogy DCC50S solar charge controller.

The connection will be made via modbus/RS485.

The end state will be to output stats in `json` format ready to be ingested into something like an InfluxDb instance.


## To Use

1. Python

    ```python
    from modbus_solar import get_all

    stats = get_all()
    ```

1. CLI
    ```bash
    modbus-solar-get-all
    ```
