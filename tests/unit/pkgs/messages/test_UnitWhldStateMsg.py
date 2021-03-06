from unittest import TestCase
from unittest.mock import patch

import os
import sys

sys.path.append(os.path.abspath('./src'))

from pkgs.messages import UnitWhldStateMsg     # noqa: E402


class TestUnitWhldStateMsg(TestCase):
    """
    The UnitWhldStateMsg class test cases.
    """
    def setUp(self):
        """
        Test cases setup.
        """
        self.testUnit = 'test unit'
        self.testPayload = {}
        self.initSteering = 0.5
        self.initThrottle = -0.3
        self.testPayload[UnitWhldStateMsg.STEERING_KEY] = self.initSteering
        self.testPayload[UnitWhldStateMsg.THROTTLE_KEY] = self.initThrottle
        self.testMsg = UnitWhldStateMsg(self.testUnit, self.testPayload)

    @patch('pkgs.messages.unitWhldStateMsg.BaseMessage.__init__')
    def test_constructor(self, mockedSuperConst):
        """
        The constructor must initialize the base class
        with the correct parameters.
        """
        expectedTopic = f"{UnitWhldStateMsg.TOPIC_ROOT}/{self.testUnit}/state"   # noqa: E501
        testMsg = UnitWhldStateMsg(self.testUnit,    # noqa: F841
                                   payload=self.testPayload)
        mockedSuperConst.assert_called_once_with(expectedTopic, self.testUnit,
                                                 payload=self.testPayload)

    def test_setSteering(self):
        """
        The setSteering method must update the steering modifier
        in the message payload.
        """
        self.testMsg._payload = None
        expectedSteering = -1.0
        self.testMsg.setSteering(expectedSteering)
        self.assertEqual(self.testMsg._payload[UnitWhldStateMsg.STEERING_KEY],
                         expectedSteering)
        self.assertFalse(hasattr(self.testMsg._payload,
                                 UnitWhldStateMsg.THROTTLE_KEY))

    def test_getSteering(self):
        """
        The getSteering method must return the message steering modifier.
        """
        testResult = self.testMsg.getSteering()
        self.assertEqual(testResult,
                         self.testPayload[UnitWhldStateMsg.STEERING_KEY])

    def test_setThrottle(self):
        """
        The setThrottle method must update the throttle modifier
        in the message payload.
        """
        self.testMsg._payload = None
        expectedThrottle = 0.4
        self.testMsg.setThrottle(expectedThrottle)
        self.assertEqual(self.testMsg._payload[UnitWhldStateMsg.THROTTLE_KEY],
                         expectedThrottle)
        self.assertFalse(hasattr(self.testMsg._payload,
                                 UnitWhldStateMsg.STEERING_KEY))

    def test_getThrottle(self):
        """
        The getThrottle method must return the message throttle modifier.
        """
        testResult = self.testMsg.getThrottle()
        self.assertEqual(testResult,
                         self.testPayload[UnitWhldStateMsg.THROTTLE_KEY])
