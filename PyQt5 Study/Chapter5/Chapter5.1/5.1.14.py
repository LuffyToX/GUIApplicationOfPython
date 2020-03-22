# -*- coding: utf-8 -*-
# QTreeWidget 树形结构的实现1


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QBrush, QColor
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("MainWindow")
        self.resize(400, 300)

        self.tree = QTreeWidget()                         # 初始化树形结构实例
        self.tree.setColumnCount(2)                       # 设置列数
        self.tree.setHeaderLabels(['Key', 'Value'])       # 设置头的标题
        self.tree.setColumnWidth(0, 160)                  # 设置列宽

        # 设置根节点，继承自树形结构 self.tree
        root = QTreeWidgetItem(self.tree)
        root.setText(0, 'root')
        root.setIcon(0, QIcon(r".\images\root.png"))
        # 设置节点的背景颜色
        brush_red = QBrush(Qt.red)
        root.setBackground(0, brush_red)
        brush_green = QBrush(Qt.green)
        root.setBackground(1, brush_green)

        # 设置子节点1，继承自根节点 root ==> child1 是 root 的子节点
        child1 = QTreeWidgetItem(root)
        child1.setText(0, 'child1')
        child1.setText(1, 'ios')
        child1.setIcon(0, QIcon(r".\images\IOS.png"))
        # 设置结点指定列的选中状态
        # child1.setCheckState(0, Qt.Checked)

        # 设置子节点2，继承自根节点 root ==> child2 是 root 的子节点
        child2 = QTreeWidgetItem(root)
        child2.setText(0, 'child2')
        child2.setText(1, 'android')
        child2.setIcon(0, QIcon(r".\images\android.png"))

        # 设置子节点21，继承自根节点 root ==> child21 是 child2 的子节点
        child21 = QTreeWidgetItem(child2)
        child21.setText(0, 'child21')
        child21.setText(1, '')
        child21.setIcon(0, QIcon(r".\images\music.png"))

        self.tree.addTopLevelItem(root)           # 加载根节点的所有属性与子结点
        self.tree.expandAll()                     # 结点全部展开
        self.setCentralWidget(self.tree)          # 将树形结构设置为主中心窗口


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
