# -*- coding: utf-8 -*-
# QClipboard 的使用


import os
import sys
from PyQt5.QtCore import QMimeData
from PyQt5.QtWidgets import QApplication, QDialog, QGridLayout, QLabel, QPushButton
from PyQt5.QtGui import QPixmap


class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.textCopyButton = QPushButton("&Copy Text")
        self.textPasteButton = QPushButton("Paste &Text")
        self.htmlCopyButton = QPushButton("C&opy HTML")
        self.htmlPasteButton = QPushButton("Paste &HTML")
        self.imageCopyButton = QPushButton("Co&py Image")
        self.imagePasteButton = QPushButton("Paste &Image")
        self.textLabel = QLabel("Original text")
        self.imageLabel = QLabel()

        self.initUI()

        # 链接槽函数
        self.textCopyButton.clicked.connect(self.copyText)
        self.textPasteButton.clicked.connect(self.pasteText)
        self.htmlCopyButton.clicked.connect(self.copyHtml)
        self.htmlPasteButton.clicked.connect(self.pasteHtml)
        self.imageCopyButton.clicked.connect(self.copyImage)
        self.imagePasteButton.clicked.connect(self.pasteImage)

    def initUI(self):
        self.setWindowTitle("MainWindow")
        self.imageLabel.setPixmap(QPixmap(r".\images\14.ico"))

        # 表单布局
        layout = QGridLayout()
        layout.addWidget(self.textCopyButton, 0, 0)
        layout.addWidget(self.imageCopyButton, 0, 1)
        layout.addWidget(self.htmlCopyButton, 0, 2)
        layout.addWidget(self.textPasteButton, 1, 0)
        layout.addWidget(self.imagePasteButton, 1, 1)
        layout.addWidget(self.htmlPasteButton, 1, 2)
        layout.addWidget(self.textLabel, 2, 0, 1, 2)
        layout.addWidget(self.imageLabel, 2, 2)
        self.setLayout(layout)

    @staticmethod
    def copyText():
        # QApplication.clipboard() 返回对剪切板对象的引用
        clipboard = QApplication.clipboard()
        clipboard.setText("I've been clipped!")

    def pasteText(self):
        # QApplication.clipboard() 返回对剪切板对象的引用
        clipboard = QApplication.clipboard()
        self.textLabel.setText(clipboard.text())

    def copyImage(self):
        # QApplication.clipboard() 返回对剪切板对象的引用
        clipboard = QApplication.clipboard()
        clipboard.setPixmap(QPixmap(self.ico_path))

    def pasteImage(self):
        # QApplication.clipboard() 返回对剪切板对象的引用
        clipboard = QApplication.clipboard()
        self.imageLabel.setPixmap(clipboard.pixmap())

    def copyHtml(self):
        # QApplication.clipboard() 返回对剪切板对象的引用
        mimeData = QMimeData()
        mimeData.setHtml("<b>Bold and <font color=red>Red</font></b>")
        clipboard = QApplication.clipboard()
        clipboard.setMimeData(mimeData)

    def pasteHtml(self):
        # QApplication.clipboard() 返回对剪切板对象的引用
        clipboard = QApplication.clipboard()
        mimeData = clipboard.mimeData()
        if mimeData.hasHtml():
            self.textLabel.setText(mimeData.html())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    sys.exit(app.exec_())
