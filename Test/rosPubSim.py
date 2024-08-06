# 本函数用于模拟ros中位置信息与速度信息的发布
import random
import time
from paho.mqtt import client as mqtt_client


broker = '8.130.97.89'
port = 1883
topic_location = "status/location"
topic_vel = "status/velocity"
client_id = f'python-mqtt-{random.randint(0, 1000)}'


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client, topic, msg):
    result = client.publish(topic, msg)
    # result: [0, 1]
    status = result[0]
    if status == 0:
        print(f"Send `{msg}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")


def run():
    client = connect_mqtt()
    client.loop_start()
    # 例子
    msg_locaion = "125.272632 43.820585"
    msg_velocity = "3.1"
    while True:
        """"
        add your code here
        # msg的格式需要和上面的一样，经纬度用空格分开
        msg_locaion = read_location()
        msg_velocity = read_velocity()
        """
        time.sleep(1)
        publish(client, topic_location, msg_locaion)
        publish(client, topic_vel, msg_velocity)

if __name__ == '__main__':
    run()