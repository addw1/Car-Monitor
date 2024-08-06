# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'homeLogFrame.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HomeLog(object):
    def setupUi(self, frame_log):
        frame_log.setObjectName("frame_log")
        frame_log.resize(628, 167)
        frame_log.setStyleSheet("QFrame#frame_log{\n"
"    border:none;\n"
"    border-radius:12px ;\n"
"    background-color:rgb(255,255,255);\n"
"\n"
"}")
        frame_log.setFrameShape(QtWidgets.QFrame.StyledPanel)
        frame_log.setFrameShadow(QtWidgets.QFrame.Raised)
        self.verticalLayoutWidget = QtWidgets.QWidget(frame_log)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(120, 30, 253, 102))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verLay_LogInfo = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verLay_LogInfo.setContentsMargins(0, 0, 0, 0)
        self.verLay_LogInfo.setObjectName("verLay_LogInfo")
        self.label_logPerson = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_logPerson.setFont(font)
        self.label_logPerson.setStyleSheet("color:rgb(0,0,0)")
        self.label_logPerson.setObjectName("label_logPerson")
        self.verLay_LogInfo.addWidget(self.label_logPerson)
        self.label_logPlace = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_logPlace.setFont(font)
        self.label_logPlace.setAutoFillBackground(False)
        self.label_logPlace.setStyleSheet("color:rgb(0,0,0)")
        self.label_logPlace.setObjectName("label_logPlace")
        self.verLay_LogInfo.addWidget(self.label_logPlace)
        self.label_logTime = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_logTime.setFont(font)
        self.label_logTime.setStyleSheet("color:rgb(0,0,0)")
        self.label_logTime.setObjectName("label_logTime")
        self.verLay_LogInfo.addWidget(self.label_logTime)
        self.label_logTest = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_logTest.setFont(font)
        self.label_logTest.setStyleSheet("color:rgb(0,0,0)")
        self.label_logTest.setObjectName("label_logTest")
        self.verLay_LogInfo.addWidget(self.label_logTest)
        self.label_imgName = QtWidgets.QLabel(frame_log)
        self.label_imgName.setGeometry(QtCore.QRect(20, 40, 82, 82))
        self.label_imgName.setStyleSheet("")
        self.label_imgName.setText("")
        self.label_imgName.setObjectName("label_imgName")
        self.label_imgCar = QtWidgets.QLabel(frame_log)
        self.label_imgCar.setGeometry(QtCore.QRect(410, 30, 170, 101))
        self.label_imgCar.setStyleSheet("")
        self.label_imgCar.setText("")
        self.label_imgCar.setObjectName("label_imgCar")

        self.retranslateUi(frame_log)
        QtCore.QMetaObject.connectSlotsByName(frame_log)

    def retranslateUi(self, frame_log):
        _translate = QtCore.QCoreApplication.translate
        frame_log.setWindowTitle(_translate("frame_log", "Frame"))
        self.label_logPerson.setText(_translate("frame_log", "操作人员: Qingning Zeng"))
        self.label_logPlace.setText(_translate("frame_log", "地点: 飞跃路"))
        self.label_logTime.setText(_translate("frame_log", "时间: 2023-03-01"))
        self.label_logTest.setText(_translate("frame_log", "测试内容: 基于激光雷达的slam建图"))