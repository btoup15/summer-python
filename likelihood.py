import math
import matplotlib.pyplot as plt

D = []  # distances for each number X in the data set
n = 948  # total number of sites in the data set
X = []  # number of different sites in the data set
y = []  # set of logarithms for likelihood


for s in range(1, 400, 10):
    X.append(s)

for num in X:
    d = ((-3/4) * math.log(1 - ((4 / 3) * (num / n))))
    D.append(d)


def lkl(x, d):
    l = (x * math.log((1 / 16) - ((1 / 16) * (math.exp((-4 * d) / 3))))) + \
        ((n - x) * math.log((1 / 16) + ((3 / 16) * (math.exp((-4 * d) / 3)))))
    return l
# calculates the natural logarithm of likelihood since likelihood itself is generally too small to work with


for i in range(len(X)):
    y.append(lkl(X[i], D[i]))

plt.plot(D, y)
plt.show()
