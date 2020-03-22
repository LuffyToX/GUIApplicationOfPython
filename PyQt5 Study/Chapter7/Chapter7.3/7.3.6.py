# -*- coding: utf-8 -*-
# 多线程 后台更新数据


from PyQt5.QtCore import QThread, pyqtSignal, QDateTime
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit, QHBoxLayout
import time
import sys


class BackendThread(QThread):
    # 带 str 参数的信号
    update_date = pyqtSignal(str)

    # 处理要做的业务逻辑
    def run(self):
        while True:
            data = QDateTime.currentDateTime()
            currTime = data.toString("yyyy-MM-dd hh:mm:ss")
            # 发射信号
            self.update_date.emit(str(currTime))
            time.sleep(1)


class Dialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        self.setWindowTitle("Dialog")
        self.setGeometry(800, 300, 300, 100)

        hbox = QHBoxLayout(self)
        self.input = QLineEdit()
        hbox.addWidget(self.input)

        # 创建线程，并连接槽函数
        self.backend = BackendThread()
        self.backend.update_date.connect(self.handleDisplay)
        self.backend.start()

    # 将当前时间输出到文本框
    def handleDisplay(self, data):
        self.input.setText(data)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Dialog()
    win.show()
    sys.exit(app.exec_())
