from .baseMsg import BaseMessage


class UnitConnectionState(BaseMessage):
    """
    The client state message class.
    """
    STATE_KEY = 'state'
    ONLINE_STATE = 'online'
    OFFLINE_STATE = 'offline'
    TOPIC_ROOT = 'units/connectionState'
    QOS = 1

    def __init__(self, unit, payload=None):
        """
        The client state message constructor.

        Params:
            unit:       The unit ID.
            payload:    Dictionary representing the message payload.
                        Default: None.
        """
        super().__init__(f"{self.TOPIC_ROOT}/{unit}", unit,
                         payload=payload, qos=self.QOS)

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
