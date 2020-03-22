# -*- coding: utf-8 -*-
# QFormLayout 表单布局管理器


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFormLayout, QLineEdit, QLabel


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("MainWindow")
        self.setGeometry(800, 300, 300, 100)

        # 表单布局
        formlayout = QFormLayout()
        for i in range(1, 5):
            formlayout.addRow(QLabel("标签"+str(i)), QLineEdit())
        self.setLayout(formlayout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
