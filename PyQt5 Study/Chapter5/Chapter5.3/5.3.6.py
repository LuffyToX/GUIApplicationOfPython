# -*- coding: utf-8 -*-
# QApplication.processEvents() 实时刷新页面


from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QListWidget, QGridLayout
import sys
import time


class MainWindow(QWidget):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("MainWindow")
        self.setGeometry(800, 300, 300, 300)

        self.listFile = QListWidget()
        self.btnStart = QPushButton('开始')
        self.btnStart.clicked.connect(self.slotAdd)

        # 栅格布局
        layout = QGridLayout()
        layout.addWidget(self.listFile, 0, 0, 1, 2)
        layout.addWidget(self.btnStart, 1, 1)
        self.setLayout(layout)

    def slotAdd(self):
        for n in range(10):
            str_n = 'File index {0}'.format(n)
            self.listFile.addItem(str_n)
            # 实时刷新页面
            QApplication.processEvents()
            time.sleep(0.5)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
