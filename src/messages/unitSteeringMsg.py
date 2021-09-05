from .baseMsg import BaseMessage


class UnitSteeringMessage(BaseMessage):
    """
    The unit steering message.
    """
    STEERING_KEY = 'steering'
    TOPIC_ROOT = 'units'

    def __init__(self, unit, payload=None, qos=0):
        """
        Constructor.

        Params:
            unit:           The unit ID.
            payload:        The message payload.
            qos:            The message QoS.
        """
        super().__init__(f"{self.TOPIC_ROOT}/{unit}/steering",
                         unit, payload=payload, qos=qos)

    def update_modifier(self, modifier):
        """
        Update the steering modifier.

        Params:
            modifier:       The new modifier.
        """
        payload = {}
        payload[self.STEERING_KEY] = modifier
        super().setPayload(payload)

    def get_modifier(self):
        """
        Get the steering modifier.

        Return:
            The steering modifier.
        """
        return super().getPayload()[self.STEERING_KEY]
