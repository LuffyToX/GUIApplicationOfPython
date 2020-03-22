# -*- coding: utf-8 -*-
# 信号与槽的入门应用 自定义信号与槽的使用


from PyQt5.QtCore import QObject, pyqtSignal


# 自定义信号
class QTypeSignal(QObject):
    # 定义一个信号，该信号包含一个参数
    # 必须放在类全局域中
    sendmsg = pyqtSignal(object)

    def __init__(self):
        super(QTypeSignal, self).__init__()

    def run(self):
        # 发射信号
        self.sendmsg.emit("你就是猪")


# 自定义槽
class QTypeSlot(QObject):
    def __init__(self):
        super(QTypeSlot, self).__init__()

    @staticmethod
    def get(msg):
        # 槽函数
        print("QSlot get msg ==> " + msg)


if __name__ == "__main__":
    send = QTypeSignal()
    slot = QTypeSlot()

    # 把信号绑定到槽函数，并发射信号
    send.sendmsg.connect(slot.get)
    send.run()

    # 把信号断开槽函数，并发射信号
    send.sendmsg.disconnect(slot.get)
    send.run()
