import numpy as np
import random as rm
import os
from progressbar import ProgressBar
pbar = ProgressBar()
os.system('cls')
states = ['T', 'C', 'A', 'G']
transitionName = [['TT', 'TC', 'TA', 'TG'], ['CT', 'CC', 'CA', 'CG'],
                  ['AT', 'AC', 'AA', 'AG'], ['GT', 'GC', 'GA', 'GG']]

T = []
C = []
A = []
G = []
transitionMatrix = [T, C, A, G]
lam = 7.3333 * 10 ** -10
years = int(input('Enter the number of years to simulate the site over: '))
its = int(input('Enter the number of iterations to run: '))


for base in states:
    if base == 'T':
        T.append(1 - (3 * lam * years))
    else:
        T.append(lam * years)
for base in states:
    if base == 'C':
        C.append(1 - (3 * lam * years))
    else:
        C.append(lam * years)
for base in states:
    if base == 'A':
        A.append(1 - (3 * lam * years))
    else:
        A.append(lam * years)
for base in states:
    if base == 'G':
        G.append(1 - (3 * lam * years))
    else:
        G.append(lam * years)

startingBase = str(input('Enter the starting base: '))


def basePrediction(steps):
    currentBase = startingBase
    sequence = [currentBase]
    i = 0
    prob = 1
    while i != steps:
        if currentBase == 'T':
            transition = np.random.choice(transitionName[0], replace=True, p=transitionMatrix[0])
            if transition == 'TT':
                sequence.append('T')
            elif transition == 'TC':
                currentBase = 'C'
                sequence.append('C')
            elif transition == 'TA':
                currentBase = 'A'
                sequence.append('A')
            else:
                currentBase = 'G'
                sequence.append('G')
        elif currentBase == 'C':
            transition = np.random.choice(transitionName[1], replace=True, p=transitionMatrix[1])
            if transition == 'CT':
                currentBase = 'T'
                sequence.append('T')
            elif transition == 'CC':
                sequence.append('C')
            elif transition == 'CA':
                currentBase = 'A'
                sequence.append('A')
            else:
                currentBase = 'G'
                sequence.append('G')
        elif currentBase == 'A':
            transition = np.random.choice(transitionName[2], replace=True, p=transitionMatrix[2])
            if transition == 'AT':
                currentBase = 'T'
                sequence.append('T')
            elif transition == 'AC':
                currentBase = 'C'
                sequence.append('C')
            elif transition == 'AA':
                sequence.append('A')
            else:
                currentBase = 'G'
                sequence.append('G')
        elif currentBase == 'G':
            transition = np.random.choice(transitionName[3], replace=True, p=transitionMatrix[3])
            if transition == 'GT':
                currentBase = 'T'
                sequence.append('T')
            elif transition == 'GC':
                currentBase = 'C'
                sequence.append('C')
            elif transition == 'GA':
                currentBase = 'A'
                sequence.append('A')
            else:
                sequence.append('G')
        i += 1

    return sequence


sequenceComp = []
countT = 0
countC = 0
countA = 0
countG = 0

for iterations in pbar(range(0, its)):
    sequenceComp.append(basePrediction(years))


for sequences in sequenceComp:
    if sequences[-1] == 'T':
        countT += 1
    elif sequences[-1] == 'C':
        countC += 1
    elif sequences[-1] == 'A':
        countA += 1
    else:
        countG += 1
percT = (countT / its) * 100
percC = (countC / its) * 100
percA = (countA / its) * 100
percG = (countG / its) * 100

os.system('cls')

print('The probability of starting at base {} and ending at base T is: '.format(startingBase), percT, '%')
print('The probability of starting at base {} and ending at base C is: '.format(startingBase), percC, '%')
print('The probability of starting at base {} and ending at base A is: '.format(startingBase), percA, '%')
print('The probability of starting at base {} and ending at base G is: '.format(startingBase), percG, '%')
