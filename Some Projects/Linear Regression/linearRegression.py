# -*- coding: utf-8 -*-
# 线性回归模型 P76 3.4
# 为考察某种维尼纤维的耐水性能，安排了一起实验，测得甲醛浓度 x 与 缩醛化度 y 的数据：
# x  18      20      22      24      26      28      30
# y  26.86   28.35   28.75   28.87   29.75   30.00   30.36
# 从实际经验及理论可知二者近似线性关系，求 y 关于 x 的经验回归方程，并画出原始数据的回归直线图形


import sys
import numpy as np
from matplotlib import pylab as pl
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPainter, QPixmap


class MainWindow(QWidget):
    # 训练数据
    x = np.array([18, 20, 22, 24, 26, 28, 30])
    y = np.array([26.86, 28.35, 28.75, 28.87, 29.75, 30.00, 30.36])

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.iniUI()
        self.regression = linearRegression(self.x, self.y)

    def iniUI(self):
        self.setWindowTitle("linearRegression")
        self.setWindowIcon(QIcon(r".\images\0.ico"))
        self.resize(800, 300)
        self.center()

        self.btn1 = QPushButton()
        self.btn2 = QPushButton()
        self.lab1 = QLabel("开始回归")
        self.lab2 = QLabel("绘制图像")

        self.btn1.setMaximumSize(54, 50)
        self.btn1.setMinimumSize(54, 50)
        self.btn2.setMaximumSize(54, 50)
        self.btn2.setMinimumSize(54, 50)
        style = """
        QPushButton { background-image: url('./images/button.png')}
        """
        self.setStyleSheet(style)
        self.btn1.clicked.connect(self.on_Btn1_click)
        self.btn2.clicked.connect(self.on_Btn2_click)

        self.hbox = QHBoxLayout(self)
        self.hbox.addWidget(self.btn1)
        self.hbox.addStretch(1)
        self.hbox.addWidget(self.lab1)
        self.hbox.addStretch(3)
        self.hbox.addWidget(self.btn2)
        self.hbox.addStretch(1)
        self.hbox.addWidget(self.lab2)
        self.setLayout(self.hbox)

        self.lin = QLineEdit(self)
        self.lin.setText("这里显示回归方程")
        self.lin.setAlignment(Qt.AlignCenter)
        self.lin.resize(400, 50)
        self.lin.move(20, 220)

    def center(self):
        """ 将主窗口居中显示 """
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("./images/background.jpg")
        # 绘制窗口背景，平铺到整个窗口，随着窗口改变而改变
        painter.drawPixmap(self.rect(), pixmap)

    def on_Btn1_click(self):
        b0, b1 = self.regression.fit(self.x, self.y)
        text = 'y = %.4fx + %.4f' % (b0, b1)
        self.lin.setText(text)

    def on_Btn2_click(self):
        self.regression.regressionImg()


class linearRegression:
    def __init__(self, x, y):
        # 定义训练数据
        self.x = x
        self.y = y

    # 回归方程求取函数
    def fit(self, x, y):
        if len(x) != len(y):
            return
        numerator = 0.0
        denominator = 0.0
        x_mean = np.mean(x)
        y_mean = np.mean(y)
        for i in range(len(x)):
            numerator += (x[i] - x_mean) * (y[i] - y_mean)
            denominator += np.square((x[i] - x_mean))
        b0 = numerator / denominator
        b1 = y_mean - b0 * x_mean
        return b0, b1

    # 定义预测函数
    def predit(self, x, b0, b1):
        return b0 * x + b1

    """ 绘制回归图像 """
    def regressionImg(self):
        # 回归参数
        b0, b1 = self.fit(self.x, self.y)
        # 预测
        x_test = np.array([0.5, 1.5, 2.5, 3, 4, 6, 10, 13, 15, 20, 22, 24, 28, 32])
        y_test = np.zeros((1, len(x_test)))
        for i in range(len(x_test)):
            y_test[0][i] = self.predit(x_test[i], b0, b1)

        # 绘制
        xx = np.linspace(0, 32)
        yy = b0 * xx + b1
        pl.plot(xx, yy, 'k-')                               # 拟合直线
        pl.scatter(self.x, self.y, cmap=pl.cm.Paired)       # 原始点
        pl.scatter(x_test, y_test[0], cmap=pl.cm.Paired)    # 预测点
        pl.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

