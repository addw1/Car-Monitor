
import sys
from PyQt5.QtWidgets import QMainWindow, QStackedLayout
from mainWindow_ui import Ui_MainWindow
from manageWindow import ManageWindow
from homeWindow import HomeWindow
from locationWindow import LocationWindow
from cloudWindow import CloudWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 加载UI文件
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.hide_up(False)
        # 页面
        self.page = self.ui.frame_show
        self.homePage = HomeWindow()
        self.managePage = ManageWindow()
        self.locationPage = LocationWindow()
        self.cloudPage = CloudWindow()
        # 堆页面
        self.stack_layout = QStackedLayout()
        self.stack_layout.addWidget(self.homePage)
        self.stack_layout.addWidget(self.managePage)
        self.stack_layout.addWidget(self.locationPage)
        self.stack_layout.addWidget(self.cloudPage)
        # 设置主框架排布
        self.page.setLayout(self.stack_layout)
        # 列表初始化
        self.pageChoice = self.ui.listWidget_static
        self.pageChoiceDown = self.ui.listWidget_dynamic
        self.pageChoice.itemClicked.connect(self.change_page)
        self.pageChoiceDown.itemClicked.connect(self.change_page_down)

    # 页面切换函数 上半部分
    def change_page(self):
        item = self.pageChoice.selectedItems()[0]
        if item.text() == "车辆管理":
            self.stack_layout.setCurrentIndex(1)
        elif item.text() == "主页":
            self.stack_layout.setCurrentIndex(0)
        elif item.text() == "数据可视化":
            self.stack_layout.setCurrentIndex(3)

    # 页面切换函数 下半部分
    def change_page_down(self):
        item = self.pageChoiceDown.selectedItems()[0]
        if item.text() == "实时定位":
            self.stack_layout.setCurrentIndex(2)

    # 隐藏上边框 hide： True  不隐藏 hide：False
    def hide_up(self, hide):
        if hide:
            self.pushButton.clicked.connect(self.exit)
        else:
            self.ui.pushButton_red.setVisible(False)
            self.ui.pushButton_green.setVisible(False)
            self.ui.pushButton_yellow.setVisible(False)

    def exit(self):
        sys.exit()
