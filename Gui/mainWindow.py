from main_ui import MainWindowUi
from mainPage import MainPage
from PyQt5.QtCore import QThread, QTimer, Qt
from client import Subscriber, ImgSubscriber, Publisher
from PyQt5.QtWidgets import QStackedLayout,QFrame


class MainWindow(QFrame):
    def __init__(self):
        super().__init__()
        # 加载UI文件
        self.ui = MainWindowUi()
        self.ui.setupUi(self)

        # 初始化组件成员
        # 上半部分容器
        self.mainContainer = self.ui.frame_10
        self.layout = QStackedLayout()
        self.mainContainer.setLayout(self.layout)
        self.mainPage = MainPage()
        self.layout.addWidget(self.mainPage)
        # 下半部分容器
        self.bottomContainer = self.ui.frame_9
        # 初始化各个按钮，按钮位于下半部分容器中
        self.toNavBtn = self.ui.pushButton
        self.toImgBtn = self.ui.pushButton_6
        self.toIogBtn = self.ui.pushButton_5
        self.toRadarBtn = self.ui.pushButton_7
        self.to3DBtn = self.ui.pushButton_8
        self.toPointBtn = self.ui.pushButton_7
        self.toReviewBtn = self.ui.pushButton_2
        # 初始化按钮
        self.btn_init()
        # 开启远程控制：controlFlag = True 关闭远程控制：controlFlag = False
        self.controlFlag = False

        list_data = [24, 34, 56, 34, 25, 62, 45]
        self.set_chart(list_data)
        ''' 需要修改
        # get 7 days data
        # !! write your get data function !!
        list_data = [24, 34, 56, 34, 25, 62, 45]
        self.mainPage.set_7day_chart(list_data)
        '''

        # 订阅线程
        self.subThread = QThread()
        self.subscriber = Subscriber()
        self.subscriber.moveToThread(self.subThread)
        # 发布线程
        self.pubThread = QThread()
        self.publisher = Publisher()
        self.publisher.moveToThread(self.pubThread)
        # 图像接收线程
        self.imgSubThread = QThread()
        self.imgSubscriber = ImgSubscriber()
        self.imgSubscriber.moveToThread(self.imgSubThread)
        # 初始化所有线程
        self.thread_init()
        # 启动所有线程
        self.thread_start()

    def thread_init(self):
        #位置/速度信息
        self.subscriber.velocity_to_main_signal.connect(self.update_data)
        self.subscriber.location_to_main_signal.connect(self.update_data)
        self.subscriber.start_thread_signal.connect(self.subscriber.work)
        # 控制命令
        self.publisher.control_to_ros_signal.connect(self.publisher.control)
        self.publisher.start_thread_signal.connect(self.publisher.work)
        # 图像信息
        self.imgSubscriber.img_show_signal.connect(self.mainPage.show_img)
        self.imgSubscriber.start_thread_signal.connect(self.imgSubscriber.work)

    def thread_start(self):
        # 启动订阅线程
        self.subThread.start()
        self.subscriber.start_thread_signal.emit()
        # 启动图像接收线程
        self.imgSubThread.start()
        self.imgSubscriber.start_thread_signal.emit()
        # 启动发布线程
        self.pubThread.start()
        self.publisher.start_thread_signal.emit()

    # 将按钮与change_module函数进行连接，既按钮每点击一次会触发一次change_module函数。
    def btn_init(self):
        # add logic for btn
        self.toNavBtn.clicked.connect(lambda: self.change_module("location"))
        self.toImgBtn.clicked.connect(lambda: self.change_module("img"))
        self.to3DBtn.clicked.connect(lambda: self.change_module("hardware"))
        self.toPointBtn.clicked.connect(lambda: self.change_module("point"))
        self.toReviewBtn.clicked.connect(lambda: self.change_module("review"))
        self.mainPage.connectBtn.clicked.connect(self.change_control_model)

    # 根据传入的参数进行页面切换
    def change_module(self, string):
        self.mainPage.set_center_content(string)

    # 开启 或者 关闭 远程控制功能
    def change_control_model(self):
        self.controlFlag = not self.controlFlag
        # send it to mainPage
        self.mainPage.change_control_mode(self.controlFlag)

    # 更新速度及位置信息
    def update_data(self, string_type, string_value):
        if string_type == "velocity":
            self.mainPage.set_velocity(string_value)
        elif string_type == "location":
            list_data = string_value.split(" ")
            self.mainPage.set_map_location(list_data)

    # def set chart
    def set_chart(self, listdata):
        self.mainPage.set_7day_chart(listdata)

    # 读取远程控制命令
    def keyPressEvent(self, event):
        # 先判断是否开启远程控制功能
        if self.controlFlag:
            # 获取键盘按键值
            key = event.key()
            # 将按键值转换为字符串
            key = chr(Qt.Key(key))
            # 转小写并发出
            key = key.lower()
            self.publisher.control_to_ros_signal.emit(key)
