# -*- coding: utf-8 -*-
# 信号/槽机制 使用 Qt Designer 实现界面与逻辑的分离


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import pyqtSignal, Qt
from MainWindow import Ui_Form


class MyMainWindow(QMainWindow, Ui_Form):
    helpSignal = pyqtSignal(str)                       # 带 strt 参数的信号
    printSignal = pyqtSignal(list)                     # 带 list 参数的信号
    previewSignal = pyqtSignal([int, str], [str])      # 多重载版本的信号 [int ,str] / [str]

    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.helpSignal.connect(self.showHelpMessage)
        self.printSignal.connect(self.printPaper)
        self.previewSignal[str].connect(self.previewPaper)
        self.previewSignal[int, str].connect(self.previewPaperWithArgs)

        self.printButton.clicked.connect(self.emitPrintSignal)
        self.previewButton.clicked.connect(self.emitPreviewSignal)

    # 发射预览信号
    def emitPreviewSignal(self):
        if self.previewStatus.isChecked():
            self.previewSignal[int, str].emit(1080, " Full Screen")
        elif not self.previewStatus.isChecked():
            self.previewSignal[str].emit("Preview")

    # 发射打印信号
    def emitPrintSignal(self):
        pList = list()
        pList.append(self.numberSpinBox.value())
        pList.append(self.styleCombo.currentText())
        self.printSignal.emit(pList)

    def printPaper(self, lst):
        self.resultLabel.setText("打印: " + "份数：" + str(lst[0]) + " 纸张：" + str(lst[1]))

    def previewPaperWithArgs(self, style, text):
        self.resultLabel.setText(str(style) + text)

    def previewPaper(self, text):
        self.resultLabel.setText(text)

    # 重载点击键盘事件
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_F1:
            self.helpSignal.emit("help message")

    # 显示帮助消息
    def showHelpMessage(self, message):
        self.resultLabel.setText(message)
        self.statusBar().showMessage(message)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyMainWindow()
    win.show()
    sys.exit(app.exec_())
