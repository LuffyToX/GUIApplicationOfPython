# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWin04.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.closeWinBtn = QtWidgets.QPushButton(Form)
        self.closeWinBtn.setGeometry(QtCore.QRect(140, 110, 91, 51))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../ico 文件/blackmushry.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeWinBtn.setIcon(icon)
        self.closeWinBtn.setIconSize(QtCore.QSize(20, 20))
        self.closeWinBtn.setObjectName("closeWinBtn")

        self.retranslateUi(Form)
        self.closeWinBtn.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.closeWinBtn.setText(_translate("Form", "关闭窗口"))
