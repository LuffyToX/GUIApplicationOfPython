# -*- coding: utf-8 -*-
# QFontDialog 的使用


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class Dialog(QWidget):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)

        self.resize(200, 100)
        self.fontLabel = QLabel("显示选择的字体及大小")
        self.fontLabel.setAlignment(Qt.AlignCenter)
        self.fontButton = QPushButton("choose font")
        self.fontButton.clicked.connect(self.getFont)

        # 垂直布局
        layout = QVBoxLayout()
        layout.addWidget(self.fontLabel)
        layout.addWidget(self.fontButton)
        self.setLayout(layout)

    def getFont(self):
        # QFontDialog.getFont() 方法返回值为元组类型  ==>  (字体, 函数执行状态)
        font, ok = QFontDialog.getFont()
        if ok:
            # 点击 'OK' 按钮
            self.fontLabel.setFont(font)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Dialog()
    win.show()
    sys.exit(app.exec_())
