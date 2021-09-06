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

    def setSteering(self, steering: float) -> None:
        """
        Set the steering state.

        Params:
            steering:   The steering modifier.
        """
        payload = super().getPayload()
        if payload is None:
            payload = {}
        payload[self.STEERING_KEY] = steering
        super().setPayload(payload)

    def getSteering(self) -> float:
        """
        Get the steering state.

        Return:
            The steering state.
        """
        return super().getPayload()[self.STEERING_KEY]

    def setThrottle(self, throttle: float) -> None:
        """
        Set the throttle state.

        Params:
            throttle:   The throttle state.
        """
        payload = super().getPayload()
        if payload is None:
            payload = {}
        payload[self.THROTTLE_KEY] = throttle
        super().setPayload(payload)

    def getThrottle(self) -> None:
        """
        Get the throttle state.

        Returns:
            The throttle state.
        """
        return super().getPayload()[self.THROTTLE_KEY]
