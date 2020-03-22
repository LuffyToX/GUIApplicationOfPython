# -*- coding: utf-8 -*-
# QListWidget 的使用


import sys
from PyQt5.QtWidgets import *


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("MainWindow")
        self.resize(500, 300)

        listWidget = QListWidget()
        listWidget.addItem("Item 1")
        listWidget.addItem("Item 2")
        listWidget.addItem("Item 3")
        listWidget.addItem("Item 4")

        listWidget.itemClicked.connect(self.clicked)

        # 垂直布局
        vbox = QVBoxLayout()
        vbox.addWidget(listWidget)
        self.setLayout(vbox)

    def clicked(self, item):
        QMessageBox.information(self, "ListWidget", "你选择了: "+item.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
