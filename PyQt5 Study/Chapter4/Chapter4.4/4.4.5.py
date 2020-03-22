# -*- coding: utf-8 -*-
# QTextEdit 的使用


from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout, QPushButton
import sys


class Dialog(QWidget):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)

        self.setWindowTitle("Dialog")
        self.resize(300, 270)

        self.pTextEdit = QTextEdit()
        self.pButton1 = QPushButton("显示文本")
        self.pButton2 = QPushButton("显示HTML")

        # 垂直布局
        layout = QVBoxLayout()
        layout.addWidget(self.pTextEdit)
        layout.addWidget(self.pButton1)
        layout.addWidget(self.pButton2)
        self.setLayout(layout)

        self.pButton1.clicked.connect(self.on_pButton1_Clicked)
        self.pButton2.clicked.connect(self.on_pButton2_Clicked)

    def on_pButton1_Clicked(self):
        self.pTextEdit.setPlainText("猪猪猪猪猪")

    def on_pButton2_Clicked(self):
        self.pTextEdit.setHtml("<font color='red' size='6'><red>猪猪猪猪猪</font>")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Dialog()
    win.show()
    sys.exit(app.exec_())
