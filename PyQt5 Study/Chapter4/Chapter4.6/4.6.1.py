# -*- coding: utf-8 -*-
# QComboBox 的使用


import sys
from PyQt5.QtWidgets import *


class Dialog(QWidget):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)

        self.setWindowTitle("Dialog")
        self.resize(300, 90)

        self.lbl = QLabel("")                       # 新建一个标签，用于添加文本
        self.cb = QComboBox()                       # 新建一个下拉列表框对象
        self.cb.addItem("C")                        # 添加一个下拉选项
        self.cb.addItem("C++")                      # 添加一个下拉选项
        self.cb.addItems(["Java", "C#", "Python"])  # 从列表中添加下拉选项
        self.cb.currentIndexChanged.connect(self.selectionchange)

        # 垂直布局
        layout = QVBoxLayout()
        layout.addWidget(self.cb)
        layout.addWidget(self.lbl)
        self.setLayout(layout)

    def selectionchange(self):
        self.lbl.setText(self.cb.currentText())     # 将标签文本设为下拉列表框中当前选中的文本
        self.lbl.adjustSize()                       # 根据内容自适应大小

        print("Items in the list are :")
        for count in range(self.cb.count()):
            print('item_' + str(count) + ' is ' + self.cb.itemText(count))
        print("Selected index is %d and item is %s" % (self.cb.currentIndex(), self.cb.currentText()))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Dialog()
    win.show()
    sys.exit(app.exec_())
