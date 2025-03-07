import sys

import paho.mqtt.client as mqtt


class SyncstateConnectionManager:
    def __init__(self, host:str = "localhost", port:int = 1883, base_topic:str = "/syncstate/"):
        self.host = host
        self.port = port
        self.base_topic = base_topic
        self._mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        self._mqttc.on_connect = self._on_connect
        self._mqttc.on_message = self._on_message
        self._dict = {}

    def _on_connect(self, client: mqtt.Client, userdata, flags: mqtt.ConnectFlags, reason_code: mqtt.ReasonCode, properties:mqtt.Properties):
        if reason_code != "Success":
            raise ConnectionError("failed to connect")
        for key in self._dict.keys():
            client.subscribe(self.base_topic + key)

    def _on_message(self, client: mqtt.Client, data, msg:mqtt.MQTTMessage) -> None:
        key = msg.topic.lstrip(self.base_topic)

        subject_type = type(self._dict[key])
        try:
            self._dict[key] = subject_type(msg.payload.decode())
        except ValueError:
            print(f"Got \"{msg.payload}\" as payload and failed to convert to {subject_type}", file=sys.stderr)
            pass

    def attach(self, dictionary:dict) -> None:
        self._dict = dictionary
        self._mqttc.connect(self.host)
        self._mqttc.loop_start()
