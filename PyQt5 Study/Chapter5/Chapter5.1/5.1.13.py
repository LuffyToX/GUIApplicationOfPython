# -*- coding: utf-8 -*-
# QTableWidget 右键菜单


import sys
from PyQt5.QtWidgets import (QMenu, QPushButton, QWidget, QTableWidget, QHBoxLayout, QApplication, QTableWidgetItem,
                             QHeaderView)
from PyQt5.QtCore import QObject, Qt


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        # 实例化 QTableWidget() 对象 4×3
        self.tableWidget = QTableWidget(4, 3)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("MainWindow")
        self.resize(500, 300)

        # 水平布局
        hbox = QHBoxLayout()
        hbox.addWidget(self.tableWidget)
        self.setLayout(hbox)

        # 设置水平方向的表格头
        self.tableWidget.setHorizontalHeaderLabels(['姓名', '性别', '体重'])

        # 水平方向：表格大小拓展到适当的尺寸
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # 创建单元格
        newItem1 = QTableWidgetItem("张三")
        newItem2 = QTableWidgetItem("男")
        newItem3 = QTableWidgetItem("160")

        # 将单元格添加到表格中
        self.tableWidget.setItem(0, 0, newItem1)
        self.tableWidget.setItem(0, 1, newItem2)
        self.tableWidget.setItem(0, 2, newItem3)

        # 将单元格居中对齐
        newItem1.setTextAlignment(Qt.AlignCenter)
        newItem2.setTextAlignment(Qt.AlignCenter)
        newItem3.setTextAlignment(Qt.AlignCenter)

        # 允许右键产生子菜单，将右键菜单绑定到槽函数 generateMenu
        self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableWidget.customContextMenuRequested.connect(self.generateMenu)

    def generateMenu(self, pos):
        # rint( pos)
        row_num = -1
        for i in self.tableWidget.selectionModel().selection().indexes():
            row_num = i.row()

        # 表格中只有 1 行有效数据，因此只在第 1 行支持右键弹出菜单
        if row_num < 1:
            menu = QMenu()
            item1 = menu.addAction(u"选项一")
            item2 = menu.addAction(u"选项二")
            item3 = menu.addAction(u"选项三")
            action = menu.exec_(self.tableWidget.mapToGlobal(pos))
            if action == item1:
                print('您选了选项一，当前行文字内容是：', self.tableWidget.item(row_num, 0).text(),
                      self.tableWidget.item(row_num, 1).text(), self.tableWidget.item(row_num, 2).text())

            elif action == item2:
                print('您选了选项二，当前行文字内容是：', self.tableWidget.item(row_num, 0).text(),
                      self.tableWidget.item(row_num, 1).text(), self.tableWidget.item(row_num, 2).text())

            elif action == item3:
                print('您选了选项三，当前行文字内容是：', self.tableWidget.item(row_num, 0).text(),
                      self.tableWidget.item(row_num, 1).text(), self.tableWidget.item(row_num, 2).text())
            else:
                return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
