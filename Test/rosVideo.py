
import numpy as np
import cv2
from socket import *

# 127.0.0.1表示本机的IP，用于测试，使用时需要改为运行客户端主机的ip地址
addr = ('127.0.0.1', 8081)
# 需要修改成图像
cap = cv2.VideoCapture("../video/roadMove.mp4")
#cap = cv2.VideoCapture(0)
# 设置镜头分辨率，默认是640x480
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 200)

s = socket(AF_INET, SOCK_DGRAM) # 创建UDP套接字

while True:
    _, img = cap.read()
    downSize = (250, 150)
    img = cv2.flip(img, 1)
    img = cv2.resize(img, downSize, interpolation= cv2.INTER_AREA)
    # cv2.imshow("test",img)
    # 压缩图片
    _, send_data = cv2.imencode('.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 50])

    s.sendto(send_data, addr)
    print(f'正在发送数据，大小:{img.size} Byte')

    # cv2.putText(img, "client", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    # cv2.imshow('client', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

s.close()
cv2.destroyAllWindows()


