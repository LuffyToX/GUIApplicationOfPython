# -*- coding: utf-8 -*-
# QTableWidget 单元格里面放控件


import sys
from PyQt5.QtWidgets import (QWidget, QTableWidget, QHBoxLayout, QApplication, QTableWidgetItem, QAbstractItemView,
                             QComboBox, QPushButton)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("MainWindow")
        self.resize(430, 300)

        # 实例化 QTableWidget() 对象 4×3
        tableWidget = QTableWidget(4, 3)

        # 水平布局
        hbox = QHBoxLayout()
        hbox.addWidget(tableWidget)
        self.setLayout(hbox)

        # 设置水平方向的表格头
        tableWidget.setHorizontalHeaderLabels(['姓名', '性别', '体重(kg)'])

        # 创建单元格，并将其添加到表格中
        newItem = QTableWidgetItem("张三")
        tableWidget.setItem(0, 0, newItem)

        # 新建下拉列表框，并设置其与单元格的边距 3px
        comBox = QComboBox()
        comBox.addItems(["男", "女"])
        comBox.setStyleSheet("QComboBox{margin:3px};")

        # 新建按钮，并设置其与单元格的边距 3px
        searchBtn = QPushButton("修改")
        searchBtn.setDown(True)
        searchBtn.setStyleSheet("QPushButton{margin:3px};")

        # 将下拉列表框、按钮添加到单元格中
        tableWidget.setCellWidget(0, 1, comBox)
        tableWidget.setCellWidget(0, 2, searchBtn)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
