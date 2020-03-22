# -*- coding: utf-8 -*-
# QTreeWidget 为节点添加响应事件


from PyQt5.QtWidgets import *
import sys


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("MainWindow")
        self.resize(400, 300)

        self.tree = QTreeWidget()                        # 初始化树形结构实例
        self.tree.setColumnCount(2)                      # 设置列数
        self.tree.setHeaderLabels(['Key', 'Value'])      # 设置头的标题
        self.tree.setColumnWidth(0, 160)                 # 设置列宽

        # 设置根节点
        root = QTreeWidgetItem(self.tree)
        root.setText(0, 'root')
        root.setText(1, '0')

        # 设置 root 的子节点 child1
        child1 = QTreeWidgetItem(root)
        child1.setText(0, 'child1')
        child1.setText(1, '1')

        # 设置 root 的子节点 child2
        child2 = QTreeWidgetItem(root)
        child2.setText(0, 'child2')
        child2.setText(1, '2')

        # 设置 root 的子节点 child3
        child3 = QTreeWidgetItem(root)
        child3.setText(0, 'child3')
        child3.setText(1, '3')

        # 设置 child3 的子节点 child31
        child31 = QTreeWidgetItem(child3)
        child31.setText(0, 'child31')
        child31.setText(1, '31')

        # 设置 child3 的子节点 child32
        child32 = QTreeWidgetItem(child3)
        child32.setText(0, 'child32')
        child32.setText(1, '32')

        self.tree.addTopLevelItem(root)                       # 加载根节点的所有属性与子结点
        self.tree.clicked.connect(self.onTreeClicked)         # 链接槽函数
        self.setCentralWidget(self.tree)                      # 将树形结构设置为主中心窗口

    def onTreeClicked(self):
        item = self.tree.currentItem()
        print("key=%s ,value=%s" % (item.text(0), item.text(1)))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
