# -*- coding: utf-8 -*-
# 设置窗口风格


import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("Style")
        self.setGeometry(800, 300, 300, 100)

        self.styleLabel = QLabel("设置界面风格")
        self.styleComboBox = QComboBox()

        # QStyleFactory.keys()
        # 获取当前平台支持的原有的 QStyle 样式
        self.styleComboBox.addItems(QStyleFactory.keys())

        # 选择当前界面风格
        index = self.styleComboBox.findText(QApplication.style().objectName(),\
                                            QtCore.Qt.MatchFixedString)
        self.styleComboBox.setCurrentIndex(index)

        # 通过 comboBox 选择界面风格
        self.styleComboBox.activated[str].connect(self.handleStyleChanged)

        # 水平布局
        hbox = QHBoxLayout()
        hbox.addWidget(self.styleLabel)
        hbox.addWidget(self.styleComboBox)
        self.setLayout(hbox)

    """ 改变界面风格 """
    @staticmethod
    def handleStyleChanged(style):
        QApplication.setStyle(style)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
