#!/bin/python3

from ipaddress import IPv4Address
from time import sleep
from pyairmore.request import AirmoreSession
from pyairmore.services.messaging import MessagingService
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(567, 441)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridFrame = QtWidgets.QFrame(self.centralwidget)
        self.gridFrame.setGeometry(QtCore.QRect(10, 10, 541, 41))
        self.gridFrame.setObjectName("gridFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.gridFrame)
        self.gridLayout.setObjectName("gridLayout")
        self.label_port = QtWidgets.QLabel(self.gridFrame)
        self.label_port.setObjectName("label_port")
        self.gridLayout.addWidget(self.label_port, 0, 3, 1, 1)
        self.label_ip = QtWidgets.QLabel(self.gridFrame)
        self.label_ip.setObjectName("label_ip")
        self.gridLayout.addWidget(self.label_ip, 0, 1, 1, 1)
        self.ip_input = QtWidgets.QLineEdit(self.gridFrame)
        self.ip_input.setObjectName("ip_input")
        self.gridLayout.addWidget(self.ip_input, 0, 2, 1, 1)
        self.port_input = QtWidgets.QLineEdit(self.gridFrame)
        self.port_input.setObjectName("port_input")
        self.gridLayout.addWidget(self.port_input, 0, 4, 1, 1)
        self.horizontalWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalWidget.setGeometry(QtCore.QRect(10, 60, 541, 61))
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.connect = QtWidgets.QPushButton(self.horizontalWidget)
        self.connect.setObjectName("connect")
        self.horizontalLayout.addWidget(self.connect)
        self.status_connection = QtWidgets.QTextBrowser(self.horizontalWidget)
        self.status_connection.setObjectName("status_connection")
        self.horizontalLayout.addWidget(self.status_connection)
        self.gridFrame_2 = QtWidgets.QFrame(self.centralwidget)
        self.gridFrame_2.setGeometry(QtCore.QRect(10, 130, 541, 111))
        self.gridFrame_2.setObjectName("gridFrame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridFrame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.number_input = QtWidgets.QLineEdit(self.gridFrame_2)
        self.number_input.setObjectName("number_input")
        self.gridLayout_2.addWidget(self.number_input, 0, 1, 1, 1)
        self.count_label = QtWidgets.QLabel(self.gridFrame_2)
        self.count_label.setObjectName("count_label")
        self.gridLayout_2.addWidget(self.count_label, 1, 0, 1, 1)
        self.content_lable = QtWidgets.QLabel(self.gridFrame_2)
        self.content_lable.setObjectName("content_lable")
        self.gridLayout_2.addWidget(self.content_lable, 0, 2, 1, 1)
        self.count_input = QtWidgets.QLineEdit(self.gridFrame_2)
        self.count_input.setObjectName("count_input")
        self.gridLayout_2.addWidget(self.count_input, 1, 1, 1, 1)
        self.target_phone_label = QtWidgets.QLabel(self.gridFrame_2)
        self.target_phone_label.setObjectName("target_phone_label")
        self.gridLayout_2.addWidget(self.target_phone_label, 0, 0, 1, 1)
        self.content_input = QtWidgets.QTextEdit(self.gridFrame_2)
        self.content_input.setObjectName("content_input")
        self.gridLayout_2.addWidget(self.content_input, 0, 3, 2, 1)
        self.message_send_status = QtWidgets.QTextBrowser(self.centralwidget)
        self.message_send_status.setGeometry(QtCore.QRect(10, 290, 541, 91))
        self.message_send_status.setObjectName("message_send_status")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(90, 250, 191, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.send = QtWidgets.QPushButton(self.centralwidget)
        self.send.setGeometry(QtCore.QRect(10, 250, 71, 25))
        self.send.setObjectName("send")
        self.sended_lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.sended_lcd.setGeometry(QtCore.QRect(300, 250, 64, 23))
        self.sended_lcd.setObjectName("sended_lcd")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 567, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        self.connect.clicked.connect(self.connecting)
        self.send.clicked.connect(self.sending)
        #self.send.clicked.connect(self.percent)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_port.setText(_translate("MainWindow", "port:"))
        self.label_ip.setText(_translate("MainWindow", "ip:"))
        self.port_input.setInputMask(_translate("MainWindow", "2333"))
        self.connect.setText(_translate("MainWindow", "connect"))
        self.count_label.setText(_translate("MainWindow", "count:"))
        self.content_lable.setText(_translate("MainWindow", "content:"))
        self.target_phone_label.setText(_translate("MainWindow", "target phone:"))
        self.send.setText(_translate("MainWindow", "send"))

    def connecting(self):
        try:
            ip = str(self.ip_input.text())
            port = int(self.port_input.text())
            ip4 = IPv4Address(ip)
            session = AirmoreSession(ip4 ,port)
            if session.is_server_running:
                self.status_connection.append("server is up")
            if session.request_authorization():
                self.status_connection.append("you are connect to phone")
        except:
            self.status_connection.append("check the connection")

    def sending(self):
        try:
            ip = str(self.ip_input.text())
            port = int(self.port_input.text())
            ip4 = IPv4Address(ip)
            phone_number = str(self.number_input.text())
            count_massage = int(self.count_input.text())
            message = str(self.content_input.toPlainText())
            session = AirmoreSession(ip4 ,port)
            service = MessagingService(session)
            try :
                for c in range(1,count_massage+1):
                    service.send_message(phone_number, message)
                    percent = (c/count_massage)*100
                    self.progressBar.setValue(percent)
                    self.message_send_status.append("message %i sended" %c )
                    self.sended_lcd.display(c)
            except:
                self.message_send_status.append("the message not send. check the information.")
        except:
            self.message_send_status.append("check the connection")
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
