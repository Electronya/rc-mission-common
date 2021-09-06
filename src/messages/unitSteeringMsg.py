from .baseMsg import BaseMessage


class UnitSteeringMsg(BaseMessage):
    """
    The unit steering message.
    """
    TOPIC_ROOT = 'units/wheeled'
    STEERING_KEY = 'angle'

    def __init__(self, unit: str, payload=None) -> None:
        """
        Constructor.

        Params:
            unit:       The unit ID.
            payload:    The message payload.
        """
        super().__init__(f"{self.TOPIC_ROOT}/{unit}/steering",
                         unit, payload=payload)

    def setAngle(self, angle: float) -> None:
        """
        Set the steering angle.

        Params:
            angle:      The new angle.
        """
        payload = {}
        payload[self.STEERING_KEY] = angle
        super().setPayload(payload)

    def getAngle(self) -> float:
        """
        Get the steering angle.

        Return:
            The steering angle.
        """
        return super().getPayload()[self.STEERING_KEY]
