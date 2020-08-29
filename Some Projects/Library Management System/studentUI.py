# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'studentUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StudentUI(object):
    def setupUi(self, StudentUI):
        StudentUI.setObjectName("StudentUI")
        StudentUI.resize(549, 332)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pic/images/student icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        StudentUI.setWindowIcon(icon)
        self.tabWidget = QtWidgets.QTabWidget(StudentUI)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 551, 171))
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setObjectName("tabWidget")
        self.query = QtWidgets.QWidget()
        self.query.setObjectName("query")
        self.gridLayout = QtWidgets.QGridLayout(self.query)
        self.gridLayout.setObjectName("gridLayout")
        self.query_ld = QtWidgets.QLineEdit(self.query)
        self.query_ld.setText("")
        self.query_ld.setObjectName("query_ld")
        self.gridLayout.addWidget(self.query_ld, 0, 0, 1, 1)
        self.query_btn = QtWidgets.QPushButton(self.query)
        self.query_btn.setObjectName("query_btn")
        self.gridLayout.addWidget(self.query_btn, 0, 1, 1, 1)
        self.query_tw = QtWidgets.QTableWidget(self.query)
        self.query_tw.setRowCount(1)
        self.query_tw.setColumnCount(5)
        self.query_tw.setObjectName("query_tw")
        self.query_tw.horizontalHeader().setVisible(True)
        self.query_tw.horizontalHeader().setCascadingSectionResizes(True)
        self.query_tw.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.query_tw, 1, 0, 1, 2)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/pic/images/student tab1.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.query, icon1, "")
        self.borrow = QtWidgets.QWidget()
        self.borrow.setObjectName("borrow")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.borrow)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.borrow_ld = QtWidgets.QLineEdit(self.borrow)
        self.borrow_ld.setObjectName("borrow_ld")
        self.horizontalLayout.addWidget(self.borrow_ld)
        self.borrow_btn = QtWidgets.QPushButton(self.borrow)
        self.borrow_btn.setObjectName("borrow_btn")
        self.horizontalLayout.addWidget(self.borrow_btn)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/pic/images/student tab2.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.borrow, icon2, "")
        self.back = QtWidgets.QWidget()
        self.back.setObjectName("back")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.back)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.back_ld = QtWidgets.QLineEdit(self.back)
        self.back_ld.setObjectName("back_ld")
        self.horizontalLayout_2.addWidget(self.back_ld)
        self.back_btn = QtWidgets.QPushButton(self.back)
        self.back_btn.setObjectName("back_btn")
        self.horizontalLayout_2.addWidget(self.back_btn)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/pic/images/student tab3.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.back, icon3, "")

        self.retranslateUi(StudentUI)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(StudentUI)

    def retranslateUi(self, StudentUI):
        _translate = QtCore.QCoreApplication.translate
        StudentUI.setWindowTitle(_translate("StudentUI", "学生端"))
        self.query_btn.setText(_translate("StudentUI", "查询"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.query), _translate("StudentUI", "查询"))
        self.borrow_btn.setText(_translate("StudentUI", "借阅"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.borrow), _translate("StudentUI", "借阅"))
        self.back_btn.setText(_translate("StudentUI", "归还"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.back), _translate("StudentUI", "归还"))
import apprcc
