'''
Implementation for Buffon's computational method
'''
import random

import matplotlib.pyplot as plt

import numpy as np

L = float(100)  # 1 area dimension value
N = 1000  # needle amount
N_LEN = 1  # needle length
R = 3  # distance between straight lines

# plot configuration
plt.figure(figsize=(11, 11))
plt.xlabel('X')
plt.ylabel('Y')
plt.xlim(0, L)
plt.ylim(0, L)

# drawing vertical lines
vLines = np.arange(0, L, R)
for v in vLines:
    plt.axvline(x=v, color='k')


def find_nearest_line(right_x):
    '''
    Finds nearest vertical line to needle's tail

    :param right_x:
    :type right_x: float

    :return:
    :rtype: float
    '''
    lower, upper = 0., 0.
    for x_var in vLines:
        if x_var <= right_x:
            lower = x_var
        else:
            upper = x_var
            break
    if np.abs(lower - right_x) < np.abs(upper - right_x):
        return lower
    return upper


# main computation part
K = 0
for p in range(N):
    # needle head
    x1 = random.random() * L
    y1 = random.random() * L
    randAngle = random.random() * 2 * np.pi
    # needle tail
    x2 = x1 + N_LEN * np.cos(randAngle)
    y2 = y1 + N_LEN * np.sin(randAngle)
    # looking for nearest vertical line from right
    x_near = find_nearest_line(max(x1, x2))
    # distance from head projection to nearest vertical line
    h = abs(x_near - min(x1, x2))
    if h <= abs(x2 - x1) and (min(x1, x2) <= x_near):
        plt.plot([x1, x2], [y1, y2], '-,', color='r')
        K += 1
    else:
        plt.plot([x1, x2], [y1, y2], '-,', color='b')

plt.title('pi = ' + str(2. * N_LEN * N / (K * R)))
plt.show()
