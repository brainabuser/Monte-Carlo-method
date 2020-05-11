import random

import matplotlib.pyplot as plt

import numpy as np

N = 1000  # number of points
L = float(1000)  # square side value

# plot configuration
plt.figure(figsize=(11, 11))
plt.xlabel('X')
plt.ylabel('Y')
plt.xlim(0, L * 1.1)
plt.ylim(0, L * 1.1)

# draw sector & square
for x in np.arange(0, L, 1):
    plt.plot(x, np.sqrt(L ** 2 - x ** 2), ',', color='m')

# draw square limits
plt.axvline(x=L)
plt.axhline(y=L)

K = 0
for p in range(N):
    x = random.random() * L
    y = random.random() * L
    if x ** 2 + y ** 2 <= L ** 2:
        K = K + 1
        plt.plot(x, y, 'x', color='r')
    else:
        plt.plot(x, y, 'x', color='b')

plt.title('pi = ' + str(4. * K / N))
plt.show()
