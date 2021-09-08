import json
from unittest import TestCase

import os
import sys

sys.path.append(os.path.abspath('./src'))

from pkgs.messages.baseMsg import BaseMessage   # noqa: E402


class TestBaseMessage(TestCase):
    """
    BaseMessage class test cases.
    """
    def setUp(self):
        """
        Test cases setup.
        """
        self.testTopic = 'test topic'
        self.testUnit = 'unit'
        self.testPayload = {'payload key': 'payload value'}
        self.testQos = 1
        self.testRetain = True
        self.testMsg = BaseMessage(self.testTopic, self.testUnit,
                                   payload=self.testPayload,
                                   qos=self.testQos, retain=self.testRetain)

    def test_constructorSaveData(self):
        """
        The constructor must save the message information.
        """
        testMsg = BaseMessage(self.testTopic, self.testUnit,
                              payload=self.testPayload,
                              qos=self.testQos, retain=self.testRetain)
        self.assertEqual(testMsg._topic, self.testTopic)
        self.assertEqual(testMsg._unit, self.testUnit)
        self.assertEqual(testMsg._payload, self.testPayload)
        self.assertEqual(testMsg._qos, self.testQos)
        self.assertEqual(testMsg._retain, self.testRetain)

    def test_getTopic(self):
        """
        The getTopic method must return the message topic.
        """
        testResult = self.testMsg.getTopic()
        self.assertEqual(testResult, self.testTopic)

    def test_getUnit(self):
        """
        The getUnit method must return the unit ID sending the message.
        """
        testResult = self.testMsg.getUnit()
        self.assertEqual(testResult, self.testUnit)

    def test_setPayload(self):
        """
        The setPayload must save the new payload.
        """
        expectedPayload = {'new payload key': 'new payload value'}
        self.testMsg.setPayload(expectedPayload)
        self.assertEqual(expectedPayload, self.testMsg._payload)

    def test_getPayload(self):
        """
        The getPayload method must return the current payload.
        """
        testResult = self.testMsg.getPayload()
        self.assertEqual(testResult, self.testPayload)

    def test_setQos(self):
        """
        The setQos method must save the new QoS.
        """
        expectedQos = 0
        self.testMsg.setQos(expectedQos)
        self.assertEqual(expectedQos, self.testMsg._qos)

    def test_getQos(self):
        """
        The getQos method must return the current QoS.
        """
        testResult = self.testMsg.getQos()
        self.assertEqual(testResult, self.testQos)

    def test_setRetain(self):
        """
        The setRetain method must save the new retention flag value.
        """
        expectedRetain = False
        self.testMsg.setRetain(expectedRetain)
        self.assertEqual(expectedRetain, self.testMsg._retain)

    def test_getRetain(self):
        """
        The getRetain method must return the current retention flag value.
        """
        testResult = self.testMsg.getRetain()
        self.assertEqual(testResult, self.testRetain)

    def test_fromJson(self):
        """
        The fromJson method must update the unit and payload from a
        JSON string.
        """
        expectedUnit = 'new unit'
        expectedPayload = {'new payload key': 'new payload value'}
        testJson = json.dumps({'unit id': expectedUnit,
                               'payload': expectedPayload})
        self.testMsg.fromJson(testJson)
        self.assertEqual(expectedUnit, self.testMsg._unit)
        self.assertEqual(expectedPayload, self.testMsg._payload)

    def test_toJson(self):
        """
        The toJson method return the JSON string representing the message.
        """
        expectedJson = json.dumps({'unit id': self.testUnit,
                                   'payload': self.testPayload})
        testResult = self.testMsg.toJson()
        self.assertEqual(testResult, expectedJson)
