#!/bin/python3

from ipaddress import IPv4Address
from time import sleep
from pyairmore.request import AirmoreSession
from pyairmore.services.messaging import MessagingService
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(601, 425)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridFrame = QtWidgets.QFrame(self.centralwidget)
        self.gridFrame.setObjectName("gridFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.gridFrame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_ip = QtWidgets.QLabel(self.gridFrame)
        self.label_ip.setObjectName("label_ip")
        self.horizontalLayout_2.addWidget(self.label_ip)
        self.ip_input = QtWidgets.QLineEdit(self.gridFrame)
        self.ip_input.setObjectName("ip_input")
        self.horizontalLayout_2.addWidget(self.ip_input)
        self.label_port = QtWidgets.QLabel(self.gridFrame)
        self.label_port.setObjectName("label_port")
        self.horizontalLayout_2.addWidget(self.label_port)
        self.port_input = QtWidgets.QLineEdit(self.gridFrame)
        self.port_input.setObjectName("port_input")
        self.horizontalLayout_2.addWidget(self.port_input)
        self.gridLayout_2.addWidget(self.gridFrame, 0, 0, 1, 3)
        self.horizontalWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.connect = QtWidgets.QPushButton(self.horizontalWidget)
        self.connect.setObjectName("connect")
        self.horizontalLayout.addWidget(self.connect)
        self.status_connection = QtWidgets.QTextBrowser(self.horizontalWidget)
        self.status_connection.setObjectName("status_connection")
        self.horizontalLayout.addWidget(self.status_connection)
        self.gridLayout_2.addWidget(self.horizontalWidget, 1, 0, 1, 3)
        self.gridFrame_2 = QtWidgets.QFrame(self.centralwidget)
        self.gridFrame_2.setObjectName("gridFrame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.gridFrame_2)
        self.gridLayout.setObjectName("gridLayout")
        self.target_phone_label = QtWidgets.QLabel(self.gridFrame_2)
        self.target_phone_label.setObjectName("target_phone_label")
        self.gridLayout.addWidget(self.target_phone_label, 0, 0, 1, 1)
        self.number_input = QtWidgets.QLineEdit(self.gridFrame_2)
        self.number_input.setObjectName("number_input")
        self.gridLayout.addWidget(self.number_input, 0, 1, 1, 1)
        self.content_lable = QtWidgets.QLabel(self.gridFrame_2)
        self.content_lable.setObjectName("content_lable")
        self.gridLayout.addWidget(self.content_lable, 0, 2, 1, 1)
        self.content_input = QtWidgets.QTextEdit(self.gridFrame_2)
        self.content_input.setObjectName("content_input")
        self.gridLayout.addWidget(self.content_input, 0, 3, 2, 1)
        self.count_label = QtWidgets.QLabel(self.gridFrame_2)
        self.count_label.setObjectName("count_label")
        self.gridLayout.addWidget(self.count_label, 1, 0, 1, 1)
        self.count_input = QtWidgets.QLineEdit(self.gridFrame_2)
        self.count_input.setObjectName("count_input")
        self.gridLayout.addWidget(self.count_input, 1, 1, 1, 1)
        self.gridLayout_2.addWidget(self.gridFrame_2, 2, 0, 1, 3)
        self.send = QtWidgets.QPushButton(self.centralwidget)
        self.send.setObjectName("send")
        self.gridLayout_2.addWidget(self.send, 3, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        #self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_2.addWidget(self.progressBar, 3, 1, 1, 1)
        self.sended_lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.sended_lcd.setObjectName("sended_lcd")
        self.gridLayout_2.addWidget(self.sended_lcd, 3, 2, 1, 1)
        self.message_send_status = QtWidgets.QTextBrowser(self.centralwidget)
        self.message_send_status.setObjectName("message_send_status")
        self.gridLayout_2.addWidget(self.message_send_status, 4, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.connect.clicked.connect(self.connecting)
        self.send.clicked.connect(self.sending)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_ip.setText(_translate("MainWindow", "ip:"))
        self.label_port.setText(_translate("MainWindow", "port:"))
        self.port_input.setInputMask(_translate("MainWindow", "2333"))
        self.connect.setText(_translate("MainWindow", "connect"))
        self.target_phone_label.setText(_translate("MainWindow", "target phone:"))
        self.content_lable.setText(_translate("MainWindow", "content:"))
        self.count_label.setText(_translate("MainWindow", "count:"))
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
                    self.progressBar.setProperty("value", percent)
                    self.message_send_status.append("message %i sended" %c )
                    self.sended_lcd.display(c)
                    sleep(1)
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