from PyQt5.QtGui import QKeySequence
from PyQt5.QtNetwork import QTcpSocket
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import register_ui
import base_pb2
import random


class Register(QWidget, register_ui.Ui_Form):
    def __init__(self, _login, parent=None):
        super(Register, self).__init__(parent)
        self.setupUi(self)
        self._login = _login
        self.setWindowTitle('五子棋')
        self.pushButton.clicked.connect(self.login)
        self.pushButton_3.clicked.connect(self.quit)
        self.pushButton.setShortcut(QKeySequence(Qt.Key_Enter))
        self.pushButton.setShortcut(QKeySequence(Qt.Key_Return))
        self.setFixedSize(self.width(), self.height())

    def login(self):
        client_register = base_pb2.client_register()
        client_register.cmd = 4
        client_register.username = self.lineEdit.text()
        client_register.passwd = self.lineEdit_2.text()
        client_register.nicheng = self.lineEdit_4.text()
        client_register.email = self.lineEdit_5.text()
        client_register.touxiang = str(random.randint(1, 10))
        passwd2 = self.lineEdit_3.text()
        if client_register.passwd != passwd2:
            QMessageBox.warning(self, '警告', '两次输入的密码不一致', QMessageBox.Ok)
            return
        if client_register.username == '' or client_register.passwd == '' or passwd2 == '':
            QMessageBox.warning(self, '警告', '请填入全部信息', QMessageBox.Ok)
            return
        if client_register.username == "" and client_register.passwd == "" and client_register.nicheng == "" and client_register.email == "":
            QMessageBox.warning(self, '警告', '还有信息未填', QMessageBox.Ok)
        self._login.writeData(client_register.SerializeToString())

    def quit(self):
        self.close()
        self._login.show()
