import random

import matplotlib.pyplot as plt

import numpy as np

L = float(100)  # 1 area dimension value
N = 100  # needle amount
nLen = 10  # needle length
r = 15  # distance between straight lines

# plot configuration
plt.figure(figsize=(11, 11))
plt.xlabel('X')
plt.ylabel('Y')
plt.xlim(0, L)
plt.ylim(0, L)

# drawing vertical lines
vLines = np.arange(0, L, r)
for v in vLines:
    plt.axvline(x=v, color='k')


def find_nearest_line(right_x):
    lower, upper = float(0), float(L)
    for x in vLines:
        if x <= right_x:
            lower = x
        else:
            upper = x
    if np.abs(lower - right_x) < np.abs(upper - right_x):
        return lower
    else:
        return upper


# main computation part
K = 0
for p in range(N):
    # needle head
    x1 = random.random() * L
    y1 = random.random() * L
    randAngle = random.random() * 2 * np.pi
    # needle tail
    x2 = x1 + nLen * np.cos(randAngle)
    y2 = y1 + nLen * np.sin(randAngle)
    # looking for nearest vertical line from right
    x_near = find_nearest_line(max(x1, x2))
    # distance from head projection to nearest vertical line
    h = x_near - min(x1, x2)
    if h <= x2 - x1:
        plt.plot([x1, x2], [y1, y2], '-,', color='r')
        K = K + 1
    else:
        plt.plot([x1, x2], [y1, y2], '-,', color='b')

plt.title('pi = ' + str(2. * nLen * N / (K * r)))
plt.show()
