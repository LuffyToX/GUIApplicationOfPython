import numpy as np
from matplotlib import pylab as pl

# 定义训练数据
x = np.array([18, 20, 22, 24, 26, 28, 30])
y = np.array([26.86, 28.35, 28.75, 28.87, 29.75, 30.00, 30.36])

# 回归方程求取函数
def fit(x,y):
    if len(x) != len(y):
        return
    numerator = 0.0
    denominator = 0.0
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    for i in range(len(x)):
        numerator += (x[i]-x_mean)*(y[i]-y_mean)
        denominator += np.square((x[i]-x_mean))
    b0 = numerator/denominator
    b1 = y_mean - b0*x_mean
    return b0, b1

# 定义预测函数
def predit(x, b0, b1):
    return b0*x + b1

# 求取回归方程
b0, b1 = fit(x,y)
print('Line is:y = %.4fx + %.4f' % (b0, b1))

# 预测
x_test = np.array([0.5, 1.5, 2.5, 3, 4, 6, 10, 13, 15, 20, 22, 24, 28, 32])
y_test = np.zeros((1, len(x_test)))
for i in range(len(x_test)):
    y_test[0][i] = predit(x_test[i], b0, b1)

# 绘制图像
xx = np.linspace(0, 32)
yy = b0*xx + b1
pl.plot(xx, yy, 'k-')
pl.scatter(x, y, cmap=pl.cm.Paired)
pl.scatter(x_test, y_test[0], cmap=pl.cm.Paired)
pl.show()
