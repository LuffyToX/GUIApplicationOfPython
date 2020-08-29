# -*- coding: utf-8 -*-


import numpy as np


# 初始化银行家算法的数据结构（5 个进程，3 类资源）
Available = np.array([3, 3, 2])
Max = np.array([[7,5,3], [3,2,2], [9,0,2], [2,2,2], [4,3,3]])
Allocation = np.array([[0,1,0], [2,0,0], [3,0,2], [2,1,1], [0,0,2]])
Need = np.array([[7,4,3], [1,2,2], [6,0,0], [0,1,1], [4,3,1]])

safeList=[]            # 安全序列
Request=[]             # 请求向量
Request_name=""        # 进程名称


def input_Request():
    global Allocation, Available, Max, Need, safeList, Request, Request_name
    try:
        Request_name = int(input("请输入请求进程的编号：\n0   1    2    3    4\n"))
        Request_new = input("请输入进程 P{} 的请求向量:\n".format(Request_name)).split()
        for x in Request_new:
            Request.append(int(x))
        Request=np.array(Request)
    except:
        print("输入错误，请重新输入")
        input_Request()


def BankerAlgorithm():
    global Allocation, Available, Max, Need, safeList, Request, Request_name
    input_Request()

    if (Request <= Need[Request_name]).all():
        if (Request <= Available).all():
            Available -= Request
            Allocation[Request_name] += Request
            Need[Request_name] -= Request
            safeAlgorithm()
        else:
            print("尚无足够的资源，请等待")
    else:
        print("False！超出宣布的最大值")


def safeAlgorithm():
    Work = Available                                                                      #分配work向量
    Finish = [False]*5                                                                    #分配Finish向量
    cnt = 0
    while True:
        for i in range(0, 5):
            if Finish[i] == False and (Need[i] <= Work).all():
                for j in range(0, 3):
                    Work[j] += Allocation[i][j]
                Finish[i] = True
                safeList.append(i)
                cnt = 0
            else:
                cnt += 1
                continue
        if cnt >= 5:
            break

    if False in Finish:
        print("*"*45)
        print("您输入的请求资源数: {}".format(Request))
        print("您输入的请求进程是 P{}".format(Request_name))
        print("系统安全性：不安全状态")
        print("*"*45)
    else:
        print("*"*45)
        print("您输入的请求进程是 P{}".format(Request_name))
        print("您输入的请求资源数: {}".format(Request))
        print("系统安全性：系统安全")
        print("安全序列为：", safeList)
        print("*"*45)


if __name__ =="__main__":
    BankerAlgorithm()
