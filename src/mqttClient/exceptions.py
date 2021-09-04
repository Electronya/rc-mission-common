class MqttClientNotInit(Exception):
    """
    The MQTT client not initialized exception.
    """
    def __init__(self) -> None:
        super().__init__('MQTT client not initialized.')
