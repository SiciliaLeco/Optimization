import math
import numpy as np
import matplotlib.pyplot as plt
X = [3]
Y = [4]
timea, timeb = 0, 0
def f(x, y):
    return (2 * x) ** 2 + (2 * y) ** 2

def getGrad(x,y):
   return 2*x, 2*y

def adaGrad(x, y, g1, g2, eta0, eps = 1e-8):
    '''
    :param x: 第一个参数
    :param y: 第二个参数
    :param g1: 第一个参数的梯度平方和的平方根
    :param g2: 第二个参数的梯度平方和的平方根
    :param eta0: 初始的学习率
    :param eps: 平滑值
    :return: 迭代后的x y g1 g2
    '''
    i = 0
    while ((2 * x) ** 2 + (2 * y) ** 2 > 0.1):
        i += 1
        gradx, grady = getGrad(x, y)
        g1 += gradx
        g2 += grady
        x -= eta0 / math.sqrt(g1 + eps) * gradx
        y -= eta0 / math.sqrt(g2 + eps) * grady
        print("第{}次迭代，x = {}, y = {}".format(i, x, y))
        X.append(x)
        Y.append(y)
        #X, Y 存放了每一次迭代的点的信息，便于后续做出

    print("迭代结束，x = {}, y = {}, 对应的解为函数的解f(x, y) = {}.".format(x, y, f(x, y)))
    timea = i
X1 = [3]
Y1 = [4]
def gradDescen(x, y, alpha, eps):
    i = 0
    while((2*x)**2 + (2*y)**2 > eps):
        i += 1
        grad = getGrad(x,y)
        x -= alpha * grad[0]
        y -= alpha * grad[1]
        print("第{}次迭代，x = {}, y = {}".format(i,x,y))
        X1.append(x)
        Y1.append(y)

    timeb = i
    print("final is ({},{}), value is {}".format(x, y, x**2+y**2))

gradDescen(1, 3, 0.03, 0.1)
adaGrad(1, 3, 0, 0, 0.4)

x = np.arange(-1, 4.5, 0.5)
# y = np.arange(-1, 4.5, 0.5)
# [x, y] = np.meshgrid(x, y)
# f = (2 * x) ** 2 + (2 * y) ** 2
# plt.contour(x, y, f, 20)
# plt.plot(X, Y)
# plt.scatter(X, Y,s = 10)
# plt.plot(X1, Y1)
# plt.scatter(X1, Y1, s = 10)
# plt.legend('AG')
#
#
# plt.show()
