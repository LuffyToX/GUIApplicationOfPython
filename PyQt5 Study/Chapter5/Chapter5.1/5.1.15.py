# -*- coding: utf-8 -*-
# QTreeWidget 树形结构的实现2


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

        # 根节点列表，只需添加根节点
        rootList = list()

        # 设置根节点
        root = QTreeWidgetItem()
        root.setText(0, 'root')
        root.setIcon(0, QIcon(r".\images\root.png"))
        # 设置根节点的背景颜色
        brush_red = QBrush(Qt.red)
        root.setBackground(0, brush_red)
        brush_green = QBrush(Qt.green)
        root.setBackground(1, brush_green)
        # 将 root 添加到根节点列表中
        rootList.append(root)

        # 设置子节点1
        child1 = QTreeWidgetItem()
        child1.setText(0, 'child1')
        child1.setText(1, 'ios')
        child1.setIcon(0, QIcon(r".\images\IOS.png"))
        child1.setCheckState(0, Qt.Checked)
        # child1 是 root 的子节点
        root.addChild(child1)

        # 设置子节点2
        child2 = QTreeWidgetItem(root)
        child2.setText(0, 'child2')
        child2.setText(1, 'android')
        child2.setIcon(0, QIcon(r".\images\android.png"))
        # child2 是 root 的子节点
        root.addChild(child2)

        # 设置子节点21
        child21 = QTreeWidgetItem(child2)
        child21.setText(0, 'child21')
        child21.setText(1, '')
        child21.setIcon(0, QIcon(r".\images\music.png"))
        # child21 是 child2 的子节点
        child2.addChild(child21)

        # QTreeWidgetinsertTopLevelItem (0, root)      在树形结构的顶层插入根节点
        # QTreeWidgetinsertTopLevelItems(0, rootList)  在树形结构的顶层插入根节点列表
        self.tree.insertTopLevelItems(0, rootList)
        self.tree.expandAll()                          # 结点全部展开
        self.setCentralWidget(self.tree)               # 将树形结构设置为主中心窗口


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
