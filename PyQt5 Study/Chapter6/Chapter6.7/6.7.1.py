# -*- coding: utf-8 -*-
# 在布局中添加其他布局


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QFormLayout, QPushButton


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("MainWindow")

        # 全局布局（1个）：水平
        wlayout = QHBoxLayout()

        # 局部布局（4个）：水平、竖直、网格、表单
        hlayout = QHBoxLayout()
        vlayout = QVBoxLayout()
        glayout = QGridLayout()
        formlayout = QFormLayout()

        # 局部布局添加部件
        hlayout.addWidget(QPushButton(str(1)))
        hlayout.addWidget(QPushButton(str(2)))

        vlayout.addWidget(QPushButton(str(3)))
        vlayout.addWidget(QPushButton(str(4)))

        glayout.addWidget(QPushButton(str(5)), 0, 0)
        glayout.addWidget(QPushButton(str(6)), 0, 1)
        glayout.addWidget(QPushButton(str(7)), 1, 0)
        glayout.addWidget(QPushButton(str(8)), 1, 1)

        formlayout.addWidget(QPushButton(str(9)))
        formlayout.addWidget(QPushButton(str(10)))
        formlayout.addWidget(QPushButton(str(11)))
        formlayout.addWidget(QPushButton(str(12)))

        # 准备四个部件
        hwg = QWidget()
        vwg = QWidget()
        gwg = QWidget()
        fwg = QWidget()

        # 四个部件设置局部布局
        hwg.setLayout(hlayout)
        vwg.setLayout(vlayout)
        gwg.setLayout(glayout)
        fwg.setLayout(formlayout)

        # 四个部件加至全局布局
        wlayout.addWidget(hwg)
        wlayout.addWidget(vwg)
        wlayout.addWidget(gwg)
        wlayout.addWidget(fwg)

        # 窗体本体设置全局布局
        self.setLayout(wlayout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

