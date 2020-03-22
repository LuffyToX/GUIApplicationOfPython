# -*- coding: utf-8 -*-
# 加载 GIF 动画效果


import sys
from PyQt5.QtWidgets import QApplication,  QLabel  ,QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.move(800, 300)
        self.setFixedSize(128, 128)
        self.label = QLabel('', self)
        self.setWindowFlags(Qt.Dialog | Qt.CustomizeWindowHint)
        self.movie = QMovie("./images/loading.gif")
        self.label.setMovie(self.movie)
        self.movie.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
