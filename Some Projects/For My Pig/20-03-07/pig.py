import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap, QPainter


class MainWindow(QWidget):
    cnt = 0

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("哎妈呀")
        self.resize(800, 600)
        self.center()
        self.setWindowIcon(QIcon(r".\images\1.ico"))

        self.child = ChildrenWindow()
        self.btnGo = QPushButton("点我你试试")
        self.btnNew = QPushButton("还不能点我哦")
        self.btnNew.setEnabled(False)
        self.lab = QLabel()
        self.lst = QListWidget()
        self.lan = ['为啥？',
                    '你为什么要去洗脸？',
                    '你竟然要洗脸？？',
                    '你要去见谁？？？',
                    '你是不是要见小姐姐！！！',
                    '你是不是不爱我了！',
                    '你是不是要背叛我！！',
                    '你是不是要跟我分手！！！',
                    '渣男！！！！！！！']

        grid = QGridLayout()
        grid.addWidget(self.btnGo, 0, 0, 1, 1)
        grid.addWidget(self.btnNew, 0, 2, 1, 1)
        grid.addWidget(self.lab, 0, 5, 1, 5)
        grid.addWidget(self.lst, 1, 0, 10, 10)
        self.setLayout(grid)

        self.btnGo.clicked.connect(self.on_btnGo_clicked)
        self.btnNew.clicked.connect(self.on_btnNew_clicked)

    def center(self):
        """ 将主窗口居中显示 """
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

    def on_btnGo_clicked(self):
        self.lst.addItem(self.lan[self.cnt] + '\n')
        self.cnt += 1
        if self.cnt > 8:
            self.btnGo.setEnabled(False)
            self.btnGo.setText("看看右边那兄弟")
            self.btnNew.setEnabled(True)
            self.btnNew.setText("点我看证据")
            self.lab.setText("行了行了，自己说的话还不知道有几句吗，傻儿子")

    def on_btnNew_clicked(self):
        self.child.show()


class ChildrenWindow(QMainWindow):
    def __init__(self, parent=None):
        super(ChildrenWindow, self).__init__(parent)

        self.setWindowTitle("没错，就是它")
        self.setWindowIcon(QIcon(r".\images\0.ico"))
        self.resize(500, 900)
        self.center()

    def center(self):
        """ 将主窗口居中显示 """
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

    # 绘图事件
    def paintEvent(self, event):
        """ 设置背景图片，并使图片自适应窗体大小 """
        painter = QPainter(self)
        painter.drawRect(self.rect())
        pixmap = QPixmap(r".\images\2.png")
        painter.drawPixmap(self.rect(), pixmap)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
