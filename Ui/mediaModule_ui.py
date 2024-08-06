# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mediaModule.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class MediaModuleUi(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(491, 431)
        Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pushButton = QtWidgets.QPushButton(Frame)
        self.pushButton.setGeometry(QtCore.QRect(30, 350, 71, 32))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(0, 121, 136,100);\n"
"    border:1px outset rgb(255, 255, 255);\n"
"    border-radius:8px;\n"
"      text-align: center center;\n"
"} \n"
"/*鼠标放在按钮上方*/\n"
"QPushButton:hover {\n"
"    background-color: rgba(0, 121, 136, 80%);\n"
"    border:2px outset rgba(36, 36, 36,0);\n"
"} \n"
"QPushButton:pressed {\n"
"    background-color: rgba(0, 121, 136,90%);\n"
"    border:4px outset rgba(36, 36, 36,0);\n"
"} ")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Frame)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 350, 71, 32))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(211, 105, 0,100);\n"
"    border:1px outset rgb(255, 255, 255);\n"
"    border-radius:8px;\n"
"      text-align: center center;\n"
"} \n"
"/*鼠标放在按钮上方*/\n"
"QPushButton:hover {\n"
"    background-color: rgba(211, 105, 0,80%);\n"
"    border:2px outset rgba(36, 36, 36,0);\n"
"} \n"
"QPushButton:pressed {\n"
"    background-color: rgba(211, 105, 0, 90%);\n"
"    border:4px outset rgba(36, 36, 36,0);\n"
"} ")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalSlider = QtWidgets.QSlider(Frame)
        self.horizontalSlider.setGeometry(QtCore.QRect(20, 320, 441, 22))
        self.horizontalSlider.setStyleSheet("/*滑块整体样式*/\n"
"QSlider {\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    border-radius: 8px;\n"
"}\n"
"/*还未滑过的地方*/\n"
"QSlider::add-page:horizontal {\n"
"    background-color: rgb(244, 244, 244);\n"
"border-radius: 2px;\n"
"}\n"
"/*已经滑过的地方*/\n"
"QSlider::sub-page:horizontal {\n"
"}\n"
"/*滑块沟槽部分*/\n"
"QSlider::groove:horizontal {\n"
"    background-color: rgb(93, 207, 239);\n"
"    height: 6px;\n"
"    border-radius: 2px;\n"
"}\n"
"/*滑块*/\n"
"QSlider::handle:horizontal {\n"
"    image: url(:/hardware/car2.png);\n"
"    width: 35px;\n"
"    height: 33px;\n"
"    margin: -14px  0px -14px 0px;\n"
"}\n"
"\n"
"")
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.widget = QVideoWidget(Frame)
        self.widget.setGeometry(QtCore.QRect(20, 20, 441, 281))
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet("border:none;")
        self.widget.setObjectName("widget")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.pushButton.setText(_translate("Frame", "播放"))
        self.pushButton_2.setText(_translate("Frame", "暂停"))
from PyQt5.QtMultimediaWidgets import QVideoWidget
import picture_rc