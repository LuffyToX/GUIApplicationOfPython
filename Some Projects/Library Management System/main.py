# 图书管理系统入口

import sys
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QAbstractItemView, QTableWidgetItem
from PyQt5.QtGui import QPixmap, QPainter
from loginUI import Ui_loginUI
from studentUI import Ui_StudentUI


class loginUI(QWidget, Ui_loginUI):
    def __init__(self, parent=None):
        super(loginUI, self).__init__(parent)
        self.setupUi(self)

        # 禁止窗口最大化和最小化
        self.setWindowFlags(Qt.WindowCloseButtonHint)

        # 将内置信号链接到自定义槽函数
        self.login_btn.clicked.connect(self.goto)

    def paintEvent(self, event):
        """ 绘制背景 """
        painter = QPainter(self)
        pixmap = QPixmap("./images/login background.jpg")
        # 绘制窗口背景，平铺到整个窗口，随着窗口改变而改变
        painter.drawPixmap(self.rect(), pixmap)

    def check(self, string):
        """ 用户名及密码仅能为数字、字母、特殊字符的组合 """
        letters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                   'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                   'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
                   'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                   'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                   'Y', 'Z', '!', '~', '@', '#', '$', '%', '^', '&',
                   '*', '(', ')', '-', '=', '+', ':', ';', '"', '<',
                   '>', ',', '.', '?', '/', '\\', '{', '}', '[', ']',
                   '|', "'"]
        for i in string:
            if i not in letters:
                return False
            else:
                return True

    def goto(self):
        """ 登录跳转（学生/管理员） """
        if self.check(self.user_ld.text()) and self.check(self.password_ld.text()):
            if self.student_rb.isChecked():
                self.stuUI = studentUI()
                self.stuUI.show()
                self.close()
            elif self.librarian_rb.isChecked():
                print("librarian login")
        else:
            QMessageBox.warning(self, "title", "请输入正确的用户名及密码", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)


class studentUI(QWidget, Ui_StudentUI):
    def __init__(self, parent=None):
        super(studentUI, self).__init__(parent)
        self.setupUi(self)

        # 禁止窗口最大化和最小化
        self.setWindowFlags(Qt.WindowCloseButtonHint)

        # 设置表格的水平表头标签
        self.query_tw.setHorizontalHeaderLabels(["书名", "作者", "剩余馆藏/本", "书籍总数/本", "书架号"])

        # 将表格变为禁止编辑的
        self.query_tw.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # 将内置信号链接到自定义槽函数
        self.query_btn.clicked.connect(self.query_book)
        self.borrow_btn.clicked.connect(self.borrow_book)
        self.back_btn.clicked.connect(self.back_book)

    def paintEvent(self, event):
        """ 绘制背景 """
        painter = QPainter(self)
        pixmap = QPixmap("./images/student background.png")
        # 绘制窗口背景，平铺到整个窗口，随着窗口改变而改变
        painter.drawPixmap(self.rect(), pixmap)

    def query_book(self):
        """ 查询操作槽函数 """
        with open('bookDatabase.txt', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                name, author, state, amount, position = line.rstrip().split('，')
                if name == self.query_ld.text():
                    lists = [(0, name), (1, author), (2, state), (3, amount), (4, position)]
                    for itemcotent in lists:
                        item = QTableWidgetItem(itemcotent[1])
                        item.setTextAlignment(Qt.AlignHCenter)
                        self.query_tw.setItem(0, itemcotent[0], item)
                    return True
        QMessageBox.information(self, "title", "本图书馆没有收录此书籍", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        return False

    def borrow_book(self):
        """ 借阅操作槽函数 """
        with open('bookDatabase.txt', 'r', encoding='utf-8') as fileR:
            lines = fileR.readlines()
        with open('bookDatabase.txt', 'w', encoding='utf-8') as fileW:
            lineNum = 0
            for line in lines:
                name, author, state, amount, position = line.rstrip().split('，')
                if name == self.borrow_ld.text():
                    state = int(state)
                    if state > 0:
                        lines[lineNum] = name + '，' + author + '，' + str(state-1) + '，' + amount + '，' + position + '\n'
                        QMessageBox.information(self, "title", "借阅成功", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                    else:
                        QMessageBox.information(self, "title", "此书已全部借出", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                    print(lines)
                    fileW.writelines(lines)
                    return True
                lineNum = lineNum + 1
        QMessageBox.information(self, "title", "本图书馆没有收录此书籍", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        return False

    def back_book(self):
        """ 归还操作槽函数 """
        with open('bookDatabase.txt', 'r', encoding='utf-8') as fileR:
            lines = fileR.readlines()
        with open('bookDatabase.txt', 'w', encoding='utf-8') as fileW:
            lineNum = 0
            for line in lines:
                name, author, state, amount, position = line.rstrip().split('，')
                if name == self.back_ld.text():
                    state = int(state)
                    if state < int(amount):
                        lines[lineNum] = name + '，' + author + '，' + str(state+1) + '，' + amount + '，' + position + '\n'
                        QMessageBox.information(self, "title", "还书成功", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                    else:
                        QMessageBox.information(self, "title", "馆藏可没这么多", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                    print(lines)
                    fileW.writelines(lines)
                    return True
                lineNum = lineNum + 1
        QMessageBox.information(self, "title", "本图书馆没有收录此书籍", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        return False









if __name__ == "__main__":
    # 下面这行代码可以确保运行界面与 Qt Designer 预览界面一致
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

    app = QApplication(sys.argv)
    myWin = loginUI()
    myWin.show()
    sys.exit(app.exec_())