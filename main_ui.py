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
        Form.resize(1188, 706)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 760, 650))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("source/游戏界面.png"))
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(760, 0, 331, 651))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listView = QtWidgets.QListView(self.layoutWidget)
        self.listView.setObjectName("listView")
        self.verticalLayout.addWidget(self.listView)
        self.textBrowser = QtWidgets.QTextBrowser(self.layoutWidget)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget)
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
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setEnabled(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        self.comboBox.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
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
        self.label_2.setText(_translate("Form", "TextL"))
        self.pushButton.setText(_translate("Form", "发送"))
