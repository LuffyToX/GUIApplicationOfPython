# -*- coding: utf-8 -*-
# 高级自定义信号与槽


from PyQt5.QtCore import QObject, pyqtSignal


class CustSignal(QObject):

    # 声明信号（类全局作用域）
    signal1 = pyqtSignal()                     # 声明一个无参数的信号
    signal2 = pyqtSignal(int)                  # 声明带一个 int 类型参数的信号
    signal3 = pyqtSignal(int, str)             # 声明带一个 int 和 str 类型参数的信号
    signal4 = pyqtSignal(list)                 # 声明带一个 list 类型参数的信号
    signal5 = pyqtSignal(dict)                 # 声明带一个 dict 类型参数的信号
    signal6 = pyqtSignal([int, str], [str])    # 声明一个多重载版本的信号，[int, str] / [str]

    def __init__(self, parent=None):
        super(CustSignal, self).__init__(parent)

        # 信号连接到指定槽
        self.signal1.connect(self.signalCall1)
        self.signal2.connect(self.signalCall2)
        self.signal3.connect(self.signalCall3)
        self.signal4.connect(self.signalCall4)
        self.signal5.connect(self.signalCall5)
        self.signal6[int, str].connect(self.signalCall6)       # 信号参数 [int, str]
        self.signal6[str].connect(self.signalCall6OverLoad)    # 信号参数 [str]

        # 信号发射
        self.signal1.emit()                                    # signal1 无参数
        self.signal2.emit(1)                                   # signal2 [int]
        self.signal3.emit(1, "text")                           # signal3 [int, str]
        self.signal4.emit([1, 2, 3, 4])                        # signal4 [list]
        self.signal5.emit({"name": "wangwu", "age": "25"})     # signal5 [dict]
        self.signal6[int, str].emit(1, "text")                 # signal6 [int, str]
        self.signal6[str].emit("text")                         # signal6 [str]

    @staticmethod
    def signalCall1():
        print("signal1 emit")

    @staticmethod
    def signalCall2(val):
        print("signal2 emit, value:", val)

    @staticmethod
    def signalCall3(val, text):
        print("signal3 emit, value:", val, text)

    @staticmethod
    def signalCall4(val):
        print("signal4 emit, value:", val)

    @staticmethod
    def signalCall5(val):
        print("signal5 emit, value:", val)

    @staticmethod
    def signalCall6(val, text):
        print("signal6 emit, value:", val, text)

    @staticmethod
    def signalCall6OverLoad(val):
        print("signal6 overload emit,value:", val)


if __name__ == "__main__":
    custSignal = CustSignal()
