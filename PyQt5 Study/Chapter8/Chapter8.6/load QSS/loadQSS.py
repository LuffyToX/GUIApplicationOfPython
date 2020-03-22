# -*- coding: utf-8 -*-
# 加载 QSS 样式的公共类


class LoadQss:
    def __init__(self):
        pass

    @staticmethod
    def readQss(style):
        with open(style, 'r') as f:
            return f.read()
