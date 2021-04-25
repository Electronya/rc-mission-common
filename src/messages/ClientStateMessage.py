from src.messages import BaseMessage

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
