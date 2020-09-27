from PyQt5.QtGui import QKeySequence
from PyQt5.QtNetwork import QTcpSocket
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import login_ui
import sys
import socket
import base_pb2
import register
import game


# pyuic5 -o login_ui.py login.ui
# pyuic5 -o main_ui.py main.ui
# pyuic5 -o register_ui.py register.ui
# pyinstaller -F --icon=ui.ico main.py --noconsole

class MyWindow(QMainWindow, login_ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('五子棋')
        self.pushButton.clicked.connect(self.login)
        self.pushButton_2.clicked.connect(self.register)
        self.ip = '127.0.0.1'
        self.port = 9123
        self.sock = QTcpSocket(self)
        self.sock.connectToHost(self.ip, self.port)
        self.sock.readyRead.connect(self.readData)
        self.pushButton.setShortcut(QKeySequence(Qt.Key_Enter))
        self.pushButton.setShortcut(QKeySequence(Qt.Key_Return))

        if not self.sock.waitForConnected(2500):
            msg = self.sock.errorString()
            QMessageBox.warning(self, '警告', '服务器连接失败', QMessageBox.Ok)
        self.switch = {
            3: self.cmd3,
            5: self.cmd5,
        }

    def login(self):
        client_login = base_pb2.client_login()
        client_login.cmd = 2
        client_login.username = self.lineEdit.text()
        client_login.passwd = self.lineEdit_2.text()
        if client_login.username == "" and client_login.username == "":
            QMessageBox.warning(self, '警告', '用户名或密码为空', QMessageBox.Ok)
            return
        wData = QByteArray(client_login.SerializeToString())
        self.username = client_login.username
        self.writeData(wData)

    def register(self):
        self.reg = register.Register(self)
        self.hide()  # 隐藏
        self.reg.show()

    def readData(self):
        readData = self.sock.readAll()
        if readData == b'':
            return

        cmd = base_pb2.cmd()
        cmd.ParseFromString(readData.data())
        self.switch[cmd.c](readData.data())

    def writeData(self, data):
        headerData = QByteArray()
        wData = QDataStream(headerData, QIODevice.WriteOnly)
        wData.writeInt32(socket.htonl(len(data)))
        self.sock.write(headerData + data)
        self.sock.waitForBytesWritten()
        self.sock.flush()

    def cmd3(self, data):
        s_l = base_pb2.server_login()
        s_l.ParseFromString(data)
        if s_l.token == "":
            QMessageBox.warning(self, '警告', s_l.message, QMessageBox.Ok)
            return
        self.token = s_l.token
        print(self.token)
        self.sock.readyRead.disconnect(self.readData)
        self.g = game.PlayGame(self.sock, self.token, self.username)
        self.g.show()
        self.close()

    def cmd5(self, data):
        s_l = base_pb2.server_register()
        s_l.ParseFromString(data)
        QMessageBox.warning(self, '警告', s_l.message, QMessageBox.Ok)
        if s_l.isSuccess == 0:
            return
        self.reg.close()
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()

    myWin.show()

    app.exec_()
