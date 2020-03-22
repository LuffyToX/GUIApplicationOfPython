# -*- coding: utf-8 -*-
# 拖拽功能


import sys
from PyQt5.QtWidgets import *


class Combo(QComboBox):

    def __init__(self, parent):
        super(Combo, self).__init__(parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        """
        当执行一个拖拽控件操作，并且鼠标指针进入该控件时，该事件将被触发
        该事件可以获得被操作的窗口控件，也可以有条件的接受/拒绝该拖拽操作 """

        # 验证事件的 MIME 数据是否包含了字符串文本
        if event.mimeData().hasText():
            # 响应事件
            event.accept()
        else:
            # 忽略事件
            event.ignore()

    def dropEvent(self, event):
        """
        当拖拽操作在目标控件上被释放时，该事件将被触发 """

        self.addItem(event.mimeData().text())


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("MainWindow")
        self.resize(400, 300)

        label = QLabel("请把左边的文本拖拽到右边的下拉菜单中")

        # 允许拖拽数据的控件必须设置 QWidget.setDragEnabled(True)
        # 另外控件应该响应拖拽事件，以便存储所拖拽的数据
        edit = QLineEdit()
        edit.setDragEnabled(True)
        com = Combo(self)

        # 表单布局
        fl = QFormLayout()
        fl.addRow(label)
        fl.addRow(edit, com)
        self.setLayout(fl)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
