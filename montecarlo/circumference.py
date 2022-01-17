import random
import matplotlib.pyplot as plt
import numpy as np

N = 100000
p_in_x = np.array([])
p_in_y = np.array([])
p_out_x = np.array([])
p_out_y = np.array([])
for _ in range(N):
    rx = random.random()
    ry = random.random()
    if rx**2+ry**2 <=1:
        # inside
        p_in_x = np.append(p_in_x,rx)
        p_in_y = np.append(p_in_y,ry)
    else:
        p_out_x = np.append(p_out_x,rx)
        p_out_y = np.append(p_out_y,ry)

all = len(p_in_x)+len(p_out_y)
target_area = len(p_in_x)/all
circumference = target_area*4

print(circumference)
plt.plot(p_in_x,p_in_y,'bo')
plt.plot(p_out_x,p_out_y,'ro')
plt.axis('equal')
plt.show()

