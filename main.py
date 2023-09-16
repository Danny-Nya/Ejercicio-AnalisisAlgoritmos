import random
import time
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


def findPairs(arr, sum):
    pairs = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == sum:
                pairs.append((arr[i], arr[j]))
    return pairs


def generateRandomList(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(0, 2 * n))
    return arr

def ajuste(x,y):
    z=np.polyfit(x,y,2)
    p=np.poly1d(z)
    plt.plot(x,p(x),'r--')
    plt.grid()
    plt.show()

sum = -10000
times1 = []
n = []
N = 100
for i in range(1, N + 1):
    arr = generateRandomList(i)
    n.append(i)
    start = time.perf_counter()
    findPairs(arr, sum)
    end = time.perf_counter()
    times1.append(end - start)
plt.scatter(n, times1)
plt.show()
ajuste(n,times1)
