#f(x,y)=x*cos(2*pi*y)+y*sin(2*pi*x)
#要求：种群初始随机，范围分别为[-2, 2]、[-2, 2]，染色体长度为20，交叉概率0.7，变异概率为0.01
import math
import matplotlib.pyplot as plt
import numpy as np

chroms_size = 20
dna_size = 10
pop_size = 10 #暂定可修改
generation = 300 #暂定可修改
crossover_ratio = 0.7
mutation_ratio = 0.01
x_bound = [-2, 2]
y_bound = [-2, 2]

def aimFun(x, y):
    return  x * np.cos(2 * math.pi * y) + y * np.sin(2 * math.pi * x)

def decode(pop):
    '''
    :param pop: a np array
    :return x, y: decode result of pop array
    '''
    x_population = pop[:, 1::2] #奇数列
    y_population = pop[:,::2] #偶数列
    x = x_population.dot(2**np.arange(dna_size)[::-1])/\
            float(2**dna_size - 1) * (x_bound[1] - x_bound[0]) + x_bound[0]
    y = y_population.dot(2**np.arange(dna_size)[::-1])/\
            float(2**dna_size - 1) * (y_bound[1] - y_bound[0]) + y_bound[0]
    return x, y

def fitness_evaluate(pop):
    '''
    求最大适应度
    :param pop: 种群
    :return: 每一组xy值计算得到的结果对应的适应度值，防止负数出现
    '''
    x, y = decode(pop)
    cal = aimFun(x, y)
    return cal-np.min(cal) + 0.001 # +0.01防止出现0


def select(pop, fitness):
    '''
    按照轮盘赌选法，选出种群（其实是按被选出的顺序排列）
    :param pop:
    :param fitness:
    :return:
    '''
    idx = np.random.choice(np.arange(pop_size),
                           size=pop_size, replace=True, p = (fitness) / (fitness.sum()))
    return pop[idx]

def crossover(pop, crossover_ratio):
    '''
    :param pop: 种群
    :param crossover_ratio: 交叉的概率
    :param cpoint: 交叉的点，随机选取的
    :return: 婚配的结果
    '''
    new_population = []
    for f in pop:
        child = f #默认继承了父亲
        if np.random.rand() < crossover_ratio:
            m = pop[np.random.randint(pop_size)] ##母亲
            cpoint = np.random.randint(low = 0, high = chroms_size)
            #单点交叉
            child[cpoint:] = m[cpoint:] #后半段由母亲给
        mutation(child, mutation_ratio)
        new_population.append(child)
    return new_population

def mutation(chromosone, mutation_ratio):
    if np.random.rand() < mutation_ratio:
        mpoint = np.random.randint(low = 0, high = dna_size)
        chromosone[mpoint] ^= 1


best_per_generation = [] #记录每次完成迭代后的最优解
population = np.random.randint(2, size = (pop_size, chroms_size))

##算法开始，一共迭代generation次
for i in range(generation):
    crossover(population, crossover_ratio)
    fitness = fitness_evaluate(population)
    population = select(population, fitness)

    ix, iy = decode(population)
    result = aimFun(ix, iy).tolist()

    best_per_generation.append(max(result))

print("calculation result is :" ,best_per_generation[-1])
plt.plot(best_per_generation) #作图
plt.show()
