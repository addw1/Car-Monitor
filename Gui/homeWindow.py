
from PyQt5.QtWidgets import QWidget, QFrame, QVBoxLayout
from PyQt5.QtGui import QPixmap
from homeWindow_ui import Ui_HomeWindow
from homeLogFrame_ui import Ui_HomeLog


class HomeWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_HomeWindow()
        self.ui.setupUi(self)

        self.index = 0
        # car button init
        self.btnCarA = self.ui.btn_carA
        self.btnCarB = self.ui.btn_carB
        self.btnCarC = self.ui.btn_carC
        self.btnCarD = self.ui.btn_carD

        # scroll view init
        self.scrollLog = self.ui.wid_logContent
        self.scrollLayout = QVBoxLayout()

        # add log
        self.logList = []
        self.add_log("girl1.png", "Jenny", "吉林大学前卫校区", "2023-03-01", "自动驾驶")
        self.add_log("boy2.png", "Ben", "吉林大学前卫校区", "2023-03-03", "目标检测")
        self.add_log("boy1.png", "Tommy", "吉林大学前卫校区", "2023-03-05", "slam建图")
        self.scrollLog.setLayout(self.scrollLayout)

        # change name of car
        self.set_car_info(1, "测试车一号", "Linux", "STM32F7")
        self.set_car_info(2, "空", "空", "空")

    def add_log(self, img_name, name, place, date, content):
        self.index = self.index + 1
        logCard = HomeLog()
        logCard.set_img(img_name)
        logCard.set_info(name, place, date, content)
        self.scrollLayout.addWidget(logCard)
        if self.index == 4:
            item = self.scrollLayout.itemAt(0)
            self.scrollLayout.removeItem(item)
            if item.widget():
                item.widget().deleteLater()

    def set_car_info(self, car_index, car_name, car_os, car_micro):
        if car_index == 1:
            self.ui.label_carAOs.setText("操作系统: " + car_os)
            self.ui.label_carAMicro.setText("芯片: " + car_micro)
            self.btnCarA.setText(car_name)
        elif car_index == 2:
            self.ui.label_CarBOs.setText("操作系统: " + car_os)
            self.ui.label_CarBMicro.setText("芯片: " + car_micro)
            self.btnCarB.setText(car_name)
        elif car_index == 3:
            self.ui.label_CarCOs.setText("操作系统: " + car_os)
            self.ui.label_CarCMicro.setText("芯片: " + car_micro)
            self.btnCarC.setText(car_name)
        else:
            self.ui.label_carDOs.setText("操作系统: " + car_os)
            self.ui.label_carDMicro.setText("芯片: " + car_micro)
            self.btnCarD.setText(car_name)


class HomeLog(QFrame):
    def __init__(self):
        super().__init__()
        # 完成UI的基本样式设置
        self.ui = Ui_HomeLog()
        self.ui.setupUi(self)
        # member init
        self.img = self.ui.label_imgName
        self.labName = self.ui.label_logPerson
        self.labTest = self.ui.label_logTest
        self.labPlace = self.ui.label_logPlace
        self.labDate = self.ui.label_logTime

    def set_info(self, str_name, str_place, str_date, str_test):
        self.labName.setText("姓名: " + str_name)
        self.labTest.setText("测试内容: " + str_test)
        self.labPlace.setText("地点: " + str_place)
        self.labDate.setText("日期: " + str_date)

    def set_img(self, img_file_path):
        self.img.setPixmap(QPixmap("./QtUiFile/img/head/" + img_file_path))
