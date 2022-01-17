import random
import math
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

# a_s = [2,10,100,1000,10000]
a_s = [10,1000,10000]
# Ks = [1000,5000,10000,20000,40000,100000]
Ks = np.linspace(0,20000,100,dtype=int)
areass = []
for a in tqdm(a_s):
    areas = []
    for K in Ks:
        vals = np.array([])
        for _ in range(K):
            r = random.random()*a
            val = 1/math.sqrt(2*math.pi)*math.exp(-0.5*r**2)
            vals = np.append(vals,val)

        average = vals.mean()
        width = 2*a
        area = average*width
        # print(area)
        areas.append(area)
    areass.append(areas)

for areas in areass:
    plt.plot(Ks,areas)

plt.xlabel('K')
plt.ylabel('area')
plt.legend(a_s)
plt.show()

