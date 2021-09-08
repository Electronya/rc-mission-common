from .baseMsg import BaseMessage


class UnitCxnStateMsg(BaseMessage):
    """
    The client state message class.
    """
    STATE_KEY = 'state'
    ONLINE_STATE = 'online'
    OFFLINE_STATE = 'offline'
    TOPIC_ROOT = 'units/connectionState'
    QOS = 1
    RETAIN = True

    def __init__(self, unit: str, payload: dict = None) -> None:
        """
        The client state message constructor.

        Params:
            unit:       The unit ID.
            payload:    Dictionary representing the message payload.
                        Default: None.
        """
        super().__init__(f"{self.TOPIC_ROOT}/{unit}", unit,
                         payload=payload, qos=self.QOS, retain=self.RETAIN)

    def setAsOffline(self) -> None:
        """
        Change the state to offline.
        """
        payload = {}
        payload[self.STATE_KEY] = self.OFFLINE_STATE
        super().setPayload(payload)

    def setAsOnline(self) -> None:
        """
        Change the state to online.
        """
        payload = {}
        payload[self.STATE_KEY] = self.ONLINE_STATE
        super().setPayload(payload)

    def getState(self) -> str:
        """
        Get the state from the message.

        Return:
            The state of the client contained in the message.
        """
        return super().getPayload()[self.STATE_KEY]

    def isOffline(self) -> bool:
        """
        Test if the state contained in the message is ONLINE.

        Return:
            True if the state is online, Flase otherwise.
        """
        state = super().getPayload()[self.STATE_KEY]
        return True if state == self.OFFLINE_STATE else False

    def isOnline(self) -> bool:
        """
        Test if the state contained in the message is ONLINE.

        Return:
            True if the state is online, Flase otherwise.
        """
        state = super().getPayload()[self.STATE_KEY]
        return True if state == self.ONLINE_STATE else False
