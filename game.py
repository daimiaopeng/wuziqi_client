import socket
import time

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import *
import sys
import base_pb2
import button as MyButton
from PyQt5.QtNetwork import QTcpSocket
import main_ui


class Chessman(QLabel):
    def __init__(self, color="black", parent=None):
        super().__init__(parent)
        self.color = color
        self.pic = None
        if self.color == "black":
            self.pic = QPixmap("source/黑子.png")
        else:
            self.pic = QPixmap("source/白子.png")
        self.setPixmap(self.pic)
        self.setFixedSize(self.pic.size())  # 设置棋子大小
        self.show()

        self.x = 0
        self.y = 0

    def move(self, a0: QtCore.QPoint):
        super().move(a0.x() - 15, a0.y() - 15)

    def setIndex(self, x, y):
        self.x = x
        self.y = y


class PlayGame(QWidget, main_ui.Ui_Form):
    backSignal = pyqtSignal()  # 返回信号

    def __init__(self, sock, token, username, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.sock = sock
        self.isBeginGame = False
        self.isCanXia = False
        self.username = username
        self.sock.readyRead.connect(self.readData)
        self.token = token
        self.switch = {
            7: self.cmd7,
            9: self.cmd9,
            10: self.cmd10,
            12: self.cmd12,
            13: self.cmd13,
        }
        # img = QPixmap('source/表情.png')
        # img.scaled(self.label_2.size(), Qt.KeepAspectRatioByExpanding)
        # self.label_2.setScaledContents(True)
        # self.label_2.setPixmap(img)

        self.listView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listView.clicked.connect(self.listViewClicked)
        self.pushButton.clicked.connect(self.messageSend)
        # 左上角chessboard[0][0]
        # 右上角chessboard[0][18]
        # 左下角chessboard[18][0]
        # 右下角chessboard[18][18]
        # chessboard[行下标][列下标]
        self.chessboard = [[None for i in range(19)] for i in range(19)]
        # 落子棋子颜色
        self.turnChessColor = "black"
        self.history = []
        self.history2 = []
        self.is_over = False

        self.lbl = None

        # self.lab = QLabel('背景图片', self)
        # self.lab.setGeometry(0, 0, 760, 650)
        # pixmap = QPixmap('source/游戏界面.png')
        # self.lab.setPixmap(pixmap)

        # # 配置背景图
        # p = QPalette(self.palette())  # 获得当前的调色板
        # brush = QBrush(QImage("source/游戏界面.png"))
        # p.setBrush(QPalette.Background, brush)  # 设置调色
        # self.setPalette(p)  # 给窗口设置调色板

        # 设置标题
        # self.resize(760,650)
        self.setWindowTitle("双人联机")

        # 设置窗口图标
        self.setWindowIcon(QIcon("source/icon.ico"))
        # 设置窗口大小
        # self.setFixedSize(QImage("source/游戏界面.png").size())

        self.backBtn = MyButton.MyButton('source/返回按钮_hover.png',
                                         'source/返回按钮_normal.png',
                                         'source/返回按钮_press.png',
                                         parent=self)
        self.backBtn.move(650, 50)

        self.startBtn = MyButton.MyButton('source/开始按钮_hover.png',
                                          'source/开始按钮_normal.png',
                                          'source/开始按钮_press.png',
                                          parent=self)
        self.startBtn.move(650, 300)

        self.returnBtn = MyButton.MyButton('source/悔棋按钮_hover.png',
                                           'source/悔棋按钮_normal.png',
                                           'source/悔棋按钮_press.png',
                                           parent=self)
        self.returnBtn.move(650, 400)

        self.loseBtn = MyButton.MyButton('source/认输按钮_hover.png',
                                         'source/认输按钮_normal.png',
                                         'source/认输按钮_press.png',
                                         parent=self)
        self.loseBtn.move(650, 500)

        # 绑定返回按钮
        self.backBtn.clicked.connect(self.goBack)
        self.startBtn.clicked.connect(self.restar)
        self.loseBtn.clicked.connect(self.lose)
        self.returnBtn.clicked.connect(self.huiback)

        self.gameStatu = []

        self.focusPoint = QLabel(self)
        self.focusPoint.setPixmap(QPixmap("source/标识.png"))

        self.pushButton.setShortcut(QKeySequence(Qt.Key_Enter))
        self.pushButton.setShortcut(QKeySequence(Qt.Key_Return))

    def goBack(self):
        self.backSignal.emit()
        self.close()

    def closeEvent(self, a0: QtGui.QCloseEvent):
        self.backSignal.emit()

    def mouseReleaseEvent(self, a0: QtGui.QMouseEvent):
        if self.gameStatu == False or self.isCanXia == False:
            return None
        print(a0.pos())
        print("x:", a0.x())
        print("y:", a0.y())
        pos, chess_index = self.reversePos(a0)
        if pos is None:
            return

        if self.chessboard[chess_index[1]][chess_index[0]] != None:
            return

        self.chess = Chessman(color=self.turnChessColor, parent=self)
        self.chess.setIndex(chess_index[0], chess_index[1])
        self.chess.move(pos)
        self.chess.show()  # 显示棋子
        self.history.append(self.chess)
        self.history2.append(self.focusPoint)

        self.focusPoint.move(QPoint(pos.x() - 15, pos.y() - 15))
        self.focusPoint.show()
        self.focusPoint.raise_()

        print("棋盘交点位置：", chess_index)

        s_g_p = base_pb2.server_gobang_position()
        s_g_p.cmd = 6
        s_g_p.x = chess_index[0]
        s_g_p.y = chess_index[1]

        self.writeData(s_g_p.SerializeToString())

        # 放入棋盘
        self.chessboard[chess_index[1]][chess_index[0]] = self.chess

        if self.turnChessColor == "black":
            self.turnChessColor = "white"
        else:
            self.turnChessColor = "black"
        self.lbl = None
        result = self.isWin(self.chess)
        if result != None:
            print(result + '赢了')
            self.isBeginGame = False
            self.showResult(result)
        self.isCanXia = False
        # 自动落子
        # self.autoDown()

    # 坐标转换
    def reversePos(self, a0: QtCore.QPoint):
        if a0.x() <= 50 - 15 or a0.x() >= 590 + 15 or a0.y() <= 50 - 15 or a0.y() >= 590 + 15:
            return None, None

        self.x = (a0.x() - 35) // 30
        self.y = (a0.y() - 35) // 30

        x = 50 + 30 * self.x
        y = 50 + 30 * self.y
        return QPoint(x, y), (self.x, self.y)

    def isWin(self, chessman):
        print("in iswin,lastChessman:", chessman.color, chessman.x, chessman.y)
        # 水平方向y相同，chessboard[chessman.y][i]
        count = 1
        # 左边
        i = chessman.x - 1
        while i >= 0:
            if self.chessboard[chessman.y][i] == None or self.chessboard[chessman.y][i].color != chessman.color:
                break
            count += 1
            i -= 1
        # 右边
        i = chessman.x + 1
        while i <= 18:
            if self.chessboard[chessman.y][i] == None or self.chessboard[chessman.y][i].color != chessman.color:
                break
            count += 1
            i += 1

        if count >= 5:
            return chessman.color

        count = 1
        j = chessman.y - 1
        while j >= 0:
            if self.chessboard[j][chessman.x] == None or self.chessboard[j][chessman.x].color != chessman.color:
                break
            count += 1
            j -= 1

        j = chessman.y + 1
        while j <= 18:
            if self.chessboard[j][chessman.x] == None or self.chessboard[j][chessman.x].color != chessman.color:
                break
            count += 1
            j += 1

        if count >= 5:
            return chessman.color

        count = 1
        j, i = chessman.y - 1, chessman.x + 1
        while j >= 0 and i <= 18:
            if self.chessboard[j][i] == None or self.chessboard[j][i].color != chessman.color:
                break
            count += 1
            j -= 1
            i += 1

        j, i = chessman.y + 1, chessman.x - 1
        while i >= 0 and j <= 18:
            if self.chessboard[j][i] == None or self.chessboard[j][i].color != chessman.color:
                break
            count += 1
            i -= 1
            j += 1
        if count >= 5:
            return chessman.color

        count = 1
        j, i = chessman.y - 1, chessman.x - 1
        while j >= 0 and i >= 0:
            if self.chessboard[j][i] == None or self.chessboard[j][i].color != chessman.color:
                break
            count += 1
            j -= 1
            i -= 1

        j, i = chessman.y + 1, chessman.x + 1
        while j <= 18 and i <= 18:
            if self.chessboard[j][i] == None or self.chessboard[j][i].color != chessman.color:
                break
            count += 1
            j += 1
            i += 1

        if count >= 5:
            return chessman.color

        return None

    def showResult(self, isWin=None):
        self.gameStatu = False
        if isWin == "white":
            self.lbl = QLabel(self)
            self.lbl.setPixmap(QPixmap("source/白棋胜利.png"))
            self.lbl.move(150, 150)
            self.lbl.show()
        elif isWin == "black":
            self.lbl = QLabel(self)
            self.lbl.setPixmap(QPixmap("source/黑棋胜利.png"))
            self.lbl.move(150, 150)
            self.lbl.show()
        else:
            return

    def restar(self):
        for i in range(19):
            for j in range(19):
                if self.chessboard[i][j] != None:
                    self.chessboard[i][j].close()
                    self.chessboard[i][j] = None
                    self.focusPoint.close()
                else:
                    pass
        if self.lbl != None:
            self.lbl.close()

        self.gameStatu = True

    def lose(self):
        if self.gameStatu == False:
            return
        if self.turnChessColor == "black":
            self.lbl = QLabel(self)
            self.lbl.setPixmap(QPixmap("source/白棋胜利.png"))
            self.lbl.move(150, 150)
            self.lbl.show()
        elif self.turnChessColor == "white":
            self.lbl = QLabel(self)
            self.lbl.setPixmap(QPixmap("source/黑棋胜利.png"))
            self.lbl.move(150, 150)
            self.lbl.show()
        else:
            return

    def huiback(self):
        if self.gameStatu == False:
            return
        m = self.history.pop()
        a = self.history2.pop()
        self.chessboard[m.y][m.x] = None
        m.close()
        a.close()
        if self.turnChessColor == "black":
            self.turnChessColor = "white"
        else:
            self.turnChessColor = "black"

    def readData(self):
        readData = self.sock.readAll()
        if readData == b'':
            return

        cmd = base_pb2.cmd()
        cmd.ParseFromString(readData.data())
        print("cmd: %s" % cmd.c)
        self.switch[cmd.c](readData.data())

    def writeData(self, data):
        headerData = QByteArray()
        wData = QDataStream(headerData, QIODevice.WriteOnly)
        wData.writeInt64(socket.htonl(len(data)))
        self.sock.write(headerData + data)
        self.sock.waitForBytesWritten()
        self.sock.flush()

    def cmd7(self, data):
        # 获取对方的棋子位置，并显示
        s_g_p = base_pb2.server_gobang_position()
        s_g_p.ParseFromString(data)

        # 注意：x,y坐标对应
        chess_index = (s_g_p.y, s_g_p.x)  # 棋子在棋盘中的下标
        pos = QPoint(50 + s_g_p.x * 30, 50 + s_g_p.y * 30)  # 棋子在棋盘中的坐标

        self.chessman = Chessman(color=self.turnChessColor, parent=self)
        self.chessman.setIndex(chess_index[1], chess_index[0])
        self.chessman.move(pos)
        self.chessman.show()  # 显示棋子

        # 显示标识
        self.focusPoint.move(QPoint(pos.x() - 15, pos.y() - 15))
        self.focusPoint.show()
        self.focusPoint.raise_()

        self.chessboard[chess_index[0]][chess_index[1]] = self.chessman

        # 改变落子颜色
        if self.turnChessColor == 'black':
            self.turnChessColor = 'white'
        else:
            self.turnChessColor = 'black'
        # 判断输赢
        result = self.isWin(self.chessman)
        if result != None:
            print(result + '赢了')
            self.showResult(result)
            self.isBeginGame = False
        self.isCanXia = True

    def cmd9(self, data):
        # 显示在线用户列表
        s_o_i = base_pb2.server_online_infor()
        s_o_i.ParseFromString(data)
        print(s_o_i.people)
        self.peopleList = s_o_i.people
        self.peopleList.remove(self.username)
        slm = QStringListModel()
        slm.setStringList(self.peopleList)
        self.listView.setModel(slm)

    def cmd10(self, data):
        s_g_i = base_pb2.server_game_invite()
        s_g_i.ParseFromString(data)
        reply = QMessageBox.question(self, '提示', '"%s"请求对战' % s_g_i.people, QMessageBox.Yes | QMessageBox.No)
        c_g_i = base_pb2.client_game_invite()
        c_g_i.cmd = 11
        if reply == QMessageBox.Yes:
            c_g_i.code = 1
            self.isBeginGame = True
        else:
            c_g_i.code = 0
            pass
        self.writeData(c_g_i.SerializeToString())

    def cmd12(self, data):
        s_g_i = base_pb2.server_game_isInvite()
        s_g_i.ParseFromString(data)
        reply = ""
        self.fightBox.close()
        if s_g_i.code == 1:
            reply = "对方接受了请求"
            self.isBeginGame = True
            self.isCanXia = True
        elif s_g_i.code == 0:
            reply = "对方拒绝了请求"

        QMessageBox.information(self, '提示', reply, QMessageBox.Ok)

    def cmd13(self, data):
        c_m = base_pb2.chatMessage()
        c_m.ParseFromString(data)
        messagetype = c_m.type
        string = c_m.data
        messageTime = c_m.time

        s = '<font color=#F9904A>对手 %s </font> <br>%s' % (messageTime, string)
        if messagetype == 1:  # 文字信息
            self.insertChatMessage(s)

    def insertChatMessage(self, s):
        self.textBrowser.append(s)
        self.textBrowser.moveCursor(QTextCursor.End)
        self.lineEdit.clear()

    def listViewClicked(self, qModelIndex):
        if self.isBeginGame == True:
            QMessageBox.information(self, '警告', '您正在游戏中', QMessageBox.Ok)
            return
        self.withusername = self.peopleList[qModelIndex.row()]
        print(self.withusername)
        c_c_g = base_pb2.client_create_game()
        c_c_g.cmd = 8
        c_c_g.withUsername = self.withusername
        self.writeData(c_c_g.SerializeToString())

        # 创建一个问答框，注意是Question
        self.fightBox = QMessageBox(QMessageBox.Question, '对局请求中', '正在等待对方响应中...', parent=self)
        # 添加按钮，可用中文
        cancel = self.fightBox.addButton('取消对局', QMessageBox.YesRole)

        # 设置消息框中内容前面的图标
        self.fightBox.setIcon(1)

        # 显示该问答框
        self.fightBox.show()
        if self.fightBox.clickedButton() == cancel:
            self.fightBox.close()

    def messageSend(self):
        if self.lineEdit.text() == "":
            return
        c_m = base_pb2.chatMessage()
        c_m.cmd = 13
        c_m.type = 1
        c_m.time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        c_m.data = self.lineEdit.text()
        s = '<font color="#F9904A">我 %s </font> <br>%s' % (c_m.time, self.lineEdit.text())
        self.insertChatMessage(s)
        self.writeData(c_m.SerializeToString())


if __name__ == "__main__":
    a = QApplication(sys.argv)
    m = PlayGame()
    m.show()
    sys.exit(a.exec_())
