# -*- coding: utf-8 -*-
# QMdiArea 多重文档界面


import sys
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    count = 0

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("MDI")
        self.setGeometry(800, 300, 500, 400)

        # 新建 MDI 容器控件
        self.mdi = QMdiArea()

        # 将 MDI 容器设为中央控件
        self.setCentralWidget(self.mdi)

        # 菜单栏
        bar = self.menuBar()
        file = bar.addMenu("File")
        file.addAction("New")
        file.addAction("cascade")
        file.addAction("Tiled")
        # 当单击 'file' 控件时触发 triggered 信号
        file.triggered[QAction].connect(self.windowaction)

    def windowaction(self, q):
        # 新建子 MDI 容器控件
        if q.text() == "New":
            MainWindow.count = MainWindow.count + 1
            sub = QMdiSubWindow()
            sub.setWidget(QTextEdit())
            sub.setWindowTitle("subwindow" + str(MainWindow.count))
            self.mdi.addSubWindow(sub)
            sub.show()
        # 子窗口的排列方式 => 级联
        if q.text() == "cascade":
            self.mdi.cascadeSubWindows()
        # 子窗口的排列方式 => 平铺
        if q.text() == "Tiled":
            self.mdi.tileSubWindows()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

