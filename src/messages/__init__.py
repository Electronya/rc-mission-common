import json

class BaseMessage:
    """
    The RC mission base message class.
    """
    SENDER_ID_KEY = 'sender'
    RECEIVER_ID_KEY = 'receiver'
    PAYLOAD_KEY = 'payload'

    COMMADER_ID = 'commander'
    OPERATOR_ID = 'operator'

    def __init__(self, sender=None, receiver=None, payload=None):
        """
        The base message constructor.

        Params:
            sender:     The sender ID. Default: None.
            receiver:   The receiver ID. Default: None.
            payload:    Dictionary representing the message json payload. Default: None.
        """
        self._sender = sender
        self._receiver = receiver
        self._payload = payload

    def set_sender(self, sender):
        """
        Set the sender ID.

        Params:
            sender:     The sender ID.
        """
        self._sender = sender

    def get_sender(self):
        """
        Get the sender ID.

        Return
            The message sender ID.
        """
        return self._sender

    def set_receiver(self, receiver):
        """
        Set the receiver ID.

        Params:
            receiver:   The receiver ID.
        """
        self._receiver = receiver

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

    def set_from_json(self, msg_json):
        """
        Set the message from its json string representation.

        Params:
            msg_json:   The json string containing the message.
        """
        msg = json.loads(msg_json)
        self._sender = msg[self.SENDER_ID_KEY]
        self._receiver = msg[self.RECEIVER_ID_KEY]
        self._payload = msg[self.PAYLOAD_KEY]

    def to_json(self):
        """
        Get the message as a json string.

        Return:
            The message as a json string.
        """
        msg = {}
        msg[self.SENDER_ID_KEY] = self._sender
        msg[self.RECEIVER_ID_KEY] = self._receiver
        msg[self.PAYLOAD_KEY] = self._payload
        return json.dumps(msg)

class ClientStateMessage(BaseMessage):
    """
    The client state message class.
    """
    STATE_KEY = 'state'
    READY_STATE = 'ready'
    BUSY_STATE = 'busy'

    def __init__(self, sender=None, receiver=None, payload=None):
        """
        The client state message constructor.

        Params:
            sender:     The sender ID. Default: None.
            receiver:   The receiver ID. Defaut: None.
            payload:    Dictionary representing the message payload. Default: None.
        """
        super().__init__(sender=sender, receiver=receiver, payload=payload)

    def set_as_busy(self):
        """
        Change the state to busy.
        """
        payload = {}
        payload[self.STATE_KEY] = self.BUSY_STATE
        super().set_payload(payload)

    def set_as_ready(self):
        """
        Change the state to ready.
        """
        payload = {}
        payload[self.STATE_KEY] = self.READY_STATE
        super.set_payload(payload)

    def get_state(self):
        """
        Get the state from the message.

        Return:
            The state of the client contained in the message.
        """
        return super().get_payload()[self.STATE_KEY]

    def is_busy(self):
        """
        Test if the state contained in the message is BUSY.

        Return:
            True if the state is busy, Flase otherwise.
        """
        state = super().get_payload()[self.STATE_KEY]
        return True if state == self.BUSY_STATE else False

    def is_ready(self):
        """
        Test if the state contained in the message is READY.

        Return:
            True if the state is ready, Flase otherwise.
        """
        state = super().get_payload()[self.STATE_KEY]
        return True if state == self.READY_STATE else False
