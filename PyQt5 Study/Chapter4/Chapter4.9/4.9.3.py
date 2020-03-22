# -*- coding: utf-8 -*-
# QInputDialog 的使用


import sys
from PyQt5.QtWidgets import *


class Dialog(QWidget):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)

        self.setWindowTitle("Dialog")

        self.btn1 = QPushButton("获得列表里的选项")
        self.btn1.clicked.connect(self.getItem)
        self.le1 = QLineEdit()

        self.btn2 = QPushButton("获得字符串")
        self.btn2.clicked.connect(self.getText)
        self.le2 = QLineEdit()

        self.btn3 = QPushButton("获得整数")
        self.btn3.clicked.connect(self.getInt)
        self.le3 = QLineEdit()

        # 表单布局
        layout = QFormLayout()
        layout.addRow(self.btn1, self.le1)
        layout.addRow(self.btn2, self.le2)
        layout.addRow(self.btn3, self.le3)
        self.setLayout(layout)

    """
    QInputDialog：该类提供了一种简单方便的对话框来获取用户的单个输入信息，提供了 4 种数据类型的输入：
    
    1. getInt()：     从控件中获取标准 int        类型输入
    2. getDouble()：  从控件中获取标准 double     类型输入
    3. getText()：    从控件中获取标准 str        类型输入
    4. getItem()：    从控件中获取标准 下拉列表框  条目输入
    
    以上方法的返回值均为元组  ==>  (获取的输入, 函数执行状态)
    
    一个标准输入对话框包含：一个提示标签、一个输入控件：
    
    1. getInt()：     一个 QSpinBox 控件   +   一个 'OK' 按钮   +   一个 'Cancel' 按钮
    2. getDouble()：  一个 QSpinBox 控件   +   一个 'OK' 按钮   +   一个 'Cancel' 按钮
    3. getText()：    一个 QLineEdit 控件  +   一个 'OK' 按钮   +   一个 'Cancel' 按钮
    4. getItem()：    一个 QComboBox 控件  +   一个 'OK' 按钮   +   一个 'Cancel' 按钮
    
    1. getInt(QWidget parent, QString title, QString label, int value=0, 
              int minValue=-2147483647, int maxValue=2147483647, int step=1, bool ok=0)
       QWidget parent：父窗口
       QString title： 标题
       QString label： 标签提示
       int value：     QSpinBox 控件的显示值，默认为 0
       int minValue：  QSpinBox 控件的取值范围，最小值默认为 -2147483647
       int maxValue：                          最大值默认为  2147483647
       int step：      QSpinBox 控件的步长，默认为 1
       bool ok：       指示标准输入对话框的哪个按钮被触发：
                                           ok=True   ==>  表示用户单击了 'OK' 按钮
                                           ok=False  ==>  表示用户单击了 'Cancel' 按钮

    2. getDouble(QWidget parent, QString title, QString label, double value=0,
                 double minValue=-2147483647, double maxValue=2147483647, int decimals = 1, bool ok=0）
       int decimals：  QSpinBox 控件的小数点位数，默认为 1
       
    3. getText(QWidget parent, QString title, QString label, QString text=QString(), bool ok=0)
       QString text：  QLineEdit 控件中默认出现的文字
    
    4. getItem(QWidget parent, QString title, QString label, QStringList list,
               int current=0, bool editable=True, bool ok=0,
       QStringList list： 指定 QComboBox 控件中的条目
       int current：      指定 QComboBox 控件中当前显示条目的索引，默认为 0
       bool editable：    指定 QComboBox 控件中的条目是否可编辑，默认为 True 
    """

    def getItem(self):
        items = ("C", "C++", "Java", "Python")
        item, ok = QInputDialog.getItem(self, "getItem", "编程语言", items, editable=False)
        if ok and item:
            # 选择了 'OK' 按钮
            self.le1.setText(item)

    def getText(self):
        text, ok = QInputDialog.getText(self, "getText", "输入姓名:")
        if ok:
            # 选择了 'OK' 按钮
            self.le2.setText(str(text))

    def getInt(self):
        num, ok = QInputDialog.getInt(self, "getInt", "输入数字")
        if ok:
            # 选择了 'OK' 按钮
            self.le3.setText(str(num))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Dialog()
    win.show()
    sys.exit(app.exec_())
