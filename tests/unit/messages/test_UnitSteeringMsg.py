from unittest import TestCase
from unittest.mock import patch

import os
import sys

sys.path.append(os.path.abspath('./src'))

from messages.unitSteeringMsg import UnitSteeringMsg    # noqa: E402 F401


class TestUnitSteeringMsg(TestCase):
    """
    The UnitSteeringMsg class test cases.
    """
    def setUp(self):
        """
        The test cases setup.
        """
        self.testUnit = 'test unit'
        self.testPayload = {}
        self.testPayload[UnitSteeringMsg.STEERING_KEY] = 40
        self.testMsg = UnitSteeringMsg(self.testUnit, payload=self.testPayload)

    @patch('messages.unitSteeringMsg.BaseMessage.__init__')
    def test_constructor(self, mockedSuperConst):
        """
        The constructor must initialize the base class with
        the correct parameters.
        """
        expectedTopic = f"{UnitSteeringMsg.TOPIC_ROOT}/{self.testUnit}/steering"    # noqa: E501
        testMsg = UnitSteeringMsg(self.testUnit,    # noqa: F841
                                  payload=self.testPayload)
        mockedSuperConst.assert_called_once_with(expectedTopic,
                                                 self.testUnit,
                                                 payload=self.testPayload)

    def test_setAngle(self):
        """
        The setAngle method must save the new steering angle.
        """
        expectedAgle = -12
        self.testMsg.setAngle(expectedAgle)
        self.assertEqual(expectedAgle,
                         self.testMsg._payload[UnitSteeringMsg.STEERING_KEY])

    def test_getAngle(self):
        """
        The getAngle method must return the current steering angle.
        """
        testResult = self.testMsg.getAngle()
        self.assertEqual(testResult,
                         self.testPayload[UnitSteeringMsg.STEERING_KEY])
