# -*- coding: utf-8 -*-
# 绝对布局


import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("MainWindow")
        self.setGeometry(800, 300, 320, 120)

        # 如果不继承 self，该控件将被当作窗口处理
        lbl1 = QLabel('欢迎', self)
        lbl1.move(15, 10)

        lbl2 = QLabel('学习', self)
        lbl2.move(35, 40)

        lbl3 = QLabel('PyQt5 !', self)
        lbl3.move(55, 70)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
