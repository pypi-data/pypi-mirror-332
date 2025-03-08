"""Parser for Browan TBMS100 PIR sensor."""
import logging

from ...models import Sensors, Uplink

_LOGGER = logging.getLogger(__name__)


class TBHH100:
    @staticmethod
    def _parse_payload_tbhh100_107(sensors: Sensors, payload: bytes) -> None:
        """Parse payload on FPort 107."""
        voc_sensor = True if payload[0] == 0 else False
        sensors.battery_level = (25 + (payload[1] & 0x0F)) / 10
        sensors.temperature = (payload[2] & 0x7F) - 32
        sensors.humidity = payload[3] & 0x7F

        # VOC sensor only installed on TBHV110
        if voc_sensor:
            _LOGGER.error(
                'TBHH100 parse does not implement CO2eq/VOC. Received payload "%s"',
                format(payload.hex()),
            )

    @staticmethod
    async def parse_uplink(uplink: Uplink) -> Uplink:
        """Parse binary payload depending on FPort."""
        if uplink.f_port == 107:
            TBHH100._parse_payload_tbhh100_107(uplink.sensors, uplink.payload)
        else:
            _LOGGER.warning('Unknown frame port "%s"', uplink.f_port)

        return uplink
