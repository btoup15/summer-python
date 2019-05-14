from numpy import *
import math
import time
import os

T = []
C = []
A = []
G = []

bases = ['T', 'C', 'A', 'G']

os.system('cls')
# populates each base list with the number of occurances in the data set
for letters in bases:
    T.append(int(input('Enter the number of T to {} conversions: '.format(letters))))
for letters in bases:
    C.append(int(input('Enter the number of C to {} conversions: '.format(letters))))
for letters in bases:
    A.append(int(input('Enter the number of A to {} conversions: '.format(letters))))
for letters in bases:
    G.append(int(input('Enter the number of G to {} conversions: '.format(letters))))

# forms a sort of matrix using the four base lists
b = [T, C, A, G]

# function so calculate S


def transitions(tbl):
    trans = 0
    trans += tbl[0][1]
    trans += tbl[1][0]
    trans += tbl[2][3]
    trans += tbl[3][2]
    tot = sum(tbl)
    s = trans / tot
    return s

# function to calculate V


def transversions(tbl):
    trans = 0
    trans += tbl[0][2]
    trans += tbl[0][3]
    trans += tbl[1][2]
    trans += tbl[1][3]
    trans += tbl[2][0]
    trans += tbl[2][1]
    trans += tbl[3][0]
    trans += tbl[3][1]
    tot = sum(tbl)
    v = trans / tot
    return v

# function to calculate the proportion of S to V


def K(tbl):
    s = transitions(tbl)
    v = transversions(tbl)
    k = ((2 * log(1 - (2 * s) - v)) / (log(1 - (2 * v))) - 1)
    return k
# function to calculate distance of the two sequences


def D(tbl):
    s = transitions(tbl)
    v = transversions(tbl)
    d = ((-.5) * log(1 - (2 * s) - v)) - ((.25) * log(1 - (2 * v)))
    return d


os.system('cls')
print('S = ', round(transitions(b), 4))
print('V = ', round(transversions(b), 4))
print('The distance between the two sequences is approximately: ', round(D(b), 4))
print('There are approximately ', round(K(b), 4),
      ' times more transitions than transversions in the data set')
