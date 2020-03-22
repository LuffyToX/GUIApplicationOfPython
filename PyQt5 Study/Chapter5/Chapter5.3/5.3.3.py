# -*- coding: utf-8 -*-
#  QThread 的使用


from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("MainWindow")
        self.setGeometry(800, 300, 500, 400)

        self.thread = Worker()
        self.thread.sinOut.connect(self.slotAdd)

        self.listFile = QListWidget()
        self.btnStart = QPushButton('开始')
        self.btnStart.clicked.connect(self.slotStart)

        # 栅格布局
        layout = QGridLayout()
        layout.addWidget(self.listFile, 0, 0, 1, 2)
        layout.addWidget(self.btnStart, 1, 1)
        self.setLayout(layout)

    def slotAdd(self, file_inf):
        self.listFile.addItem(file_inf)

    def slotStart(self):
        self.btnStart.setEnabled(False)
        self.thread.start()


class Worker(QThread):
    sinOut = pyqtSignal(str)

    def __init__(self, parent=None):
        super(Worker, self).__init__(parent)
        self.working = True
        self.num = 0

    def __del__(self):
        self.working = False
        self.wait()

    def run(self):
        while self.working:
            file_str = 'File index {0}'.format(self.num)
            self.num += 1
            # 发出信号
            self.sinOut.emit(file_str)
            # 线程休眠2秒
            self.sleep(2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
