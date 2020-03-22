# -*- coding: utf-8 -*-
# QPalette 设置窗口背景图片


import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPalette, QBrush, QPixmap


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("MainWindow")
        # 当背景图片的宽度和高度大于窗口的宽度和高度时，会铺满整个窗口
        self.setGeometry(800, 300, 460, 250)
        # 当背景图片的宽度和高度小于窗口的宽度和高度时，会加载多个图片
        # self.setGeometry(800, 300, 800, 600)

        palette = QPalette()
        # 设置调色板背景图片
        palette.setBrush(QPalette.Background, QBrush(QPixmap("./images/python.jpg")))
        self.setPalette(palette)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
