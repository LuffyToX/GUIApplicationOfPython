# -*- coding: utf-8 -*-
# QTableWidget 的基本用法


import sys
from PyQt5.QtWidgets import QWidget, QTableWidget, QHBoxLayout, QApplication, QTableWidgetItem, QAbstractItemView


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("MainWindow")
        self.resize(430, 230)

        # 实例化 QTableWidget() 对象
        # tableWidget = QTableWidget(4, 3)
        tableWidget = QTableWidget()
        tableWidget.setRowCount(4)
        tableWidget.setColumnCount(3)

        # 设置水平方向的表格头和垂直方向的表格头
        tableWidget.setHorizontalHeaderLabels(['姓名', '性别', '体重(kg)'])
        tableWidget.setVerticalHeaderLabels(['行1', '行2', '行3', '行4'])

        # 创建单元格（即QTableWidgetItem() 对象），并将其添加到表格中
        Item1 = QTableWidgetItem("张三")
        tableWidget.setItem(0, 0, Item1)

        Item2 = QTableWidgetItem("男")
        tableWidget.setItem(0, 1, Item2)

        Item3 = QTableWidgetItem("160")
        tableWidget.setItem(0, 2, Item3)

        # 将单元格设为禁止编辑的（默认情况下：单元格是可编辑的）
        # tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # 设置表格为整行选择
        # tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        # 将行和列的大小设为与内容相匹配
        # tableWidget.resizeColumnsToContents()
        # tableWidget.resizeRowsToContents()

        # 表格表头的显示与隐藏 True/False
        # tableWidget.verticalHeader().setVisible(False)
        # tableWidget.horizontalHeader().setVisible(False)

        # 不显示表格单元格的分割线
        # tableWidget.setShowGrid(False)

        # 水平布局
        hbox = QHBoxLayout()
        hbox.addWidget(tableWidget)
        self.setLayout(hbox)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
