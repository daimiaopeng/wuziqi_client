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
        Form.resize(997, 754)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 760, 650))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("source/游戏界面.png"))
        self.label.setObjectName("label")
        self.listView = QtWidgets.QListView(Form)
        self.listView.setGeometry(QtCore.QRect(760, 0, 201, 651))
        self.listView.setObjectName("listView")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
