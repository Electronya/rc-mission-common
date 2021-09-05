from unittest import TestCase
from unittest.mock import patch

import os
import sys

sys.path.append(os.path.abspath('./src'))

from messages.unitThrtlBrkMsg import UnitThrtlBrkMsg    # noqa: E402 F401


class TestUnitThrtlBrkMsg(TestCase):
    """
    The UnitThrtlBrkMsg class test cases.
    """
    def setUp(self):
        """
        Test cases setup.
        """
        self.testUnit = 'test unit'
        self.testPayload = {}
        self.testPayload[UnitThrtlBrkMsg.THROTTLE_KEY] = 0.54
        self.testMsg = UnitThrtlBrkMsg(self.testUnit, self.testPayload)

    @patch('messages.unitThrtlBrkMsg.BaseMessage.__init__')
    def test_constructor(self, mockedSuperConst):
        """
        The constructor must initialize the base class with the
        correct parameters.
        """
        expectedTopic = f"{UnitThrtlBrkMsg.TOPIC_ROOT}/{self.testUnit}/throttle"    # noqa: E501
        testMsg = UnitThrtlBrkMsg(self.testUnit,    # noqa: F841
                                  payload=self.testPayload)
        mockedSuperConst.assert_called_once_with(expectedTopic, self.testUnit,
                                                 payload=self.testPayload)

    def test_setAmplitude(self):
        """
        The setAmplitude method must save the new
        throttle/brake amplitude.
        """
        expectedAmplitude = -0.99
        self.testMsg.setAmplitude(expectedAmplitude)
        self.assertEqual(self.testMsg._payload[UnitThrtlBrkMsg.THROTTLE_KEY],
                         expectedAmplitude)

    def test_getAmplitude(self):
        """
        The getAmplitude method must return the current
        throttle/brake amplitude.
        """
        testResult = self.testMsg.getAmplitude()
        self.assertEqual(testResult,
                         self.testPayload[UnitThrtlBrkMsg.THROTTLE_KEY])
