import paho.mqtt.client as mqtt
from unittest import TestCase
from unittest.mock import call, Mock, patch

import os
import sys

sys.path.append(os.path.abspath('./src'))

import mqttClient as client                             # noqa: E402
from messages.unitCxnMsg import UnitConnectionState     # noqa: E402


class TestMqttClient(TestCase):
    """
    The mqttClient module test cases.
    """
    def setUp(self):
        """
        Test cases setup.
        """
        self.testId = 'testId'
        self.testPassword = 'testPassword'
        self.mockedLogging = Mock()
        self.mockedClient = Mock()
        with patch('mqttClient.mqtt') as mockedMqtt:
            mockedMqtt.Client.return_value = self.mockedClient
            client.init(self.mockedLogging, self.testId, self.testPassword)
        self.mockedLogging.reset_mock()
        self.mockedClient.reset_mock()

    def tearDown(self):
        """
        Test cases teardown.
        """
        client.logger = None
        client.client = None

    def test_initAlreadyInit(self):
        """
        The init function must do nothing and warn that the client has
        already been initialized.
        """
        with patch('mqttClient.mqtt') as mockedMqtt:
            client.init(self.mockedLogging, self.testId, self.testPassword)
            self.mockedLogging.assert_not_called()
            mockedMqtt.Client.assert_not_called()
            client.logger.warn.assert_called_once()

    def test_initLogger(self):
        """
        The init function must initialize the logger.
        """
        client.logger = None
        client.client = None
        client.init(self.mockedLogging, self.testId, self.testPassword)
        self.mockedLogging.getLogger.assert_called_once_with(f"MQTT-{self.testId.upper()}")     # noqa: E501

    def test_initCreatMqttClient(self):
        """
        The init function must create the MQTT client.
        """
        client.logger = None
        client.client = None
        with patch('mqttClient.mqtt') as mockedMqtt:
            client.init(self.mockedLogging, self.testId, self.testPassword)
            mockedMqtt.Client.assert_called_once_with(client_id=self.testId)

    def test_initSetWill(self):
        """
        The init function must set the client last will.
        """
        client.logger = None
        client.client = None
        testWillMsg = UnitConnectionState(unit=self.testId, payload={
            UnitConnectionState.STATE_KEY: UnitConnectionState.OFFLINE_STATE
        })
        with patch('mqttClient.mqtt') as mockedMqtt:
            mockedMqtt.Client.return_value = self.mockedClient
            client.init(self.mockedLogging, self.testId, self.testPassword)
            client.client.will_set.assert_called_once_with(testWillMsg.get_topic(),     # noqa: E501
                                                           testWillMsg.to_json(),       # noqa: E501
                                                           qos=testWillMsg.get_qos(),   # noqa: E501
                                                           retain=True)                 # noqa: E501

    def test_initSetUserPassword(self):
        """
        The init function must set the user and password.
        """
        client.logger = None
        client.client = None
        with patch('mqttClient.mqtt') as mockedMqtt:
            mockedMqtt.Client.return_value = self.mockedClient
            client.init(self.mockedLogging, self.testId, self.testPassword)
            client.client.username_pw_set.assert_called_once_with(self.testId,
                                                                  self.testPassword)    # noqa: E501

    def test_initSetCallbacks(self):
        """
        The init function must set the client callbacks.
        """
        client.logger = None
        client.client = None
        with patch('mqttClient.mqtt') as mockedMqtt:
            mockedMqtt.Client.return_value = self.mockedClient
            client.init(self.mockedLogging, self.testId, self.testPassword)
            self.assertEqual(client.client.on_connect, client._onConnect)
            self.assertEqual(client.client.on_disconnect, client._onDisconnect)
            self.assertEqual(client.client.on_message, client._onMessage)
            self.assertEqual(client.client.on_publish, client._onPublish)
            self.assertEqual(client.client.on_subscribe, client._onSubscribe)
            self.assertEqual(client.client.on_unsubscribe,
                             client._onUnsubscribe)
            self.assertEqual(client.client.on_log, client._onLog)

    def test_onConnect(self):
        """
        The _onConnect function must log (info) the connection information.
        """
        testRc = 0
        client._onConnect(self.mockedClient, None, {}, testRc)
        client.logger.info.assert_called_once_with(f"connection result: "
                                                   f"{testRc}")

    def test_onDisconnect(self):
        """
        The _onDisconnect function must log (info)
        the disconnection information.
        """
        testRc = 0
        client._onDisconnect(self.mockedClient, None, testRc)
        client.logger.info.assert_called_once_with(f"disconnection result: "
                                                   f"{testRc}")

    def test_onMessage(self):
        """
        The _onMessage function must warn of the uncaught messages.
        """
        testMsg = 'uncaught message'
        client._onMessage(self.mockedClient, None, testMsg)
        client.logger.warn.assert_called_once_with(f"uncaught message: "
                                                   f"{testMsg}")

    def test_onPublish(self):
        """
        The _onPublish function must log (debug) the publish result.
        """
        testMid = 1
        client._onPublish(self.mockedClient, None, testMid)
        client.logger.debug.assert_called_once_with(f"message {testMid} "
                                                    f"published")

    def test_onSubscribe(self):
        """
        The _onSubscribe function must log (debug) the subscribe result.
        """
        testMid = 3
        testQos = 2
        client._onSubscribe(self.mockedClient, None, testMid, testQos)
        client.logger.debug.assert_called_once_with(f"subscribed to message "
                                                    f"{testMid} with QoS: "
                                                    f"{testQos}")

    def test_onUnsubscribe(self):
        """
        The _onUnsubscribe function must log (debug) the unsubscribe result.
        """
        testMid = 0
        client._onUnsubscribe(self.mockedClient, None, testMid)
        client.logger.debug.assert_called_once_with(f"unsubscribed from "
                                                    f"message {testMid}")

    def test_onLog(self):
        """
        The _onLog function must log the recieved message base on its level.
        """
        testLvls = [mqtt.MQTT_LOG_DEBUG, mqtt.MQTT_LOG_NOTICE,
                    mqtt.MQTT_LOG_INFO, mqtt.MQTT_LOG_WARNING,
                    mqtt.MQTT_LOG_ERR, 5000]
        testMsg = 'test log message'
        for idx, testLvl in enumerate(testLvls):
            client._onLog(self.mockedClient, None, testLvl, testMsg)
        client.logger.debug.assert_called_once_with(testMsg)
        client.logger.info.assert_called_with(testMsg)
        self.assertEqual(client.logger.info.call_count, 2)
        warnCalls = [call(testMsg), call(f"unknown level "
                                         f"log: {testMsg}")]
        client.logger.warn.assert_has_calls(warnCalls)
        client.logger.error.assert_called_once_with(testMsg)

    def test_connectNotInit(self):
        """
        The connect function must raise a MqttClientNotInit exception
        and do nothing else if the client has not been initialized.
        """
        client.client = None
        testIp = '192.168.1.45'
        testPort = 1883
        with self.assertRaises(client.MqttClientNotInit) as context:
            client.connect(testIp, testPort)
            self.assertTrue(isinstance(context.exception,
                                       client.MqttClientNotInit))
            client.client.connect.assert_not_called()

    def test_connect(self):
        """
        The connect function must try to connect to the broker.
        """
        testIp = '192.168.1.45'
        testPort = 1883
        client.connect(testIp, testPort)
        client.client.connect.assert_called_once_with(testIp, port=testPort)

    def test_disconnectNotInit(self):
        """
        The disconnect function must raise a MqttClientNotInit exception
        and do nothing else if the client has not been initialized.
        """
        client.client = None
        with self.assertRaises(client.MqttClientNotInit) as context:
            client.disconnect()
            self.assertTrue(isinstance(context.exception,
                                       client.MqttClientNotInit))
            client.client.disconnect.assert_not_called()

    def test_disconnect(self):
        """
        The disconnect function must disconect from the broker.
        """
        client.disconnect()
        client.client.disconnect.assert_called_once()

    def test_startLoopNotInit(self):
        """
        The startLoop function must raise a MqttClientNotInit exception
        and do nothing else if the client has not been initialized.
        """
        client.client = None
        with self.assertRaises(client.MqttClientNotInit) as context:
            client.startLoop()
            self.assertTrue(isinstance(context.exception,
                                       client.MqttClientNotInit))
            client.client.loop_start.assert_not_called()

    def test_startLoop(self):
        """
        The startLoop function must start the MQTT client network loop.
        """
        client.startLoop()
        client.client.loop_start.assert_called_once()

    def test_stopLoopNotInit(self) -> None:
        """
        The stopLoop function must raise a MqttClientNotinit exception
        and do nothing else if the client has not been initialized.
        """
        client.client = None
        with self.assertRaises(client.MqttClientNotInit) as context:
            client.stopLoop()
            self.assertTrue(isinstance(context.exception,
                            client.MqttClientNotInit))
            client.client.loop_stop.assert_not_called()

    def test_stopLoop(self):
        """
        The stopLoop function must stop the MQTT client network loop.
        """
        client.stopLoop()
        client.client.loop_stop.assert_called_once()
