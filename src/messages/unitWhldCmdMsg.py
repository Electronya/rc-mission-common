from .baseMsg import BaseMessage


class UnitWhldCmdMsg(BaseMessage):
    """
    The wheeled unit command message.
    """
    TOPIC_ROOT = 'units/wheeled'
    STEERING_KEY = 'steering'
    THROTTLE_KEY = 'throttle'

    def __init__(self, unit: str, payload=None) -> None:
        """
        Constructor.

        Params:
            unit:       The unit ID.
            payload:    The message payload.
        """
        super().__init__(f"{self.TOPIC_ROOT}/{unit}/steering",
                         unit, payload=payload)

    def setSteering(self, modifier: float) -> None:
        """
        Set the steering modifier.

        Params:
            modifier:   The new modifier.
        """
        if self._payload is None:
            self._payload = {}
        self._payload[self.STEERING_KEY] = modifier

    def getSteering(self) -> float:
        """
        Get the steering mofifier.

        Return:
            The steering mofifier.
        """
        return self._payload[self.STEERING_KEY]

    def setThrottle(self, modifier: float) -> None:
        """
        Set the throttle modifier.

        Params:
            modifier:   The new modifier.
        """
        if self._payload is None:
            self._payload = {}
        self._payload[self.THROTTLE_KEY] = modifier

    def getThrottle(self) -> float:
        """
        Get the throttle modifier.

        Return:
            The throttle modifier.
        """
        return self._payload[self.THROTTLE_KEY]
