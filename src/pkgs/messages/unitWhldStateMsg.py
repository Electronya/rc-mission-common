from .baseMsg import BaseMessage


class UnitWhldStateMsg(BaseMessage):
    """
    The wheeled unit state message.
    """
    TOPIC_ROOT = 'units/wheeled'
    STEERING_KEY = 'steering'
    THROTTLE_KEY = 'throttle'

    def __init__(self, unit: str, payload: dict = None) -> None:
        """
        Constructor.

        Params:
            unit:       The unit ID.
            Payload:    The message payload. Default: None.
        """
        super().__init__(f"{self.TOPIC_ROOT}/{unit}/state",
                         unit, payload=payload)

    def setSteering(self, modifier: float) -> None:
        """
        Set the steering state.

        Params:
            modifier:   The steering modifier.
        """
        if self._payload is None:
            self._payload = {}
        self._payload[self.STEERING_KEY] = modifier

    def getSteering(self) -> float:
        """
        Get the steering state.

        Return:
            The steering state.
        """
        return self._payload[self.STEERING_KEY]

    def setThrottle(self, modifier: float) -> None:
        """
        Set the throttle state.

        Params:
            modifier:   The throttle state.
        """
        if self._payload is None:
            self._payload = {}
        self._payload[self.THROTTLE_KEY] = modifier

    def getThrottle(self) -> None:
        """
        Get the throttle state.

        Returns:
            The throttle state.
        """
        return self._payload[self.THROTTLE_KEY]
