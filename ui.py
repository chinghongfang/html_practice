# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Project.ui',
# licensing of 'Project.ui' applies.
#
# Created: Wed Dec 18 19:40:09 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(873, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 381, 401))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.Speed_Slider = QtWidgets.QSlider(self.frame)
        self.Speed_Slider.setGeometry(QtCore.QRect(30, 90, 221, 22))
        self.Speed_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.Speed_Slider.setObjectName("Speed_Slider")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(40, 40, 101, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(40, 150, 81, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(40, 210, 91, 51))
        self.label_4.setObjectName("label_4")
        self.checkBox_1 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_1.setGeometry(QtCore.QRect(120, 160, 61, 20))
        self.checkBox_1.setObjectName("checkBox_1")
        self.checkBox_2 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_2.setGeometry(QtCore.QRect(190, 160, 61, 20))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_3.setGeometry(QtCore.QRect(260, 160, 61, 20))
        self.checkBox_3.setObjectName("checkBox_3")
        self.label_speed = QtWidgets.QLabel(self.frame)
        self.label_speed.setGeometry(QtCore.QRect(290, 90, 60, 16))
        self.label_speed.setObjectName("label_speed")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(30, 290, 131, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 290, 131, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(10, 420, 381, 131))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_qrcode = QtWidgets.QLabel(self.frame_2)
        self.label_qrcode.setGeometry(QtCore.QRect(30, 0, 151, 131))
        self.label_qrcode.setText("")
        self.label_qrcode.setObjectName("label_qrcode")
        self.btn_qrcode = QtWidgets.QPushButton(self.frame_2)
        self.btn_qrcode.setGeometry(QtCore.QRect(220, 20, 131, 91))
        self.btn_qrcode.setObjectName("btn_qrcode")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(400, 10, 461, 541))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 111, 41))
        self.label_7.setObjectName("label_7")
        self.textBrowser = QtWidgets.QTextBrowser(self.frame_3)
        self.textBrowser.setGeometry(QtCore.QRect(10, 60, 441, 471))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 873, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "彈幕速度", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", "字體大小", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("MainWindow", "字型", None, -1))
        self.checkBox_1.setText(QtWidgets.QApplication.translate("MainWindow", "大", None, -1))
        self.checkBox_2.setText(QtWidgets.QApplication.translate("MainWindow", "中", None, -1))
        self.checkBox_3.setText(QtWidgets.QApplication.translate("MainWindow", "小", None, -1))
        self.label_speed.setText(QtWidgets.QApplication.translate("MainWindow", "0", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "PushButton", None, -1))
        self.pushButton_2.setText(QtWidgets.QApplication.translate("MainWindow", "PushButton", None, -1))
        self.btn_qrcode.setText(QtWidgets.QApplication.translate("MainWindow", "PushButton", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("MainWindow", "訊息", None, -1))
