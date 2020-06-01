import random
import matplotlib.pyplot as plt
import math

x = [i for i in range(20)]
ra, rb = 3, 4 ##
y=[0 for i in range(20)]
for m in range(len(x)):
    y2 = random.random()
    ng = random.randint(-10, 10)
    y[m] = (m*rb + ra) + ng*y2

# h(x) = bx + a, a和b是变量
def fuResult(a,b):
    sum = 0
    for i in range(len(x)):
        tx, ty = x[i], y[i]
        sum += (b*tx+a-ty)**2
    return sum/40 ##假设m为1

def grad(a, b):
    g1, g2 = 0, 0
    for i in range(len(x)):
        tx, ty = x[i], y[i]
        g1 += b*tx+a-ty
        g2 += (b*tx+a-ty)*tx
    g1 /= 20
    g2 /= 20
    return g1, g2

def gradDescen(a,b, alpha, eps):
    #print("gradis:",ta, tb)
    while (grad(a,b)[0])**2 + (grad(a,b)[1])**2 > eps**2 : ##梯度未趋于0，做迭代
        gra = grad(a,b)
        print("grad is:", gra[0], gra[1])
        a -= alpha * gra[0]
        b -= alpha * gra[1]
        print(a,b)

    return a,b

m,n = gradDescen(4,6,0.01,0.1)

z = [m+n*x for x in range(20)]
print("y = {:.2f} + {:.2f}x is the best suitable function of the given data".format(m,n))
plt.scatter(x,y)
plt.plot(x,z)
plt.show()
