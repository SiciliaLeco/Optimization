'''
   One Dimension Search Method
   In this context, the finding process is under 2d, which might unfortunately fall into
   Local optimal solution.
   findSection() helps to find the most possible section that the minimum hides, parameter a
   will influence the result
   goldSection() applies to the section found by findSection(), and return the minimum info
   it uses the magic number 0.618 to update the section.


'''

import matplotlib.pyplot as plt
import math
import numpy as np

def calFun1(x): ##exercise 1
    return x*x - 7*x + 10

def calFun(x): ##exercise 2
    return 2*(x**2)-2*x-1

def drvt1(x): #first derivative of a function
    return 4*(x**3-3*(x**2)-3*x-4)
def drvt2(x): #second derivative
    return  12*(x**2-2*x-1)

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

def goldSection(calFun, a0, b0, exp):
    '''
    use this function to find the most possible section
    when the length of the seciton is minor to exp, end.
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

def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)

def fiboSect(calFun, a, b, exp):
    '''
    calFun is the function, a0 b0 denotes the section.
    fn>=(b-a)/exp
    '''
    n=0
    while fibo(n)<(b-a)/exp:
        n=n+1
    ##find the index of the matched fn
    x1 = (b - a) * fibo(n - 2) / fibo(n) + a
    x2 = (b - a) * fibo(n - 1) / fibo(n) + a ## x1<x2
    f1, f2=calFun(x1), calFun(x2)
    for k in range(1, n): ##from 1 to n-1
        if f1<=f2:
            b = x2
            x2 = x1
            x1 = a + (b-a) * fibo(n-2-k)/fibo(n)
        elif f1>f2:
            a = x1
            x1 = x2
            x2 = a + (b-a) * fibo(n-1-k)/fibo(n)
        f1, f2 = calFun(x1), calFun(x2)
    if f1<f2:
        b=x2
    else:
        a=x1
    return [a,b] ##return the most possible section of the minimum

def newtonIns(fun1, fun2, a0, eps):
    k=0
    f1a, f2a = fun1(a0), fun2(a0)
    a1 = a0 - f1a/f2a
    while abs(a1-a0) > eps: #math/fabs
        k+=1
        a0 = a1
        f1a, f2a = fun1(a0), fun2(a0)
        a1 = a0 - f1a / f2a
    return a1


print(fiboSect(calFun, 0, 0.6, 0.16))
print(newtonIns(drvt1, drvt2, 3, 0.001))

#visualization
plt.figure(1)
x=np.linspace(3,10,10)
plt.plot(x, x**4-4*x**3-6*x**2-16*x)
plt.show()
