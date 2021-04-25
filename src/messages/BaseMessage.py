import json

class RcMissionBaseMessage:
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
