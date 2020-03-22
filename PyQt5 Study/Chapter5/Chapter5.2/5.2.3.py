# -*- coding: utf-8 -*-
# QDockWidget 的使用


import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class DockWidget(QMainWindow):
    def __init__(self, parent=None):
        super(DockWidget, self).__init__(parent)

        self.setWindowTitle("DockWidget")

        # 菜单栏
        bar = self.menuBar()
        file = bar.addMenu("File")
        file.addAction("New")
        file.addAction("save")
        file.addAction("quit")

        # 设置中央控件
        self.setCentralWidget(QTextEdit())

        # 创建可停靠的窗口（Dock 窗口）
        # 第一个参数指定该窗口标题
        self.items = QDockWidget("Dockable", self)

        # 在 Dock 窗口中添加 QListWidget 对象
        self.listWidget = QListWidget()
        self.listWidget.addItem("item1")
        self.listWidget.addItem("item2")
        self.listWidget.addItem("item3")
        self.items.setWidget(self.listWidget)

        # 将 Dock 窗口设置为不可浮动
        self.items.setFloating(False)

        # 将 Dock 窗口放置在中央控件右侧
        self.addDockWidget(Qt.RightDockWidgetArea, self.items)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = DockWidget()
    win.show()
    sys.exit(app.exec_())
