# -*- coding: utf-8 -*-
# 显示 QLable 标签


import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPalette


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("MainWidow")
        self.move(300, 30)

        label1 = QLabel()
        label1.setText("这是一个文本标签")
        label1.setAutoFillBackground(True)          # 自动填充背景
        palette = QPalette()                        # 获取调色板对象
        palette.setColor(QPalette.Window, Qt.blue)  # 设置调色板颜色
        label1.setPalette(palette)                  # 设置 label1 的背景颜色
        label1.setAlignment(Qt.AlignCenter)         # 居中对齐

        label2 = QLabel()
        label2.setText("欢迎使用 Python GUI 应用")

        label3 = QLabel()
        label3.setAlignment(Qt.AlignCenter)         # 居中对齐
        label3.setToolTip('这是一个图片图标')        # 设置 label3 的提示信息
        # 设置 label3 为 Pixmap 图片
        # 参数为 QPixmap 对象，而 QPixmap 对象的构造函数为图片路径
        label3.setPixmap(QPixmap(r".\images\house.jpg"))

        label4 = QLabel()
        label4.setText("<a href='https://image.baidu.com'>点击这里进入百度图片</a>")
        label4.setAlignment(Qt.AlignRight)          # 居右对其
        label4.setToolTip('这是一个超链接标签')      # 设置 label4 的提示信息
        label4.setOpenExternalLinks(True)           # 允许 label4 访问超链接

        # 垂直布局
        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)
        # QVBoxLayout 没有传递参数 self，必须调用 self.setLayout
        self.setLayout(vbox)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

