# -*- coding: utf-8 -*-
# QTableView 的使用


from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys


class MainWindow(QWidget):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("MainWindow")
        self.resize(500, 300)

        # 实例化数据层次结构模型 ==> 4×4
        self.model = QStandardItemModel(4, 4)

        # 设置水平方向的表格头
        self.model.setHorizontalHeaderLabels(['标题1', '标题2', '标题3', '标题4'])

        # 设置每个单元格的文本值
        for row in range(4):
            for column in range(4):
                item = QStandardItem("row %s, column %s" % (row, column))
                self.model.setItem(row, column, item)

        # 实例化表格视图，设置模型为自定义的数据模型
        self.tableView = QTableView()
        self.tableView.setModel(self.model)

        # 垂直布局
        vbox = QVBoxLayout()
        vbox.addWidget(self.tableView)
        self.setLayout(vbox)

        """ <优化1> 让表格填满窗口，每列不能自由拉伸 """
        # 水平方向：标签拓展剩下的窗口部分，填满表格
        # self.tableView.horizontalHeader().setStretchLastSection(True)
        # 水平方向：表格大小拓展到适当的尺寸
        # self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        """ <优化2> 添加数据 """
        # self.model.appendRow([
        #     QStandardItem('row %s, column %s' % (4, 0)),
        #     QStandardItem('row %s, column %s' % (4, 1)),
        #     QStandardItem('row %s, column %s' % (4, 2)),
        #     QStandardItem('row %s, column %s' % (4, 3)),
        # ])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
