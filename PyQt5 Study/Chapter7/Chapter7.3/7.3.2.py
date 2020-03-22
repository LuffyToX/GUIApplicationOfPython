# -*- coding: utf-8 -*-
# 使用自定义参数 lambda 表达式


from PyQt5.QtWidgets import *
import sys


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("MainWindow")
        self.setGeometry(800, 300, 300, 200)

        button1 = QPushButton('Button 1')
        button2 = QPushButton('Button 2')

        # clicked 信号本身不传递参数
        # 使用 lambda 表达式传递参数
        button1.clicked.connect(lambda: self.onButtonClick(1))
        button2.clicked.connect(lambda: self.onButtonClick(2))

        layout = QHBoxLayout()
        layout.addWidget(button1)
        layout.addWidget(button2)

        main_frame = QWidget()
        main_frame.setLayout(layout)
        self.setCentralWidget(main_frame)

    def onButtonClick(self, n):
        print('Button {0} 被按下了'.format(n))
        QMessageBox.information(self, "信息提示框", 'Button {0} clicked'.format(n))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
