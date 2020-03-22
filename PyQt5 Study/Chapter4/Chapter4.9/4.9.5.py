# -*- coding: utf-8 -*-
# QFileDialog 的使用


import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Dialog(QWidget):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)

        self.setWindowTitle("Dialog")

        self.btn = QPushButton("加载图片")
        self.btn.clicked.connect(self.getfile)
        self.le = QLabel("")

        self.btn1 = QPushButton("加载文本文件")
        self.btn1.clicked.connect(self.getfiles)
        self.contents = QTextEdit()

        # 垂直布局
        layout = QVBoxLayout()
        layout.addWidget(self.btn)
        layout.addWidget(self.le)
        layout.addWidget(self.btn1)
        layout.addWidget(self.contents)
        self.setLayout(layout)

    """
    QFileDialog.getOpenFileName(QWidget parent, QString caption=QString(),
                                QString dir=QString(), QString filter=QString())
    
    QWidget parent：          父对象
    QString caption：         标题 
    QString dir：             对话框显示时默认打开的目录（. 代表程序运行目录）
    QString filter：          对话框中文件扩展名的过滤器，如：
                              "Image Files (*.jpg *.gif)" 表示只能显示扩展名为 .jpg / .gif 的文件
                              如果需要使用多个过滤器，使用 ";;" 分割，如：
                              "JPEG Files (*.jpg);;PNG Files (*.png)" 
    """

    def getfile(self):
        # QFileDialog.getOpenFileName() 方法返回值是一个元组 (文件路径, 指定文件类型)
        fname, _ = QFileDialog.getOpenFileName(self, 'Open file', 'C:\\', "Image Files (*.jpg *.gif)")
        self.le.setPixmap(QPixmap(fname))

    def getfiles(self):
        dlg = QFileDialog()                     # 新建 QFileDialog 对象
        dlg.setFileMode(QFileDialog.AnyFile)    # 设置可以选择的文件类型 => 任何文件
        dlg.setFilter(QDir.Files)               # 设置过滤器

        if dlg.exec_():
            filenames = dlg.selectedFiles()
            f = open(filenames[0], 'r')

            with f:
                data = f.read()
                self.contents.setText(data)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Dialog()
    win.show()
    sys.exit(app.exec_())
