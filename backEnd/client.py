
import time
from paho.mqtt import client as mqtt_client
from PyQt5.QtGui import QImage
import random
from PyQt5.QtCore import QObject, pyqtSignal
from socket import *
import cv2 as cv
from detect import TargetDetect
from PyQt5.QtCore import QThread, QTimer, Qt
import numpy as np
# define broker parameter
broker = '8.130.97.89' # 服务器公网ip地址
port = 1883

# 用于订阅 位置/速度消息
class Subscriber(QObject):
    # 设置信号量
    velocity_to_main_signal = pyqtSignal(str, str)
    location_to_main_signal = pyqtSignal(str, str)
    start_thread_signal = pyqtSignal()

    def __init__(self):
        super(Subscriber, self).__init__()
        client_id = f'user-sub-{random.randint(0, 1000)}'
        self.client = mqtt_client.Client(client_id)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    def work(self):
        self.client.connect(broker, port)
        self.client.subscribe("status/velocity", 0)
        self.client.subscribe("status/location", 0)
        self.client.loop_forever()

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Subscriber:success to connect")
        else:
            print("Subscriber:fail to connect")

    # 发送位置/速度消息
    def on_message(self, client, userdata, msg):
        # print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        if msg.topic == "status/velocity":
            self.velocity_to_main_signal.emit("velocity", msg.payload.decode())
        elif msg.topic == "status/location":
            self.location_to_main_signal.emit("location", msg.payload.decode())

# 用于发布控制命令
class Publisher(QObject):
    control_to_ros_signal = pyqtSignal(str)
    start_thread_signal = pyqtSignal()

    def __init__(self):
        super(Publisher, self).__init__()
        client_id = f'user-pub-{random.randint(0, 1000)}'
        self.client = mqtt_client.Client(client_id)
        self.client.on_connect = self.on_connect

    def work(self):
        self.client.connect(broker, port)
        self.client.loop_start()  # 开启一个独立的循环通讯线程

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Publisher:success to connect")
        else:
            print("Publisher:fail to connect")

    def publish(self, topic, payload, qos=0, retain=False):
        self.client.publish(topic, payload=payload, qos=qos, retain=retain)

    def control(self,cmd):
        print(cmd)
        self.publish('user/cmd/control', 'cmd')

# 用于接收图像信息
class ImgSubscriber(QObject):
    img_show_signal = pyqtSignal(QImage)
    start_thread_signal = pyqtSignal()

    def __init__(self):
        super(ImgSubscriber, self).__init__()
        self.s = socket(AF_INET, SOCK_DGRAM)  # 创建UDP套接字
        addr = ('0.0.0.0', 8081)  # 0.0.0.0表示本机
        self.s.bind(addr)
        # self.s.setblocking(0)  # 设置为非阻塞模式
        self.model = TargetDetect()

    def work(self):
        while True:
            try:
                # 读取数据from udp
                data, _ = self.s.recvfrom(921600)
                receive_data = np.frombuffer(data, dtype='uint8')
                downSize = (401, 291)
                r_img = cv.imdecode(receive_data, 1)
                r_img = cv.resize(r_img, (401, 291), interpolation= cv.INTER_AREA)
                show = cv.cvtColor(r_img, cv.COLOR_BGR2RGB)
                showImage = QImage(show.data, show.shape[1],show.shape[0],show.shape[1]*show.shape[2],QImage.Format_RGB888)
                self.img_show_signal.emit(showImage)
            except BlockingIOError as e:
                print("wrong")
