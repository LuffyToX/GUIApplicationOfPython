# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_loginUI(object):
    def setupUi(self, loginUI):
        loginUI.setObjectName("loginUI")
        loginUI.resize(480, 320)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pic/images/login icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        loginUI.setWindowIcon(icon)
        self.layoutWidget = QtWidgets.QWidget(loginUI)
        self.layoutWidget.setGeometry(QtCore.QRect(230, 70, 222, 125))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.password_ld = QtWidgets.QLineEdit(self.layoutWidget)
        self.password_ld.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_ld.setObjectName("password_ld")
        self.gridLayout.addWidget(self.password_ld, 1, 3, 1, 2)
        self.user_lb = QtWidgets.QLabel(self.layoutWidget)
        self.user_lb.setObjectName("user_lb")
        self.gridLayout.addWidget(self.user_lb, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 1, 1, 2)
        self.user_ld = QtWidgets.QLineEdit(self.layoutWidget)
        self.user_ld.setObjectName("user_ld")
        self.gridLayout.addWidget(self.user_ld, 0, 3, 1, 2)
        self.password_lb = QtWidgets.QLabel(self.layoutWidget)
        self.password_lb.setObjectName("password_lb")
        self.gridLayout.addWidget(self.password_lb, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 1, 1, 2)
        self.identity_lb = QtWidgets.QLabel(self.layoutWidget)
        self.identity_lb.setObjectName("identity_lb")
        self.gridLayout.addWidget(self.identity_lb, 2, 0, 1, 1)
        self.student_rb = QtWidgets.QRadioButton(self.layoutWidget)
        self.student_rb.setObjectName("student_rb")
        self.gridLayout.addWidget(self.student_rb, 2, 3, 1, 1)
        self.librarian_rb = QtWidgets.QRadioButton(self.layoutWidget)
        self.librarian_rb.setObjectName("librarian_rb")
        self.gridLayout.addWidget(self.librarian_rb, 2, 4, 1, 1)
        self.login_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.login_btn.setStyleSheet("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/pic/images/login button.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.login_btn.setIcon(icon1)
        self.login_btn.setObjectName("login_btn")
        self.gridLayout.addWidget(self.login_btn, 5, 0, 1, 5)
        self.password_ld.raise_()
        self.user_ld.raise_()
        self.password_lb.raise_()
        self.login_btn.raise_()
        self.identity_lb.raise_()
        self.student_rb.raise_()
        self.librarian_rb.raise_()
        self.user_lb.raise_()

        self.retranslateUi(loginUI)
        QtCore.QMetaObject.connectSlotsByName(loginUI)

    def retranslateUi(self, loginUI):
        _translate = QtCore.QCoreApplication.translate
        loginUI.setWindowTitle(_translate("loginUI", "登录"))
        self.user_lb.setText(_translate("loginUI", "用户名"))
        self.password_lb.setText(_translate("loginUI", "密码"))
        self.identity_lb.setText(_translate("loginUI", "身份"))
        self.student_rb.setText(_translate("loginUI", "学生"))
        self.librarian_rb.setText(_translate("loginUI", "图书管理员"))
        self.login_btn.setText(_translate("loginUI", "登录/注册"))
import apprcc
