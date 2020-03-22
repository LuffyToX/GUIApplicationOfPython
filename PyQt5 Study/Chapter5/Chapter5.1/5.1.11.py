# -*- coding: utf-8 -*-
# QTableWidget 为单元格添加图片，并显示图片的描述信息


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("MainWindow")
        self.resize(600, 400)

        # 实例化 QTableWidget() 对象 5×4
        tableWidget = QTableWidget(5, 4)

        # 水平布局
        hbox = QHBoxLayout()
        hbox.addWidget(tableWidget)
        self.setLayout(hbox)

        # 设置水平方向的表格头
        tableWidget.setHorizontalHeaderLabels(['姓名', '性别', '体重', '显示图片'])

        # 水平方向：表格大小拓展到适当的尺寸
        tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # 创建单元格
        newItem1 = QTableWidgetItem("张三")
        newItem2 = QTableWidgetItem("男")
        newItem3 = QTableWidgetItem("160")
        newItem4 = QTableWidgetItem(QIcon(r".\images\10.ico"), "小黄人")

        # 将单元格添加到表格中
        tableWidget.setItem(0, 0, newItem1)
        tableWidget.setItem(0, 1, newItem2)
        tableWidget.setItem(0, 2, newItem3)
        tableWidget.setItem(0, 3, newItem4)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
