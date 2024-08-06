import paho.mqtt.client as mqtt
import threading
import random
import time


class MqttPublisher:
    def __init__(self, central_ip='47.104.189.43', port=1883, node_name='bci_', anonymous=True, timeout=60):
        """
        :param central_ip: Broker的地址
        :param port:  端口号
        :param timeout:  连接延时
        :param node_name: 节点名称
        :param anonymous: 是否同时允许多个节点
        """
        self.broker_ip = central_ip
        self.broker_port = port
        self.timeout = timeout
        self.connected = False
        self.node_name = node_name
        if anonymous:
            self.node_name = self.node_name+str(random.randint(100000,999999))
        self.start()

    def start(self):
        # open publisher
        self.client = mqtt.Client(self.node_name)     # 创建客户端
        self.client.on_connect = self.on_connect  # 指定回调函数
        self.client.connect(self.broker_ip, self.broker_port, self.timeout)    # 开始连接
        self.client.loop_start()    # 开启一个独立的循环通讯线程。

    def publish(self, topic, payload, qos=0, retain=False):
        """
            发送一个mqtt消息
            :param retain:
            :param topic: 消息名称，string类型
            :param payload: 消息内容，string类型
            :param qos: 消息等级
            :retain: 状态机消息
            :return:
        """
        if self.connected:
            return self.client.publish(topic, payload=payload, qos=qos, retain=retain)
        else:
            raise Exception("mqtt server not connected! you may use .Start() function to connect to server firstly.")

    '''
                回调函数
    '''
    def on_connect(self, client, userdata, flags, rc):
        '''
            连接到broker的回调函数
        '''
        if rc == 0:
            self.connected = True

        else:
            raise Exception("Failed to connect mqtt server.")


if __name__ == '__main__':
    p=MqttPublisher()
    while not p.connected:
        pass
    while True:
        p.publish('user/cmd/control', 'w')
        time.sleep(1)