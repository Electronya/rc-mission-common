import json


class BaseMessage:
    """
    The RC mission base message class.
    """
    UNIT_ID_KEY = 'unit id'
    PAYLOAD_KEY = 'payload'

    def __init__(self, topic: str, unit: str, payload: dict = None,
                 qos: int = 0, retain: bool = False) -> None:
        """
        The base message constructor.

        Params:
            topic:      The message topic.
            unit:       The unit ID.
            payload:    Dictionary representing the message json payload.
                        Default: None.
            qos:        The message quality of service. Default: 0.
            retain:     The retention flag. Default: False
        """
        self._unit = unit
        self._payload = payload
        self._qos = qos
        self._topic = topic
        self._retain = retain

    def getTopic(self) -> str:
        """
        Get the message topic.

        Return:
            The message topic.
        """
        return self._topic

    def getUnit(self) -> str:
        """
        Get the unit ID.

        Return:
            The message unit ID.
        """
        return self._unit

    def setPayload(self, payload: dict) -> None:
        """
        Set the payload of the message.

        Params:
            payload:    Dictionary representing the new message json payload.
        """
        self._payload = payload

    def getPayload(self) -> dict:
        """
        Get the payload of the message.

        Return:
            Dictionary representing the message json payload.
        """
        return self._payload

    def setQos(self, qos: int) -> None:
        """
        Set the message quality of service.

        Params:
            qos:        The message quality of service.
        """
        self._qos = qos

    def getQos(self) -> int:
        """
        Get the message quality of service.

        Return:
            The message quality of service.
        """
        return self._qos

    def setRetain(self, retain: bool) -> None:
        """
        Set the message retain flag.

        Params:
            retain:     The retention flag.
        """
        self._retain = retain

    def getRetain(self) -> bool:
        """
        Get the message retention flag.

        Return:
            The message retention flag.
        """
        return self._retain

    def fromJson(self, msgJson: str) -> None:
        """
        Set the message from its json string representation.

        Params:
            msgJson:    The json string containing the message.
        """
        msg = json.loads(msgJson)
        self._unit = msg[self.UNIT_ID_KEY]
        self._payload = msg[self.PAYLOAD_KEY]

    def toJson(self) -> str:
        """
        Get the message as a json string.

        Return:
            The message as a json string.
        """
        msg = {}
        msg[self.UNIT_ID_KEY] = self._unit
        msg[self.PAYLOAD_KEY] = self._payload
        return json.dumps(msg)
