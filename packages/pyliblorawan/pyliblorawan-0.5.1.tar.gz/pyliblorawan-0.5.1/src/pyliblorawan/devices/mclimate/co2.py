"""Parser for MClimate CO2/temperature/humidity sensor.

Documentation: https://docs.mclimate.eu/mclimate-lorawan-devices/devices/mclimate-co2-sensor-and-notifier-lorawan
"""

import logging

from ...models import Sensors, Uplink

_LOGGER = logging.getLogger(__name__)


class CommandTypes:
    KEEP_ALIVE = 1


class CO2:
    @staticmethod
    def _parse_keep_alive(sensors: Sensors, payload: bytes) -> None:
        """Parse keep alive uplink"""
        sensors.co2 = int.from_bytes(payload[0:2], "big")
        sensors.temperature = (int.from_bytes(payload[2:4], "big") - 400) / 10
        sensors.humidity = round(payload[4] * 100 / 256, 1)
        sensors.battery_level = (payload[5] * 8 + 1600) / 1000

    @staticmethod
    def _parse_fport_2(sensors: Sensors, payload: bytes) -> None:
        """Parse payload on FPort 2."""

        if payload[0] == CommandTypes.KEEP_ALIVE:
            CO2._parse_keep_alive(sensors, payload[1:])
        else:
            _LOGGER.warning('Unknown command type "%s"', payload[0])

    @staticmethod
    async def parse_uplink(uplink: Uplink) -> Uplink:
        """Parse binary payload depending on FPort."""
        if uplink.f_port == 2:
            CO2._parse_fport_2(uplink.sensors, uplink.payload)
        else:
            _LOGGER.warning('Unknown frame port "%s"', uplink.f_port)

        return uplink
