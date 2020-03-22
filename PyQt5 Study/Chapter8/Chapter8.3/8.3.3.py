# -*- coding: utf-8 -*-
# QSS 子控件


from PyQt5.QtWidgets import *
import sys


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.InitUI()

    def InitUI(self):
        self.setWindowTitle("MainWindow")
        self.setGeometry(800, 300, 300, 200)

        combo = QComboBox(self)
        combo.setObjectName('myQComboBox')
        combo.resize(100, 30)
        combo.addItems(['Window', 'Ubuntu', 'Red Hat'])
        combo.move(100, 50)

        # QSS 子控件选择器
        # 指定 ID 为 myQComboBox 的 QComboBox 控件的下拉箭头为自定义图片
        qssStyle = " QComboBox#myQComboBox::drop-down {image: url( ./images/dropdown.png)} "
        self.setStyleSheet(qssStyle)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

