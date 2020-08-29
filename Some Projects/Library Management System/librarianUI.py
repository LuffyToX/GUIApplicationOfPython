# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'librarianUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_librarianUI(object):
    def setupUi(self, librarianUI):
        librarianUI.setObjectName("librarianUI")
        librarianUI.resize(564, 378)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pic/images/librarian icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        librarianUI.setWindowIcon(icon)
        self.widget = QtWidgets.QWidget(librarianUI)
        self.widget.setGeometry(QtCore.QRect(20, 20, 521, 331))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.addState_ld = QtWidgets.QLineEdit(self.widget)
        self.addState_ld.setText("")
        self.addState_ld.setObjectName("addState_ld")
        self.gridLayout.addWidget(self.addState_ld, 0, 3, 1, 1)
        self.addAuthor_ld = QtWidgets.QLineEdit(self.widget)
        self.addAuthor_ld.setText("")
        self.addAuthor_ld.setObjectName("addAuthor_ld")
        self.gridLayout.addWidget(self.addAuthor_ld, 0, 2, 1, 1)
        self.studentInformation_btn = QtWidgets.QPushButton(self.widget)
        self.studentInformation_btn.setObjectName("studentInformation_btn")
        self.gridLayout.addWidget(self.studentInformation_btn, 1, 0, 1, 1)
        self.addAmount_ld = QtWidgets.QLineEdit(self.widget)
        self.addAmount_ld.setText("")
        self.addAmount_ld.setObjectName("addAmount_ld")
        self.gridLayout.addWidget(self.addAmount_ld, 0, 4, 1, 1)
        self.studentInformation_lv = QtWidgets.QListView(self.widget)
        self.studentInformation_lv.setObjectName("studentInformation_lv")
        self.gridLayout.addWidget(self.studentInformation_lv, 1, 1, 2, 5)
        self.addName_ld = QtWidgets.QLineEdit(self.widget)
        self.addName_ld.setText("")
        self.addName_ld.setObjectName("addName_ld")
        self.gridLayout.addWidget(self.addName_ld, 0, 1, 1, 1)
        self.addPosition_ld = QtWidgets.QLineEdit(self.widget)
        self.addPosition_ld.setText("")
        self.addPosition_ld.setObjectName("addPosition_ld")
        self.gridLayout.addWidget(self.addPosition_ld, 0, 5, 1, 1)
        self.add_btn = QtWidgets.QPushButton(self.widget)
        self.add_btn.setObjectName("add_btn")
        self.gridLayout.addWidget(self.add_btn, 0, 0, 1, 1)

        self.retranslateUi(librarianUI)
        QtCore.QMetaObject.connectSlotsByName(librarianUI)

    def retranslateUi(self, librarianUI):
        _translate = QtCore.QCoreApplication.translate
        librarianUI.setWindowTitle(_translate("librarianUI", "图书管理员端"))
        self.addState_ld.setPlaceholderText(_translate("librarianUI", "剩余馆藏"))
        self.addAuthor_ld.setPlaceholderText(_translate("librarianUI", "作者"))
        self.studentInformation_btn.setText(_translate("librarianUI", "查看学生信息"))
        self.addAmount_ld.setPlaceholderText(_translate("librarianUI", "全部馆藏"))
        self.addName_ld.setPlaceholderText(_translate("librarianUI", "书名"))
        self.addPosition_ld.setPlaceholderText(_translate("librarianUI", "书架号"))
        self.add_btn.setText(_translate("librarianUI", "添加新书籍"))
import apprcc
