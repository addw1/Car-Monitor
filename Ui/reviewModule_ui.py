# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reviewModule.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class ReviewModuleUi(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(513, 511)
        Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pushButton = QtWidgets.QPushButton(Frame)
        self.pushButton.setGeometry(QtCore.QRect(10, 20, 113, 32))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(0, 211, 106,100);\n"
"    border:1px outset rgb(255, 255, 255);\n"
"    border-radius:8px;\n"
"      text-align: center center;\n"
"} \n"
"/*鼠标放在按钮上方*/\n"
"QPushButton:hover {\n"
"    background-color: rgba(0, 211, 106,80%);\n"
"    border:2px outset rgba(36, 36, 36,0);\n"
"} \n"
"QPushButton:pressed {\n"
"    background-color: rgba(0, 211, 106,90%);\n"
"    border:4px outset rgba(36, 36, 36,0);\n"
"} ")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Frame)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 20, 113, 32))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(255, 51, 153,125);\n"
"    border:1px outset rgb(255, 255, 255);\n"
"    border-radius:8px;\n"
"      text-align: center center;\n"
"} \n"
"/*鼠标放在按钮上方*/\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 51, 153,80%);\n"
"    border:2px outset rgba(36, 36, 36,0);\n"
"} \n"
"QPushButton:pressed {\n"
"    background-color: rgba(255, 51, 153,90%);\n"
"    border:4px outset rgba(36, 36, 36,0);\n"
"} ")
        self.pushButton_2.setObjectName("pushButton_2")
        self.frame = QtWidgets.QFrame(Frame)
        self.frame.setGeometry(QtCore.QRect(10, 60, 491, 431))
        self.frame.setStyleSheet("border:none;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_3 = QtWidgets.QPushButton(Frame)
        self.pushButton_3.setGeometry(QtCore.QRect(442, 20, 61, 32))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(0, 106, 211,100);\n"
"    border:1px outset rgb(255, 255, 255);\n"
"    border-radius:8px;\n"
"      text-align: center center;\n"
"} \n"
"/*鼠标放在按钮上方*/\n"
"QPushButton:hover {\n"
"    background-color: rgba(0, 106, 211,80%);\n"
"    border:2px outset rgba(36, 36, 36,0);\n"
"} \n"
"QPushButton:pressed {\n"
"    background-color: rgba(0, 106, 211,90%);\n"
"    border:4px outset rgba(36, 36, 36,0);\n"
"} ")
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.pushButton.setText(_translate("Frame", "轨迹回放"))
        self.pushButton_2.setText(_translate("Frame", "视频回放"))
        self.pushButton_3.setText(_translate("Frame", "load"))