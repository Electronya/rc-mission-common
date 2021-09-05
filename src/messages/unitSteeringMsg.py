from .baseMsg import BaseMessage


class UnitSteeringMsg(BaseMessage):
    """
    The unit steering message.
    """
    STEERING_KEY = 'angle'
    TOPIC_ROOT = 'units'

    def __init__(self, unit, payload=None) -> None:
        """
        Constructor.

        Params:
            unit:       The unit ID.
            payload:    The message payload.
            qos:        The message QoS.
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
