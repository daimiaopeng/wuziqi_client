from PyQt5.QtNetwork import QTcpSocket
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import register_ui
import base_pb2


class Register(QWidget, register_ui.Ui_Form):
    def __init__(self, _login, parent=None):
        super(Register, self).__init__(parent)
        self.setupUi(self)
        self._login = _login
        self.setWindowTitle('五子棋')
        self.pushButton.clicked.connect(self.login)

    def login(self):
        client_register = base_pb2.client_register()
        client_register.cmd = 4
        client_register.username = self.lineEdit.text()
        client_register.passwd = self.lineEdit_2.text()
        passwd2 = self.lineEdit_3.text()

        while True:
            pass

        if client_register.passwd != passwd2:
            QMessageBox.warning(self, '警告', '两次输入的密码不一致', QMessageBox.Ok)
            return
        if client_register.username == '' or client_register.passwd == '' or passwd2 == '':
            QMessageBox.warning(self, '警告', '请填入全部信息', QMessageBox.Ok)
            return
        self._login.writeData(client_register.SerializeToString())
