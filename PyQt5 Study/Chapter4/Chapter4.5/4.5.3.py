# -*- coding: utf-8 -*-
# QCheckBox 按钮的使用


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class Dialog(QWidget):

    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)

        self.setWindowTitle("Dialog")

        # 如果改变复选钮状态（on <=> off），将触发 stateChanged 信号
        self.checkBox1 = QCheckBox("&Checkbox1")
        self.checkBox1.stateChanged.connect(self.btnstate)

        self.checkBox2 = QCheckBox("Checkbox2")
        self.checkBox2.toggled.connect(self.btnstate)

        self.checkBox3 = QCheckBox("tristateBox")
        self.checkBox3.setTristate(True)                    # 设置复选框为 "三态复选框"
        self.checkBox3.setCheckState(Qt.PartiallyChecked)   # 设置复选框为 "半选中状态"
        self.checkBox3.stateChanged.connect(self.btnstate)

        # 水平布局
        HBox = QHBoxLayout()
        HBox.addWidget(self.checkBox1)
        HBox.addWidget(self.checkBox2)
        HBox.addWidget(self.checkBox3)

        # 添加到 group
        groupBox = QGroupBox("Checkboxes")
        groupBox.setFlat(False)
        groupBox.setLayout(HBox)

        # 垂直布局
        VBox = QVBoxLayout()
        VBox.addWidget(groupBox)

        self.setLayout(VBox)

    def btnstate(self):
        chk1Status = self.checkBox1.text() + ", isChecked=" + str(self.checkBox1.isChecked()) + ', chekState=' + str(
            self.checkBox1.checkState()) + "\n"
        chk2Status = self.checkBox2.text() + ", isChecked=" + str(self.checkBox2.isChecked()) + ', checkState=' + str(
            self.checkBox2.checkState()) + "\n"
        chk3Status = self.checkBox3.text() + ", isChecked=" + str(self.checkBox3.isChecked()) + ', checkState=' + str(
            self.checkBox3.checkState()) + "\n"
        print(chk1Status + chk2Status + chk3Status)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Dialog()
    win.show()
    sys.exit(app.exec_())

