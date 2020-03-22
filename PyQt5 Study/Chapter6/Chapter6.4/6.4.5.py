# -*- coding: utf-8 -*-
# addStretch() 在第一个控件之前添加伸缩量


from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton
import sys


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("MainWindow")
        self.setGeometry(800, 300, 500, 80)

        # 水平布局
        hbox = QHBoxLayout()
        # 添加伸缩控件
        hbox.addStretch(0)
        for i in range(1, 5):
            hbox.addWidget(QPushButton('button'+str(i)))
        self.setLayout(hbox)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
