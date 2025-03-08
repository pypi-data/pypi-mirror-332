"""Parser for MerryIoT temperature/humidity/CO2 sensor.

Documentation: https://www.merryiot.com/Product/P_1/C_3/V_1.0/RM_MerryIoT%20Air%20Quality%20CO2_20230222%20(BQW_02_0032.009).pdf
"""

import logging
import struct

from ...models import Sensors, Uplink

_LOGGER = logging.getLogger(__name__)


class AirQualityCO2:
    @staticmethod
    def _parse_fport_127(sensors: Sensors, payload: bytes) -> None:
        """Parse payload on FPort 127."""

        status = payload[0]
        sensors.battery_level = (payload[1] + 21) / 10
        sensors.temperature = int.from_bytes(payload[2:4], "little", signed=True) / 10
        sensors.humidity = payload[4] & 0x7F

        if not (status & 0x20):
            sensors.co2 = int.from_bytes(payload[5:], "little")

    @staticmethod
    async def parse_uplink(uplink: Uplink) -> Uplink:
        """Parse binary payload depending on FPort."""
        if uplink.f_port == 127:
            AirQualityCO2._parse_fport_127(uplink.sensors, uplink.payload)
        else:
            _LOGGER.warning('Unknown frame port "%s"', uplink.f_port)

        return uplink
