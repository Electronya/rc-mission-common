import json

class BaseMessage:
    """
    The RC mission base message class.
    """
    UNIT_ID_KEY = 'unit id'
    PAYLOAD_KEY = 'payload'

    def __init__(self, topic_root, unit, payload=None, qos=0):
        """
        The base message constructor.

        Params:
            topic_root: The message topic root.
            unit:       The unit ID.
            payload:    Dictionary representing the message json payload. Default: None.
            qos:        The message quality of service. Default: 0.
        """
        self._unit = unit
        self._payload = payload
        self._qos = qos
        self._topic = f"{topic_root}/{unit}"

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

class UnitConnectionState(BaseMessage):
    """
    The client state message class.
    """
    STATE_KEY = 'state'
    ONLINE_STATE = 'online'
    OFFLINE_STATE = 'offline'
    TOPIC_ROOT = 'units/connectionState'
    QOS = 1

    def __init__(self, unit=None, payload=None):
        """
        The client state message constructor.

        Params:
            unit:       The unit ID. Default: None.
            payload:    Dictionary representing the message payload. Default: None.
        """
        super().__init__(self.TOPIC_ROOT, unit, payload=payload, qos=self.QOS)

    def set_as_offline(self):
        """
        Change the state to offline.
        """
        payload = {}
        payload[self.STATE_KEY] = self.OFFLINE_STATE
        super().set_payload(payload)

    def set_as_online(self):
        """
        Change the state to online.
        """
        payload = {}
        payload[self.STATE_KEY] = self.ONLINE_STATE
        super.set_payload(payload)

    def get_state(self):
        """
        Get the state from the message.

        Return:
            The state of the client contained in the message.
        """
        return super().get_payload()[self.STATE_KEY]

    def is_offline(self):
        """
        Test if the state contained in the message is ONLINE.

        Return:
            True if the state is online, Flase otherwise.
        """
        state = super().get_payload()[self.STATE_KEY]
        return True if state == self.OFFLINE_STATE else False

    def is_online(self):
        """
        Test if the state contained in the message is ONLINE.

        Return:
            True if the state is online, Flase otherwise.
        """
        state = super().get_payload()[self.STATE_KEY]
        return True if state == self.ONLINE_STATE else False
