
from PyQt5.QtWidgets import QWidget, QVBoxLayout
from manageWindow_ui import Ui_MangeWindow
from PyQt5.QtGui import QPixmap
import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.dates as mdate
import matplotlib.pyplot as plt
import math
import numpy as np
matplotlib.use('Qt5Agg')

class ManageWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MangeWindow()
        self.ui.setupUi(self)

        # label hardware
        self.hardware = self.ui.label_carHardware
        self.hardware.setPixmap(QPixmap("./QtUiFile/img/hardware/hardware.png"))
        # camera
        self.cameraImg = self.ui.label_carCamera
        self.cameraImg.setPixmap(QPixmap("./QtUiFile/img/hardware/3Dcamera.png"))
        self.cameraText = []
        self.cameraText.append(self.ui.label_carCamera1)
        self.cameraText.append(self.ui.label_carCamera2)
        self.cameraText.append(self.ui.label_carCamera3)
        self.cameraText[0].setText("深度摄像头")
        self.cameraText[1].setText("RGB像素:1080P")
        self.cameraText[2].setText("最大帧率：30FPS")
        # laser
        self.laserImg = self.ui.label_carRadar
        self.laserImg.setPixmap(QPixmap("./QtUiFile/img/hardware/radar.png"))
        self.laserText = []
        self.laserText.append(self.ui.label_carRadar1)
        self.laserText.append(self.ui.label_carRadar2)
        self.laserText.append(self.ui.label_carRadar3)
        self.laserText[0].setText("激光雷达")
        self.laserText[1].setText("扫描原理：机械旋转式")
        self.laserText[2].setText("回波方式：单回波")
        # label wheel
        self.wheelImg = self.ui.label_carBattery
        self.wheelImg.setPixmap(QPixmap("./QtUiFile/img/hardware/jetson.png"))
        self.wheelText = []
        self.wheelText.append(self.ui.label_carBattery1)
        self.wheelText.append(self.ui.label_carBattery2)
        self.wheelText.append(self.ui.label_carBattery3)
        self.wheelText[0].setText("Jetson Nano")
        self.wheelText[1].setText("GPU:128 核 NVIDIA Maxwell")
        self.wheelText[2].setText("CPU:Arm Cortex®-A57 ")
        # label car img
        self.carImg = self.ui.label_carImg
        self.carImg.setPixmap(QPixmap("./QtUiFile/img/car/car2.png"))
        # version
        self.carName = self.ui.label_typeVersion
        self.carName.setText("测试车一号")
        # operation
        self.carOperation = self.ui.label_typeBattery
        self.carOperation.setText("负责人:小明")
        # location
        self.locationImg = self.ui.label_locationIcon
        self.locationImg.setPixmap(QPixmap("./QtUiFile/img/hardware/location.png"))
        # battery
        self.battery = self.ui.label_one
        self.battery.setText("电量🔋")
        self.batteryValue = self.ui.progressBar_one
        self.batteryValue.setValue(80)
        # memory
        self.memoryValue = self.ui.progressBar_two
        self.memoryValue.setValue(40)
        self.memory = self.ui.label_two
        self.memory.setText("内存占比")
        # self.ui.label_one.setVisible(False)
        # self.ui.progressBar_one.setVisible(False)
        # self.ui.label_two.setVisible(False)
        # self.ui.progressBar_two.setVisible(False)
        # self.ui.label_three.setVisible(False)
        # self.ui.progressBar_three.setVisible(False)

        # upgrade
        self.cpu = self.ui.label_three
        self.cpu.setText("CPU负载")
        self.cpuValue = self.ui.progressBar_three
        self.cpuValue.setValue(30)


        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.qvLay = QVBoxLayout()
        self.qvLay.addWidget(self.canvas)
        self.ui.frame_carChart.setLayout(self.qvLay)
        self.plot_()

        # 连接的绘制的方法
    def plot_(self):
        x_range = np.linspace(-20, 30, 6, endpoint=True)
        name = ['-20°', '-10°', '0°', '10°', '20°', '30°']
        y_range = np.linspace(30, 55, 6, endpoint=True)
        percentage_name = ['30%', '35%', '40%', '45%', '50%', '55%']

        rect = [0.2, 0.2, 0.7, 0.7]
        ax = self.figure.add_axes(rect)
        ax.tick_params(axis='both',color='darkblue',labelcolor='darkblue')
        font = {"family":"Times New Roman", 'size':12, 'color':'darkblue'}
        ax.set_ylabel("percentage/10km", fontdict=font)
        ax.set_xlabel("temperature", fontdict=font)
        ax.set_xticks(x_range, name)
        ax.set_yticks(y_range, percentage_name)
        ax.set_ylim(30,55)

        x = x_range
        y = [50, 40, 34, 32, 33, 38]

        # 美化
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_color('darkblue')
        ax.spines['left'].set_color('darkblue')

        ax.plot(x, y, color='deepskyblue')