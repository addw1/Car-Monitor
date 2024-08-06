from mainPage_ui import MainPageUi
from PyQt5.QtWidgets import QFrame, QStackedLayout, QVBoxLayout
from PyQt5.QtGui import QMovie, QPixmap
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from webModule import LocationModule
from imgModule import ImgModule
from hwMoudle import HwModule
from pointModule import PointModule
from reviewModule import ReviewModule


class MainPage(QFrame):
    def __init__(self):
        # 加载Ui文件
        super().__init__()
        self.ui = MainPageUi()
        self.ui.setupUi(self)

        # 初始化组件
        self.batteryIcon = self.ui.label_3
        self.batteryBar = self.ui.progressBar
        self.memoryIcon = self.ui.label_20
        self.memoryBar = self.ui.progressBar_2
        self.isConnectIcon = self.ui.label_4
        self.carModelIcon = self.ui.label_2
        self.connectBtn = self.ui.pushButton_3
        self.timeLabel = self.ui.label_5
        self.weatherLabel = self.ui.label_19
        self.weatherImg = self.ui.label_6
        self.temperLabel = self.ui.label_7
        self.weatherRtLabel = self.ui.label_8
        self.locationLabel = self.ui.label_9
        self.rtStatusFrame = self.ui.frame_3
        self.rtVelocityLabel = self.ui.label_21
        self.rtVelocityValue = self.ui.label_23
        self.rtVelocitySLabel = self.ui.label_22
        self.rtVelocityFrame = self.ui.frame_8
        self.energyFrame = self.ui.frame_4
        self.energyLabel = self.ui.label_10
        self.energyChatFrame = self.ui.frame_5
        self.avVelocityValue = self.ui.label_12
        self.avVelocityLabel = self.ui.label_13
        self.avDistanceValue = self.ui.label_14
        self.avDistanceLabel = self.ui.label_15
        self.hourValue = self.ui.label_16
        self.hourLabel = self.ui.label_17
        self.indicatorLabel = self.ui.label_11
        self.centerFrame = self.ui.frame_2

        # 设置中心容器布局
        self.centerLayout = QStackedLayout()
        self.centerFrame.setLayout(self.centerLayout)

        # 创建各个功能模块
        self.locModule = LocationModule()
        self.imgModule = ImgModule()
        self.hwModule = HwModule()
        self.pointModule = PointModule()
        self.reviewModule = ReviewModule()

        # 将功能模块加入到stack布局中
        self.centerLayout.addWidget(self.locModule)
        self.centerLayout.addWidget(self.imgModule)
        self.centerLayout.addWidget(self.hwModule)
        self.centerLayout.addWidget(self.pointModule)
        self.centerLayout.addWidget(self.reviewModule)

        # 建立7天能耗布局并为matplotlib创建画布
        self.dayChartLayout = QVBoxLayout()
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.dayChartLayout.addWidget(self.canvas)
        self.energyChatFrame.setLayout(self.dayChartLayout)

        # 设置汽车模型（在这里把gif关闭了，既为静止画面）
        self.movie = QMovie('./video/carModel.gif')
        self.carModelIcon.setMovie(self.movie)
        self.movie.start()
        self.movie.setPaused(True)

    # API：进行页面切换
    def set_center_content(self, string):
        if string == "location":
            self.centerLayout.setCurrentIndex(0)
        elif string == "img":
            self.centerLayout.setCurrentIndex(1)
        elif string == "hardware":
            self.centerLayout.setCurrentIndex(2)
        elif string == "point":
            self.centerLayout.setCurrentIndex(3)
        elif string == "review":
            self.centerLayout.setCurrentIndex(4)

    # API：设置7天能耗表
    def set_7day_chart(self, list_data):
        self.figure.patch.set_facecolor('#F4F4F4')
        rect = [0, 0, 1, 1]
        ax = self.figure.add_axes(rect)
        x = [1, 2, 3, 4, 5, 6, 7]
        y = list_data
        plt.axis('off')
        cm = ax.bar(x, y, color='#c6eab2')
        for rect in cm:
            height = rect.get_height()
            plt.text(rect.get_x() + rect.get_width() / 2.0 - 0.30, 0, '%s' % int(height), size=12,
                    family="Arial Rounded MT Bold", color='white')

    # API：设置小车在电子地图上的位置
    def set_map_location(self, list_data):
        self.locModule.js_run(list_data[0], list_data[1])

    # API：设置小车的速度
    def set_velocity(self, data):
        self.rtVelocityValue.setText("    " + data + "m/s")

    # API：改变控制模式
    def change_control_mode(self, flag):
        if flag:
            self.connectBtn.setText("控制开启")
        else:
            self.connectBtn.setText("控制关闭")


    # API：接收传输的图像信息，用于显示
    def show_img(self, show_image):
        self.imgModule.imgLabel.setPixmap(QPixmap.fromImage(show_image))
        self.imgModule.set_fps(0)

