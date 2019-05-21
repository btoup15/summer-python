import math
import matplotlib.pyplot as plt
import numpy as np

D = np.linspace(.05, .2, 50)  # range of distance in data set
n = 948  # total number of sites in the data set
x = 90  # number of variable sites in the data set
y = []  # set of logarithms for likelihood


def lkl(d):
    l = (x * math.log((1 / 16) - ((1 / 16) * (math.exp((-4 * d) / 3))))) + \
        ((n - x) * math.log((1 / 16) + ((3 / 16) * (math.exp((-4 * d) / 3)))))
    return l


for i in range(len(D)):
    y.append(lkl(D[i]))

plt.plot(D, y)
plt.show()
