# -*- coding: utf-8 -*-
# QMenuBar 的使用（菜单栏）


import sys
from PyQt5.QtWidgets import *


# 必须继承 QMainWindow，才能引用 self.menuBar()
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("MainWindow")
        self.resize(350, 300)

        bar = self.menuBar()                    # 添加一个菜单栏
        file = bar.addMenu("File")              # 添加新的顶层 QMenu() 对象 "File"
        file.addAction("New")                   # 向 "File" 中添加操作按钮 'New'
        save = QAction("Save", self)            # 新建操作按钮 'Save'
        save.setShortcut("Ctrl+S")              # 为 'Save' 设置快捷键 Ctrl+S
        file.addAction(save)                    # 向 "File" 中添加操作按钮 'Save'
        edit = file.addMenu("Edit")             # 添加新的次层 QMenu() 对象 "Edit"
        edit.addAction("copy")                  # 向 "Edit" 中添加操作按钮 'copy'
        edit.addAction("paste")                 # 向 "Edit" 中添加操作按钮 'paste'
        file.addAction("Quit")                  # 向 "File" 中添加操作按钮 'Quit'

        # 菜单发射 truggered 信号
        file.triggered[QAction].connect(self.processtrigger)

    @staticmethod
    def processtrigger(q):
        print(q.text() + " is triggered")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
