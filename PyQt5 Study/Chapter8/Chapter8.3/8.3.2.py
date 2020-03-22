# -*- coding: utf-8 -*-
# QSS 选择器类型


from PyQt5.QtWidgets import *
import sys


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("MainWindow")
        self.setGeometry(800, 300, 300, 200)

        btn1 = QPushButton('按钮1')
        btn2 = QPushButton('按钮2')
        btn2.setProperty('name', 'myBtn')      # 设置 btn2 的 name 属性

        vbox = QVBoxLayout(self)
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)

        # QSS 属性选择器
        # 指定 QPushButton 的 name 属性为 'myBtn' 的控件的背景色为红色
        qssStyle = " QPushButton[name='myBtn'] {background-color: red } "
        self.setStyleSheet(qssStyle)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

