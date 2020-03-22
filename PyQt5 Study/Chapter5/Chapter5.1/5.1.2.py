# -*- coding: utf-8 -*-
# QListView 的使用


from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListView, QMessageBox
from PyQt5.QtCore import QStringListModel
import sys


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("MainWindow")
        self.resize(300, 270)

        # 实例化列表模型，加载数据列表
        slm = QStringListModel()
        self.qList = ['Item 1', 'Item 2', 'Item 3', 'Item 4']
        slm.setStringList(self.qList)

        # 实例化列表视图，设置模型为自定义的数据模型
        listView = QListView()
        listView.setModel(slm)

        listView.clicked.connect(self.clicked)

        # 垂直布局
        vbox = QVBoxLayout()
        vbox.addWidget(listView)
        self.setLayout(vbox)

    def clicked(self, qModelIndex):
        QMessageBox.information(self, "QListView", "你选择了: " + self.qList[qModelIndex.row()])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
