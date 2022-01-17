import numpy
import math
import random
import matplotlib.pyplot as plt

N = 10000
xs = []
ys = []
for _ in range(N):
    p = random.random()
    q = random.random()
    x = math.sqrt(-2*math.log(p))*math.cos(2*math.pi*q)
    y = math.sqrt(-2*math.log(p))*math.sin(2*math.pi*q)
    xs.append(x)
    ys.append(y)
plt.hist(xs,100)
# plt.legend(['x','y'])
plt.figure()
plt.hist(ys,100)

plt.show()