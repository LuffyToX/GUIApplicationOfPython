# -*- coding: utf-8 -*-
# QGridLayout 单一的网格单元格


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("计算器")
        self.setGeometry(800, 300, 500, 400)

        # 栅格布局
        grid = QGridLayout()
        self.setLayout(grid)

        # 计算器按钮
        names = ['Cls', 'Back', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']
        positions = [(i, j) for i in range(5) for j in range(4)]
        for position, name in zip(positions, names):
            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
