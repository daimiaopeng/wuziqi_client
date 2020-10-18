from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import QSound


class Chessman(QLabel):
    def __init__(self, color='black', parent=None):
        super().__init__(parent)
        self.color = color
        self.pic = None
        if self.color == 'black':
            self.pic = QPixmap('source/black.png')
        else:
            self.pic = QPixmap('source/white.png')
        self.setPixmap(self.pic)
        self.setFixedSize(self.pic.size())  # 设置棋子大小
        self.show()
        self.parent = parent
        self.x = 0
        self.y = 0

    def move(self):
        x, y = 22 + self.x * 36 + self.parent.label.x() - 18, 22 + self.y * 36 + self.parent.label.y() - 18
        super().move(x - 4, y - 4)
        self.show()
        self.parent.sound_piece.play()
        self.parent.history.append(self)
        self.parent.history2.append(self.parent.focusPoint)
        self.parent.focusPoint.move(QPoint(x, y))
        self.parent.focusPoint.show()
        self.parent.focusPoint.raise_()
        # 放入棋盘
        self.parent.chessboard[self.y][self.x] = self
        if self.parent.turnChessColor == 'black':
            self.parent.turnChessColor = 'white'
        else:
            self.parent.turnChessColor = 'black'
        self.parent.lbl = None
        result = self.parent.isWin(self)
        if result != None:
            if result == self.parent.myColor:
                print('赢了')
                self.parent.sendGameRes(1, self.parent.userGameInfor.name)
            else:
                print('输了')
            self.parent.isBeginGame = False
            self.parent.showResult(result)

    def setIndex(self, x, y):
        self.x = x
        self.y = y
