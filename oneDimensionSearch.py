'''
    一维搜索技术
    1. 确定搜索区间->进退法
    2. 寻找最小点->黄金分割法
'''
import matplotlib.pyplot as plt

def calFun1(x): ##exercise 1
    return x*x - 7*x + 10

def calFun(x): ##exercise 2
    return -x*(350-2*x)*(260-2*x) ##use "-"to find minimum

def findSection(calFun, a):
    '''
    f is the function to be resolved, and a is the starting point.
    '''
    h = 1 #path
    a1 = a
    a2 = a1 + h
    f1, f2 = calFun(a1), calFun(a2)
    while 1:
        if f2 <= f1:
            a3 = a2 + h
            f3 = calFun(a3)
            if f3 > f2:
                return [a1, a3]
            elif f3 < f2:
                h = 2 * h
                a1, a2 = a2, a3
                f1, f2 = calFun(a1), calFun(a2)
                a3 = a2 + h
                #f3 = calFun(a3)

        elif f2 > f1:
            h = -h  ##reverse
            a3 = a2
            a2 = a1
            a1 = a3
            f1, f2= calFun(a1),calFun(a2)
            f3 = calFun(a3)
            if f3 > f2:
                return [a1, a3]
            elif f3 < f2:
                h = 2 * h
                a1, a2 = a2, a3
                f1, f2 = calFun(a1), calFun(a2)
                a3 = a2 + h
                #f3 = calFun(a3)

def goldSection(calFun, a0, b0, exp):
    '''
    use this function to find the most possible section
    '''
    a, b = a0, b0
    while 1:
        L = abs(b-a)

        a1 = a + 0.382 * L
        a2 = b - 0.382 * L
        f1, f2 = calFun(a1), calFun(a2)
        if f1 <= f2:
            b = a2

        elif f1 > f2:
            a = a1

        if abs(b-a) < exp:
            return calFun((a+b)/2), (a+b)/2


funSection = findSection(calFun, 0)
print(funSection)
answer = goldSection(calFun, funSection[0], funSection[1], 0.15)
print('When x equals to {b:.5}, function minimum is {a:.10}.'.format(a=-answer[0], b=answer[1]))

##visualization
x= [i for i in range(funSection[0], funSection[1])]
y = [-calFun(i) for i in range(funSection[0], funSection[1])]
plt.scatter(x, y)
plt.draw()
plt.pause(10)