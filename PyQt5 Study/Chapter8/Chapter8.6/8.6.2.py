# -*- coding: utf-8 -*-
# 缩放图片


import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self, parnet=None):
        super(MainWindow, self).__init__(parnet)

        self.setWindowTitle("MainWindow")
        self.move(800, 300)
        img = QImage(r".\images\Cloudy_72px.png")

        # 标签 固定大小
        label = QLabel(self)
        label.setFixedWidth(200)
        label.setFixedHeight(200)

        # 将图片缩放到标签大小，并加载到标签中
        result = img.scaled(label.width(), label.height(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        label.setPixmap(QPixmap.fromImage(result))

        vbox = QVBoxLayout()
        vbox.addWidget(label)
        self.setLayout(vbox)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

