import socket
import time
import base_pb2
import button as MyButton
import main_ui
import base64
from chessman import *


class PlayGame(QWidget, main_ui.Ui_Form):
    backSignal = pyqtSignal()  # 返回信号

    def __init__(self, sock, username, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.sock = sock
        self.isBeginGame = False
        self.isCanXia = False
        self.label.setCursor(QCursor(Qt.ForbiddenCursor))
        self.username = username
        self.sock.readyRead.connect(self.readData)
        self.switch = {
            7: self.cmd7,
            9: self.cmd9,
            10: self.cmd10,
            12: self.cmd12,
            13: self.cmd13,
            14: self.cmd14,
            15: self.cmd15,
            16: self.cmd16,
        }
        self.sound_piece = QSound("source/luozisheng.wav")
        self.sound_win = QSound("source/win.wav")
        self.sound_defeated = QSound("source/defeated.wav")

        # img = QPixmap('source/表情.png')
        # img.scaled(self.label_2.size(), Qt.KeepAspectRatioByExpanding)
        # self.label_2.setScaledContents(True)
        # self.label_2.setPixmap(img)
        self.comboBox.currentIndexChanged.connect(self.messageSend)
        self.listView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listView.clicked.connect(self.listViewClicked)
        self.pushButton.clicked.connect(self.messageSend)
        self.pushButton_2.clicked.connect(self.withdraw)
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
        self.init()
        self.initButton()

    def init(self):
        self.setWindowTitle("双人联机")

        # 设置窗口图标
        self.setWindowIcon(QIcon("source/icon.ico"))
        # 设置窗口大小
        # self.setFixedSize(QImage("source/游戏界面.png").size())

        self.backBtn = MyButton.MyButton('source/返回按钮_hover.png',
                                         'source/返回按钮_normal.png',
                                         'source/返回按钮_press.png',
                                         parent=self)
        self.backBtn.move(650, 22)

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
        self.startBtn.clicked.connect(self.reStart)
        self.pushButton_5.clicked.connect(self.lose)
        self.pushButton_3.clicked.connect(self.draw)
        self.pushButton_4.clicked.connect(self.begin)
        self.returnBtn.clicked.connect(self.huiBack)

        self.gameStatu = []

        self.focusPoint = QLabel(self)
        self.focusPoint.setPixmap(QPixmap("source/标识.png"))

        self.pushButton.setShortcut(QKeySequence(Qt.Key_Enter))
        self.pushButton.setShortcut(QKeySequence(Qt.Key_Return))
        # self.pic1 = QPixmap('source/white.png')
        # self.pic2 = QPixmap('source/black.png')
        # self.setPixmap(self.pic1)
        # self.setFixedSize(self.pic1.size())  # 设置棋子大小
        # self.show()

    def initButton(self):
        if self.isBeginGame:
            self.pushButton_2.setEnabled(True)
            self.pushButton_3.setEnabled(True)
            self.pushButton_5.setEnabled(True)
        else:
            self.pushButton_2.setEnabled(False)
            self.pushButton_3.setEnabled(False)
            self.pushButton_5.setEnabled(False)

    def goBack(self):
        self.backSignal.emit()
        self.close()

    def closeEvent(self, a0: QtGui.QCloseEvent):
        self.backSignal.emit()

    def mouseReleaseEvent(self, a0: QtGui.QMouseEvent):
        if self.isCanXia == False:
            self.label.setCursor(QCursor(Qt.ForbiddenCursor))
            return
        else:
            self.label.setCursor(QCursor(Qt.PointingHandCursor))

        if self.gameStatu == False:
            return None

        pos, chess_index = self.reversePos(a0)
        if pos is None:
            return

        if self.chessboard[chess_index[1]][chess_index[0]] != None:
            return

        self.chess = Chessman(color=self.turnChessColor, parent=self)
        self.chess.setIndex(chess_index[0], chess_index[1])
        self.chess.move()

        s_g_p = base_pb2.server_gobang_position()
        s_g_p.cmd = 6
        s_g_p.x = chess_index[0]
        s_g_p.y = chess_index[1]

        self.writeData(s_g_p.SerializeToString())
        self.isCanXia = False
        self.label.setCursor(QCursor(Qt.ForbiddenCursor))
        # 自动落子
        # self.autoDown()

    # 坐标转换
    def reversePos(self, a0: QtCore.QPoint):
        if a0.x() <= self.label.x() + 4 or a0.x() >= self.label.x() + 517 + 18 or a0.y() <= self.label.y() + 4 or a0.y() >= self.label.y() + 517 + 18:
            return None, None

        self.x = (a0.x() - self.label.x() - 4) // 36
        self.y = (a0.y() - self.label.y() - 4) // 36

        return QPoint(22 + self.x * 36, 22 + self.y * 36), (self.x, self.y)

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
        self.lbl = QLabel(self)
        if isWin == 'white':
            self.lbl.setPixmap(QPixmap("source/白棋胜利.png"))
            self.lbl.move(150, 150)
            self.lbl.show()
        elif isWin == 'black':
            self.lbl.setPixmap(QPixmap("source/黑棋胜利.png"))
            self.lbl.move(150, 150)
            self.lbl.show()

        if isWin == self.myColor:
            self.sound_win.play()
        else:
            self.sound_defeated.play()
        self.isBeginGame = False
        self.initButton()
        self.isCanXia = False
        self.label.setCursor(QCursor(Qt.ForbiddenCursor))

    def reStart(self):
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

    def begin(self):
        pass

    def lose(self):
        if self.gameStatu == False or self.isBeginGame == False:
            return
        reply = QMessageBox.question(self, '提示', '您确定要认输吗?', QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.No:
            return
        if self.myColor == 'black':
            self.showResult('white')
        elif self.myColor == 'white':
            self.showResult('black')
        w_w = base_pb2.whoWin()
        w_w.cmd = 15
        w_w.code = 2
        w_w.win = ''
        self.writeData(w_w.SerializeToString())

    def draw(self):
        if self.gameStatu == False or self.isBeginGame == False:
            return
        reply = QMessageBox.question(self, '提示', '您确定要和棋吗?', QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.No:
            return
        w_w = base_pb2.whoWin()
        w_w.cmd = 15
        w_w.code = 3
        w_w.win = ''
        self.writeData(w_w.SerializeToString())

    def withdraw(self):
        w_d = base_pb2.withDraw()
        w_d.cmd = 16
        if self.isCanXia:  # 自己回合
            self.huiBack()
            self.huiBack()
            w_d.nums = 2
        else:
            self.huiBack()
            self.isCanXia = True
            self.label.setCursor(QCursor(Qt.PointingHandCursor))
            w_d.nums = 1
        self.writeData(w_d.SerializeToString())

    def huiBack(self):
        if self.gameStatu == False and len(self.history) == 0:
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
        try:
            cmd.ParseFromString(readData.data())
        except:
            pass
        print("cmd: %s" % cmd.c)
        self.switch[cmd.c](readData.data())

    def writeData(self, data):
        print("writeData")
        headerData = QByteArray()
        wData = QDataStream(headerData, QIODevice.WriteOnly)
        wData.writeUInt32(socket.htonl(len(data)))
        self.sock.write(headerData + data)
        self.sock.waitForBytesWritten()
        self.sock.flush()

    def cmd7(self, data):
        # 获取对方的棋子位置，并显示
        s_g_p = base_pb2.server_gobang_position()
        s_g_p.ParseFromString(data)
        self.chessman = Chessman(color=self.turnChessColor, parent=self)
        self.chessman.setIndex(s_g_p.x, s_g_p.y)
        self.chessman.move()
        self.isCanXia = True
        self.label.setCursor(QCursor(Qt.PointingHandCursor))

    def cmd9(self, data):
        # 显示在线用户列表
        s_o_i = base_pb2.server_online_infor()
        s_o_i.ParseFromString(data)
        # print(s_o_i.people)
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
            self.initButton()
            self.myColor = "white"
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
            self.initButton()
            self.isCanXia = True
            self.label.setCursor(QCursor(Qt.PointingHandCursor))
            self.myColor = "black"
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

    def cmd14(self, data):
        s_u_i = base_pb2.server_user_infor()
        s_u_i.ParseFromString(data)
        self.userGameInfor = s_u_i

        s = """昵称:%-5s\n积分：%-5s  级别：%-5s\n总盘数：%-4s 游戏币：%-5s\n胜：%-5s 负：%-5s平：%-5s
        """ % (
            s_u_i.name, s_u_i.integral, s_u_i.level, s_u_i.numsGame, s_u_i.gameCurrency, s_u_i.win, s_u_i.lose,
            s_u_i.draw)
        img = QPixmap()
        img.loadFromData(base64.b64decode(s_u_i.avatar))
        self.label_11.setPixmap(img)
        self.label_11.setScaledContents(True)
        self.label_3.setText(s)

    def cmd15(self, data):
        w_w = base_pb2.whoWin()
        w_w.ParseFromString(data)
        if w_w.code == 2:
            self.showResult(self.myColor)
        elif w_w.code == 3:
            reply = QMessageBox.question(self, '提示', '对方请求和棋', QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                w_w.code = 4
                self.showResult(self.myColor)
            else:
                w_w.code = 5
            self.writeData(w_w.SerializeToString())
        elif w_w.code == 4:
            self.showResult(self.myColor)

        elif w_w.code == 5:
            reply = QMessageBox.question(self, '提示', '对方不同意和棋', QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                return

    def cmd16(self, data):
        w_d = base_pb2.withDraw()
        w_d.ParseFromString(data)
        if w_d.nums == 1:
            self.huiBack()
            self.isCanXia = False
            self.label.setCursor(QCursor(Qt.ForbiddenCursor))
        elif w_d.nums == 2:
            self.huiBack()
            self.huiBack()

    def insertChatMessage(self, s):
        self.textBrowser.append(s)
        self.textBrowser.moveCursor(QTextCursor.End)
        self.comboBox.lineEdit().clear()

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

    def sendGameRes(self, code, win):
        res = base_pb2.whoWin()
        res.cmd = 15
        res.code = code
        res.win = win
        self.writeData(res.SerializeToString())

    def messageSend(self):
        if self.comboBox.lineEdit().text() == "":
            return
        c_m = base_pb2.chatMessage()
        c_m.cmd = 13
        c_m.type = 1
        c_m.time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        c_m.data = self.comboBox.lineEdit().text()
        s = '<font color="#F9904A">我 %s </font> <br>%s' % (c_m.time, self.comboBox.lineEdit().text())
        self.insertChatMessage(s)
        self.writeData(c_m.SerializeToString())
