import os
import math
from numpy import *

os.system('cls')

n = int(input('Enter the number of sites in the data set: '))
x = int(input('Enter the number of differences among those sites: '))


def P(diff, num):
    p = diff / num
    return p


def distance(diff, num):
    p = P(diff, num)
    d = ((-3/4) * log(1 - ((4 / 3) * p)))
    return d


def sterr(diff, num):
    p = P(diff, num)
    err = (p * (1 - p)) / ((1 - ((4 * p) / 3) ** 2) * num)
    conf = (1.96 * sqrt(err))
    return conf


os.system('cls')
print('The distance of the two sequences is {} +/- {}'.format(round(distance(x, n), 4), round(sterr(x, n), 4)))
print('The 95% confidence interval is ({}, {})'.format(
    (round((distance(x, n) - sterr(x, n)), 4)), (round((distance(x, n) + sterr(x, n)), 4))))
