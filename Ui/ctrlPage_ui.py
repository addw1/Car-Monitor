# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ctrlPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class CtrlPageUi(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1171, 582)
        Form.setStyleSheet("background-color: #F4F4F4;")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1171, 581))
        self.frame.setStyleSheet("background-color:#FFFFFF;\n"
"border-radius: 40px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(320, 80, 571, 461))
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 490, 20, 20))
        self.label_3.setStyleSheet("background-image:url(:/icon/lightIcon.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.progressBar = QtWidgets.QProgressBar(self.frame)
        self.progressBar.setGeometry(QtCore.QRect(40, 490, 101, 16))
        self.progressBar.setStyleSheet("QProgressBar{\n"
"    background-color: #ECECEB;\n"
"    border-radius:5px;\n"
"\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #5ADE00;\n"
"    border-radius:5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QProgressBar::chunk::label {\n"
"    color: black;\n"
"    font-weight: bold;\n"
"    font-size: 10pt;\n"
"}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.frame_7 = QtWidgets.QFrame(self.frame)
        self.frame_7.setGeometry(QtCore.QRect(290, 10, 511, 21))
        self.frame_7.setStyleSheet("background-color:rgba(236,236,236,0.7);\n"
"border-radius: 10px;")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.label_5 = QtWidgets.QLabel(self.frame_7)
        self.label_5.setGeometry(QtCore.QRect(10, 0, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Hei")
        font.setPointSize(13)
        font.setItalic(False)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_18 = QtWidgets.QLabel(self.frame_7)
        self.label_18.setGeometry(QtCore.QRect(430, 0, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Hei")
        font.setPointSize(13)
        font.setItalic(False)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.frame_7)
        self.label_19.setGeometry(QtCore.QRect(80, -2, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Hei")
        font.setPointSize(13)
        font.setItalic(False)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(110, 30, 71, 71))
        font = QtGui.QFont()
        font.setFamily(".Diwan Kufi PUA")
        font.setPointSize(60)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: #61B0FF")
        self.label_4.setObjectName("label_4")
        self.label_20 = QtWidgets.QLabel(self.frame)
        self.label_20.setGeometry(QtCore.QRect(130, 100, 60, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.tabWidget = QtWidgets.QTabWidget(self.frame)
        self.tabWidget.setGeometry(QtCore.QRect(20, 140, 251, 321))
        self.tabWidget.setStyleSheet("QTabBar::tab {\n"
"    border:none;\n"
"    border-radius: 8px;\n"
"    min-width: 8ex;\n"
"    padding: 5px;\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background-color: #ECECEC;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    border-color: #000000;\n"
"}")
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_24 = QtWidgets.QLabel(self.tab)
        self.label_24.setGeometry(QtCore.QRect(32, 30, 211, 241))
        self.label_24.setStyleSheet("background-image:url(:/carImg/carBackSp.png)")
        self.label_24.setText("")
        self.label_24.setObjectName("label_24")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(27, 30, 201, 231))
        self.label_2.setStyleSheet("background-image:url(:/carImg/carBackView.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(920, 80, 221, 461))
        self.frame_3.setStyleSheet("")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_5.setText(_translate("Form", "12:30am"))
        self.label_18.setText(_translate("Form", "WiFi 📶"))
        self.label_19.setText(_translate("Form", "☁️多云   18°～29°"))
        self.label_4.setText(_translate("Form", "18 "))
        self.label_20.setText(_translate("Form", "km/h"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "运动模式"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "标准模式"))

import picture_rc
