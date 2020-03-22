# -*- coding: utf-8 -*-
# 关闭主窗口


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("MainWindow")
        self.setWindowIcon(QIcon(r".\images\2.ico"))
        self.resize(400, 300)

        # 获取按钮对象
        # 将内置信号 'clicked' 链接到自定义槽函数 'close()'
        # QObject.signal.connect(slot_fun) 槽函数不带()
        button = QPushButton('关闭主窗口')
        button.clicked.connect(self.onButtonClick)

        layout = QHBoxLayout()                 # 获取布局管理器对象
        layout.addWidget(button)               # 布局管理器添加对象

        mainFram = QWidget()                   # 获取窗体控件
        mainFram.setLayout(layout)             # 将布局管理器添加到该窗体控件
        self.setCentralWidget(mainFram)        # 将该窗体控件设为主窗口中心控件

    def onButtonClick(self):
        # sender() 获取发送信号的对象
        sender = self.sender()
        print('"' + sender.text() + '"' + ' 被按下了')

        qapp = QApplication.instance()         # 获取 QApplication() 对象
        qapp.quit()                            # 关闭窗口


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
