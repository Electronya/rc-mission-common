from .baseMsg import BaseMessage


class UnitThrtlBrkMsg(BaseMessage):
    """
    The Unit throttle/break message.
    """
    THROTTLE_KEY = 'amplitude'
    TOPIC_ROOT = 'units'

    def __init__(self, unit: str, payload: dict = None) -> None:
        """
        Constructor.

        Params:
            unit:       The unit ID.
            payload:    The message payload. Default: None.
        """
        super().__init__(f"{self.TOPIC_ROOT}/{unit}/throttle",
                         unit, payload=payload)

    def setAmplitude(self, amplitude: float) -> None:
        """
        Set the throttle/brake amplitude.

        Params:
            amplitude:  The new throttle/brake amplitude.
        """
        payload = {}
        payload[self.THROTTLE_KEY] = amplitude
        super().setPayload(payload)

    def getAmplitude(self) -> float:
        """
        Get the throttle/brake amplitude.

        Return:
            The current throttle/brake amplitude.
        """
        return super().getPayload()[self.THROTTLE_KEY]
