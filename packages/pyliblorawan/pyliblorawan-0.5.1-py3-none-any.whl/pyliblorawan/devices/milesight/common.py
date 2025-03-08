import logging

from ...models import Sensors

_LOGGER = logging.getLogger(__name__)


class Decoders:
    def __init__(self, sensors: Sensors):
        self._sensors = sensors

    def battery(self, data: bytearray) -> bytes:
        self._sensors.battery = data[0]
        return data[1:]

    def humidity(self, data: bytearray):
        self._sensors.humidity = int.from_bytes(data[0:1], "little") / 2
        return data[1:]

    def temperature(self, data: bytearray):
        self._sensors.temperature = (
            int.from_bytes(data[0:2], "little", signed=True) / 10
        )
        return data[2:]


class Milesight:
    def __init__(self, sensors: Sensors):
        self.converters = Decoders(sensors)

    class channels:
        BATTERY = 0x01
        TEMPERATURE = 0x03
        HUMIDITY = 0x04

    class channel_battery:
        BATTERY = 0x75

    class channel_humidity:
        HUMIDITY = 0x68

    class channel_temperature:
        TEMPERATURE = 0x67

    def data_types(self):
        return {
            self.channels.BATTERY: {
                self.channel_battery.BATTERY: self.converters.battery,
            },
            self.channels.HUMIDITY: {
                self.channel_humidity.HUMIDITY: self.converters.humidity,
            },
            self.channels.TEMPERATURE: {
                self.channel_temperature.TEMPERATURE: self.converters.temperature,
            },
        }


def parse_fport_85(sensors: Sensors, payload: bytes) -> None:
    decoder = Milesight(sensors)

    while len(payload) > 2:
        channel_id = payload[0]
        data_type = payload[1]

        try:
            converter = decoder.data_types()[channel_id][data_type]
            payload = converter(payload[2:])

        except KeyError:
            _LOGGER.warning(
                f'Unknown channel - id: "0x{channel_id:02X}" - type: "0x{data_type:02X}"'
            )
            return
