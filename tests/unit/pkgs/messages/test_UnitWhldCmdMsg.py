from unittest import TestCase
from unittest.mock import patch

import os
import sys

sys.path.append(os.path.abspath('./src'))

from pkgs.messages import UnitWhldCmdMsg     # noqa: E402 F401


class TestUnitWhldCmdMsg(TestCase):
    """
    The UnitWhldCmdMsg class test cases.
    """
    def setUp(self):
        """
        The test cases setup.
        """
        self.testUnit = 'test unit'
        self.testPayload = {}
        self.testPayload[UnitWhldCmdMsg.STEERING_KEY] = 0.64
        self.testPayload[UnitWhldCmdMsg.THROTTLE_KEY] = -0.16
        self.testMsg = UnitWhldCmdMsg(self.testUnit, payload=self.testPayload)

    @patch('pkgs.messages.unitWhldCmdMsg.BaseMessage.__init__')
    def test_constructor(self, mockedSuperConst):
        """
        The constructor must initialize the base class with
        the correct parameters.
        """
        expectedTopic = f"{UnitWhldCmdMsg.TOPIC_ROOT}/{self.testUnit}/steering"    # noqa: E501
        testMsg = UnitWhldCmdMsg(self.testUnit,    # noqa: F841
                                 payload=self.testPayload)
        mockedSuperConst.assert_called_once_with(expectedTopic,
                                                 self.testUnit,
                                                 payload=self.testPayload)

    def test_setSteering(self):
        """
        The setSteering method must save the new steering modifier.
        """
        self.testMsg._payload = None
        expectedModifier = -0.92
        self.testMsg.setSteering(expectedModifier)
        self.assertEqual(self.testMsg._payload[UnitWhldCmdMsg.STEERING_KEY],
                         expectedModifier)

    def test_getSteering(self):
        """
        The getSteering method must return the current steering modifier.
        """
        testResult = self.testMsg.getSteering()
        self.assertEqual(self.testPayload[UnitWhldCmdMsg.STEERING_KEY],
                         testResult)

    def test_setThrottle(self):
        """
        The setThrottle method must save the new throttle modifier.
        """
        self.testMsg._payload = None
        expectedModifier = 0.05
        self.testMsg.setThrottle(expectedModifier)
        self.assertEqual(self.testMsg._payload[UnitWhldCmdMsg.THROTTLE_KEY],
                         expectedModifier)

    def test_getThrottle(self):
        """
        The getThrottle method must return the current throttle modifier.
        """
        testResult = self.testMsg.getThrottle()
        self.assertEqual(self.testMsg._payload[UnitWhldCmdMsg.THROTTLE_KEY],
                         testResult)
