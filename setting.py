from PyQt5.QtGui import QKeySequence
from PyQt5.QtNetwork import QTcpSocket
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import setting_ui


class Setting(QWidget, setting_ui.Ui_Form):
    def __init__(self, game, parent=None):
        super(Setting, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('设置')
        self._game = game
        self.checkBox.stateChanged.connect(self.sound)
        self.checkBox_2.stateChanged.connect(self.chat)

    def sound(self, state):
        self._game.soundSetting(state)

    def chat(self, state):
        self._game.chatSetting(state)
