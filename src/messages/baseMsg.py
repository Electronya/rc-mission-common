import json


class BaseMessage:
    """
    The RC mission base message class.
    """
    UNIT_ID_KEY = 'unit id'
    PAYLOAD_KEY = 'payload'

    def __init__(self, topic, unit, payload=None, qos=0, retain=False):
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

    def get_topic(self):
        """
        Get the message topic.

        Return:
            The message topic.
        """
        return self._topic

    def get_unit(self):
        """
        Get the unit ID.

        Return:
            The message unit ID.
        """
        return self._unit

    def set_payload(self, payload):
        """
        Set the payload of the message.

        Params:
            payload:    Dictionary representing the new message json payload.
        """
        self._payload = payload

    def get_payload(self):
        """
        Get the payload of the message.

        Return:
            Dictionary representing the message json payload.
        """
        return self._payload

    def set_qos(self, qos):
        """
        Set the message quality of service.

        Params:
            qos:        The message quality of service.
        """
        self._qos = qos

    def get_qos(self):
        """
        Get the message quality of service.

        Return:
            The message quality of service.
        """
        return self._qos

    def set_retain(self, retain):
        """
        Set the message retain flag.

        Params:
            retain:     The retention flag.
        """
        self._retain = retain

    def get_retain(self):
        """
        Get the message retention flag.

        Return:
            The message retention flag.
        """
        return self._retain

    def set_from_json(self, msg_json):
        """
        Set the message from its json string representation.

        Params:
            msg_json:   The json string containing the message.
        """
        msg = json.loads(msg_json)
        self._unit = msg[self.UNIT_ID_KEY]
        self._payload = msg[self.PAYLOAD_KEY]

    def to_json(self):
        """
        Get the message as a json string.

        Return:
            The message as a json string.
        """
        msg = {}
        msg[self.UNIT_ID_KEY] = self._unit
        msg[self.PAYLOAD_KEY] = self._payload
        return json.dumps(msg)
