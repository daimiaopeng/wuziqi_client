# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1159, 642)
        Form.setStyleSheet("/************* 左侧管理工具栏 ***************/\n"
                           "QWidget#mangeWidget, #listItemWidget, #musicMangeScrollAreaWidget {\n"
                           "    background-color: #f5f5f7;\n"
                           "}\n"
                           "QListWidget#musicMangeListWidget {\n"
                           "    border: none;\n"
                           "    outline: none;\n"
                           "    background-color: #f5f5f7;\n"
                           "}\n"
                           "QListWidget#musicMangeListWidget::item {\n"
                           "    background-color: #f5f5f7;\n"
                           "    border: solid\n"
                           "}\n"
                           "QListWidget#musicMangeListWidget::item:hover {\n"
                           "    background-color: #f5f5f7;\n"
                           "}\n"
                           "QListWidget#musicMangeListWidget::item:selected {\n"
                           "    background-color: #e6e7ea;\n"
                           "    border-left-width: 4px;\n"
                           "    border-left-color: #c62f2f;\n"
                           "}\n"
                           "QLabel#boxTitleLabel, #toolboxNameLabel {\n"
                           "    color: #696969;\n"
                           "    font-family: \"Microsoft Yahei\";\n"
                           "    font-size: 9pt;\n"
                           "    background-color: #f5f5f7;\n"
                           "}\n"
                           "QScrollArea#musicMangeScrollArea {\n"
                           "    border: 0px solid;\n"
                           "    border-right-width: 1px;\n"
                           "    border-right-color: #dcdbdc;\n"
                           "    background-color: #f5f5f7;\n"
                           "}\n"
                           "QScrollBar:vertical {\n"
                           "    border: none;\n"
                           "    background: #f5f5f7;\n"
                           "    width: 10px;\n"
                           "    margin: 0px 0 0px 0;\n"
                           "}\n"
                           "QScrollBar::handle:vertical {\n"
                           "    background: Gainsboro;\n"
                           "    min-height: 20px;\n"
                           "    border-radius: 5px;\n"
                           "    border: none;\n"
                           "}\n"
                           "QScrollBar::add-line:vertical {\n"
                           "    border: 0px solid grey;\n"
                           "    background: #32CC99;\n"
                           "    height: 0px;\n"
                           "    subcontrol-position: bottom;\n"
                           "    subcontrol-origin: margin;\n"
                           "}\n"
                           "QScrollBar::sub-line:vertical {\n"
                           "    border: 0px solid grey;\n"
                           "    background: #32CC99;\n"
                           "    height: 0px;\n"
                           "    subcontrol-position: top;\n"
                           "    subcontrol-origin: margin;\n"
                           "}\n"
                           "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
                           "    background: none;\n"
                           "    width: 0px;\n"
                           "    height: 0px;\n"
                           "}\n"
                           "QPushButton#playListTitleButton, #openListButton,\n"
                           "        #createPLayListButton {\n"
                           "    border: none;\n"
                           "}\n"
                           "QPushButton#playListTitleButton {\n"
                           "    text-align : left;\n"
                           "    color: #696969;\n"
                           "    font-family: \"Microsoft Yahei\";\n"
                           "    font-size: 9pt;\n"
                           "    background-color: #f5f5f7;\n"
                           "}\n"
                           "")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(290, 30, 540, 540))
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setInputMethodHints(QtCore.Qt.ImhNone)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("source/chessboard.jpg"))
        self.label.setObjectName("label")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setEnabled(True)
        self.label_11.setGeometry(QtCore.QRect(77, 20, 128, 128))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(123)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("source/avatar/1.png"))
        self.label_11.setObjectName("label_11")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(47, 150, 202, 66))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(10, 20, 20, 271))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(257, 20, 20, 271))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_2.sizePolicy().hasHeightForWidth())
        self.line_2.setSizePolicy(sizePolicy)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(17, 280, 251, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Form)
        self.line_4.setGeometry(QtCore.QRect(17, 10, 250, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 230, 36, 36))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("source/black.png"))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(47, 440, 202, 66))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.line_5 = QtWidgets.QFrame(Form)
        self.line_5.setGeometry(QtCore.QRect(17, 290, 250, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(Form)
        self.line_6.setGeometry(QtCore.QRect(257, 300, 20, 281))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_6.sizePolicy().hasHeightForWidth())
        self.line_6.setSizePolicy(sizePolicy)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(40, 520, 36, 36))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("source/white.png"))
        self.label_5.setObjectName("label_5")
        self.line_7 = QtWidgets.QFrame(Form)
        self.line_7.setGeometry(QtCore.QRect(17, 570, 251, 20))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setEnabled(True)
        self.label_12.setGeometry(QtCore.QRect(77, 310, 128, 128))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(123)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("source/avatar/1.png"))
        self.label_12.setObjectName("label_12")
        self.line_8 = QtWidgets.QFrame(Form)
        self.line_8.setGeometry(QtCore.QRect(10, 300, 20, 281))
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.lcdNumber = QtWidgets.QLCDNumber(Form)
        self.lcdNumber.setGeometry(QtCore.QRect(140, 220, 101, 51))
        self.lcdNumber.setProperty("value", 0.0)
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(Form)
        self.lcdNumber_2.setGeometry(QtCore.QRect(140, 510, 101, 51))
        self.lcdNumber_2.setProperty("value", 0.0)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(80, 220, 61, 51))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(80, 510, 61, 51))
        self.label_8.setObjectName("label_8")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(290, 580, 543, 40))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("font: 16pt \"华文行楷\";")
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_2.addWidget(self.pushButton_6)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setStyleSheet("font: 16pt \"华文行楷\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_4.setAutoFillBackground(False)
        self.pushButton_4.setStyleSheet("font: 16pt \"华文行楷\";\n"
                                        "               background-image: url(\"/source/button.png\");\n"
                                        "             ")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setStyleSheet("font: 16pt \"华文行楷\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_5 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_5.setStyleSheet("font: 16pt \"华文行楷\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.layoutWidget1 = QtWidgets.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(850, 10, 291, 601))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.layoutWidget1)
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.horizontalLayout_3.addWidget(self.lcdNumber_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.listView = QtWidgets.QListView(self.layoutWidget1)
        self.listView.setStyleSheet(
                "background-color: #4C4C4C; /*#004100;*/color: #bbbbbb;background-color:transparent")
        self.listView.setObjectName("listView")
        self.verticalLayout_2.addWidget(self.listView)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.layoutWidget1)
        self.textBrowser.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.textBrowser.setStyleSheet(
                "background-color: #4C4C4C; /*#004100;*/color: #bbbbbb;background-color:transparent")
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget1)
        self.comboBox.setEnabled(True)
        self.comboBox.setTabletTracking(False)
        self.comboBox.setEditable(True)
        self.comboBox.setCurrentText("")
        self.comboBox.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 2, 0, 1, 1)
        self.label_2.raise_()
        self.lcdNumber.raise_()
        self.layoutWidget.raise_()
        self.label.raise_()
        self.layoutWidget.raise_()
        self.label_11.raise_()
        self.label_3.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        self.line_4.raise_()
        self.label_4.raise_()
        self.line_5.raise_()
        self.line_6.raise_()
        self.label_5.raise_()
        self.line_7.raise_()
        self.label_12.raise_()
        self.line_8.raise_()
        self.lcdNumber_2.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label.setBuddy(self.listView)

        self.retranslateUi(Form)
        self.comboBox.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
            _translate = QtCore.QCoreApplication.translate
            Form.setWindowTitle(_translate("Form", "Form"))
            self.label_3.setText(_translate("Form", "积分：0      级别：0    \n"
                                                    "总盘数：0    游戏币：0    \n"
                                                    "胜：0     负：0    平：0 "))
            self.label_4.setText(_translate("Form", "积分：0      级别：0    \n"
                                                    "总盘数：0    游戏币：0    \n"
                                                    "胜：0     负：0    平：0 "))
            self.label_7.setText(_translate("Form",
                                            "<html><head/><body><p><span style=\" font-size:10pt;\">倒计时：</span></p></body></html>"))
            self.label_8.setText(_translate("Form",
                                            "<html><head/><body><p><span style=\" font-size:10pt;\">倒计时：</span></p></body></html>"))
            self.pushButton_6.setText(_translate("Form", "设置"))
            self.pushButton_2.setText(_translate("Form", "悔棋"))
            self.pushButton_4.setText(_translate("Form", "匹配对手"))
            self.pushButton_3.setText(_translate("Form", "和棋"))
            self.pushButton_5.setText(_translate("Form", "认输"))
            self.label_6.setText(_translate("Form", "在线人数："))
            self.label_9.setText(_translate("Form", "在线列表："))
            self.comboBox.setItemText(0, _translate("Form", "大家好，很高兴见到各位！"))
            self.comboBox.setItemText(1, _translate("Form", "快点吧，我等到花儿也谢了。"))
            self.comboBox.setItemText(2, _translate("Form", "你的牌打得太好了！"))
        self.comboBox.setItemText(3, _translate("Form", "我们交个朋友吧，能告诉我你的联系方法吗？"))
        self.comboBox.setItemText(4, _translate("Form", "各位，真不好意思，我要离开一会。"))
        self.comboBox.setItemText(5, _translate("Form", "又断线了，网络怎么这么差啊！"))
        self.comboBox.setItemText(6, _translate("Form", "不要吵了，有什么好吵的，专心玩游戏吧。"))
        self.comboBox.setItemText(7, _translate("Form", "你是MM，还是GG？"))
        self.comboBox.setItemText(8, _translate("Form", "下次再玩吧，我要走了。"))
        self.comboBox.setItemText(9, _translate("Form", "再见了，我会想念大家的。"))
        self.comboBox.setItemText(10, _translate("Form", "和你合作真是太愉快啦。"))
        self.comboBox.setItemText(11, _translate("Form", "不要走，决战到天亮。"))
        self.pushButton.setText(_translate("Form", "发送"))
