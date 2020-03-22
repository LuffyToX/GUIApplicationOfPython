# -*- coding: utf-8 -*-
# QSS 的语法规则


from PyQt5.QtWidgets import *
import sys


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("MainWindow")
        self.setGeometry(800, 300, 300, 200)

        btn1 = QPushButton("按钮1")
        btn2 = QPushButton("按钮2")

        vbox = QVBoxLayout(self)
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)

        # QSS 类型选择器
        # 指定 QPushButton 及其子类的所有实例的前景色为红色
        qssStyle = " QPushButton {background-color: red} "
        self.setStyleSheet(qssStyle)                         # 加载 QSS 样式


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

