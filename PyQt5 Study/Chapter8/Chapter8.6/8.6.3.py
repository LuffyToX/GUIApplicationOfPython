# -*- coding: utf-8 -*-
# 设置窗口透明


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("MainWindow")
        self.setGeometry(800, 300, 500, 400)

        # 设置窗体透明度
        # 透明度取值范围 [0.0 ~ 1.0 ]，默认值为 1.0
        self.setWindowOpacity(0.5)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())


