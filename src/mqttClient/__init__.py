from array import array
import paho.mqtt.client as mqtt

from .exceptions import MqttClientNotInit
from messages.baseMsg import BaseMessage
from messages.unitCxnMsg import UnitConnectionState

client = None
logger = None


def init(appLogger: object, clientId: str, password: str) -> None:
    """
    Initialize the MQTT client.

    Params:
        appLogger:  The app logger.
        clientId:   The client ID.
        password:   The password.
    """
    global client
    global logger
    if logger is None and client is None:
        logger = appLogger.getLogger(f"MQTT-{clientId.upper()}")
        logger.info(f"creating MQTT client {clientId}")
        client = mqtt.Client(client_id=clientId)
        cxnMsg = UnitConnectionState(clientId, {
            UnitConnectionState.STATE_KEY: UnitConnectionState.OFFLINE_STATE
        })
        client.will_set(cxnMsg.get_topic(), cxnMsg.to_json(),
                        qos=cxnMsg.get_qos(), retain=True)
        client.username_pw_set(clientId, password)
        client.on_connect = _onConnect
        client.on_disconnect = _onDisconnect
        client.on_message = _onMessage
        client.on_publish = _onPublish
        client.on_subscribe = _onSubscribe
        client.on_unsubscribe = _onUnsubscribe
        client.on_log = _onLog
    else:
        logger.warn(f"MQTT client {clientId} already initialized.")


def _onConnect(client, usrData, flags, rc) -> None:
    """
    The on connection callback.

    Params:
        client:     The client instance.
        usrData:    The user data set on the client instance.
        flags:      The connection flags from the broker.
        rc:         The connection result.
    """
    global logger
    logger.info(f"connection result: {rc}")


def _onDisconnect(client, usrData, rc) -> None:
    """
    The on disconnect callback.

    Params:
        client:     The client instance.
        usrData:    The user data set on the client instance.
        rc:         The connection result.
    """
    global logger
    logger.info(f"disconnection result: {rc}")


def _onMessage(client, usrData, msg) -> None:
    """
    The on disconnect callback.

    Params:
        client:     The client instance.
        usrData:    The user data set on the client instance.
        msg:        The received message.
    """
    global logger
    logger.warn(f"uncaught message: {msg}")


def _onPublish(client, usrData, mid) -> None:
    """
    The on publish callback.

    Params:
        client:     The client instance.
        usrData:    The user data set on the client instance.
        mid:        The message id.
    """
    global logger
    logger.debug(f"message {mid} published")


def _onSubscribe(client, usrData, mid, qos) -> None:
    """
    The on subscribe callback.

    Params:
        client:     The client instance.
        usrData:    The user data set on the client instance.
        mid:        The message id.
        qos:        The granted QoS by the broker.
    """
    global logger
    logger.debug(f"subscribed to message {mid} with QoS: {qos}")


def _onUnsubscribe(client, usrData, mid) -> None:
    """
    The on unsubscribe callback.

    Params:
        client:     The client instance.
        usrData:    The user data set on the client instance.
        mid:        The message id.
    """
    global logger
    logger.debug(f"unsubscribed from message {mid}")


def _onLog(client, usrData, lvl, msg) -> None:
    """
    The on disconnect callback.

    Params:
        client:     The client instance.
        usrData:    The user data set on the client instance.
        lvl:        The message log level.
        msg:        The log message.
    """
    global logger
    if lvl == mqtt.MQTT_LOG_DEBUG:
        logger.debug(msg)
    elif lvl == mqtt.MQTT_LOG_NOTICE or lvl == mqtt.MQTT_LOG_INFO:
        logger.info(msg)
    elif lvl == mqtt.MQTT_LOG_WARNING:
        logger.warn(msg)
    elif lvl == mqtt.MQTT_LOG_ERR:
        logger.error(msg)
    else:
        logger.warn(f"unknown level log: {msg}")


def connect(ip: str, port: int) -> None:
    """
    Connect to the broker.

    Params:
        ip:     The broker IP address.
        port:   The broker listening port.
    """
    global client
    global logger
    if client is None or logger is None:
        raise MqttClientNotInit()
    logger.info(f"trying to connect to broker: {ip}:{port}")
    client.connect(ip, port=port)


def disconnect() -> None:
    """
    Disconnect from the broker.
    """
    global client
    global logger
    if client is None or logger is None:
        raise MqttClientNotInit()
    logger.info('disconnecting from the broker')
    client.disconnect()


def startLoop() -> None:
    """
    Start the network loop.
    """
    global client
    global logger
    if client is None or logger is None:
        raise MqttClientNotInit()
    logger.info('starting network loop')
    client.loop_start()


def stopLoop() -> None:
    """
    Stop the network loop.
    """
    global client
    global logger
    if client is None or logger is None:
        raise MqttClientNotInit()
    logger.info('stopping network loop')
    client.loop_stop()


def publish(msg: BaseMessage) -> None:
    """
    Publish a message.

    Params:
        msg:    The message to publish.
    """
    global client
    global logger
    if client is None or logger is None:
        raise MqttClientNotInit()
    logger.debug(f"publishing message on topic {msg.get_topic()}")
    client.publish(msg.get_topic(), payload=msg.to_json(),
                   qos=msg.get_qos(), retain=msg.get_retain())


def subscribe(subs: array) -> None:
    """
    Subscribe to a list of subscriptions.

    Params:
        subs:   The list of subscriptions to subscribe to.
    """
    global client
    global logger
    if client is None or logger is None:
        raise MqttClientNotInit()
    for sub in subs:
        logger.info(f"subscribing to {sub['topic']}")
        client.subscribe(sub['topic'], qos=sub['qos'])
