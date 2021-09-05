from unittest import TestCase
from unittest.mock import call, Mock, patch

import os
import sys

sys.path.append(os.path.abspath('./src'))

from messages.unitCxnStateMsg import UnitCxnStateMsg    # noqa: E402


class TestUnitCxnStateMsg(TestCase):
    """
    The UnitCxnStateMsg class test cases.
    """
    def setUp(self):
        """
        The test cases setup.
        """
        self.testUnit = 'test unit'
        self.testPayload = {}
        self.testPayload[UnitCxnStateMsg.STATE_KEY] = UnitCxnStateMsg.ONLINE_STATE  # noqa: E501
        self.testMsg = UnitCxnStateMsg(self.testUnit, self.testPayload)

    @patch('messages.unitCxnStateMsg.BaseMessage.__init__')
    def test_constructor(self, mockedSuperConst):
        """
        The constructor must intialize the base class with
        the correct parameters.
        """
        expectedTopic = f"{UnitCxnStateMsg.TOPIC_ROOT}/{self.testUnit}"
        testMsg = UnitCxnStateMsg(self.testUnit, self.testPayload)      # noqa: F841 E501
        mockedSuperConst.assert_called_once_with(expectedTopic,
                                                 self.testUnit,
                                                 payload=self.testPayload,
                                                 qos=UnitCxnStateMsg.QOS,
                                                 retain=UnitCxnStateMsg.RETAIN)

    def test_setAsOffline(self):
        """
        The setAsOffline method must set the state to offline.
        """
        self.testMsg.setAsOffline()
        self.assertEqual(self.testMsg._payload[UnitCxnStateMsg.STATE_KEY],
                         UnitCxnStateMsg.OFFLINE_STATE)

    def test_setAsOnline(self):
        """
        The setAsOnline method must set the state to online.
        """
        self.testMsg._payload[UnitCxnStateMsg.STATE_KEY] = \
            UnitCxnStateMsg.OFFLINE_STATE
        self.testMsg.setAsOnline()
        self.assertEqual(self.testMsg._payload[UnitCxnStateMsg.STATE_KEY],
                         UnitCxnStateMsg.ONLINE_STATE)

    def test_getState(self):
        """
        The getState method must return the current state.
        """
        expectedState = UnitCxnStateMsg.ONLINE_STATE
        testResult = self.testMsg.getState()
        self.assertEqual(testResult, expectedState)

    def test_isOffline(self):
        """
        The isOffline state method must return True
        only if the state is offline.
        """
        self.assertFalse(self.testMsg.isOffline())
        self.testMsg.setAsOffline()
        self.assertTrue(self.testMsg.isOffline())

    def test_isOnline(self):
        """
        The isOnline state method must return True
        only if the state is online.
        """
        self.assertTrue(self.testMsg.isOnline())
        self.testMsg.setAsOffline()
        self.assertFalse(self.testMsg.isOnline())
