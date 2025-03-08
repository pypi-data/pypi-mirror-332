"""Parser for Milesight EM300-TH: temperature/humidity sensor.

Documentation: https://resource.milesight.com/milesight/iot/document/em300-series-user-guide-en.pdf
"""

import logging

from ...models import Uplink
from .common import parse_fport_85

_LOGGER = logging.getLogger(__name__)


class EM300TH:
    @staticmethod
    async def parse_uplink(uplink: Uplink) -> Uplink:
        """Parse binary payload depending on FPort."""
        if uplink.f_port == 85:
            parse_fport_85(uplink.sensors, uplink.payload)
        else:
            _LOGGER.warning('Unknown frame port "%s"', uplink.f_port)

        return uplink
