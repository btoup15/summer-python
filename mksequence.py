import numpy as np
import random as rm
import os
from progressbar import ProgressBar
pbar = ProgressBar()
os.system('cls')
states = ['T', 'C', 'A', 'G']
transitionName = [['TT', 'TC', 'TA', 'TG'], ['CT', 'CC', 'CA', 'CG'],
                  ['AT', 'AC', 'AA', 'AG'], ['GT', 'GC', 'GA', 'GG']]

years = int(input('Enter the number of years to simulate the sequence over:'))

T = []
C = []
A = []
G = []
transitionMatrix = [T, C, A, G]
lam = 7.3333 * 10 ** -10

for base in states:
    if base == 'T':
        T.append(1 - (3 * lam))
    else:
        T.append(lam)
for base in states:
    if base == 'C':
        C.append(1 - (3 * lam))
    else:
        C.append(lam)
for base in states:
    if base == 'A':
        A.append(1 - (3 * lam))
    else:
        A.append(lam)
for base in states:
    if base == 'G':
        G.append(1 - (3 * lam))
    else:
        G.append(lam)

testSequence = 'CTTCCAGCCCGCGGACCGATGCTGCCGGCGGCCGCTCGCCCCCTGTGGGGGCCTTGCCTTGGGCTTCGGGCCGCTGCGTTCCGCCTTGCCAGGCGACAGGTGCCATGTGTCTGTGCCGTGCGACATATGAGGAGCAGCGGCCATCAGAGGTGTGAGGCCCTCGCTGGTGCAACGCCCCCAAGGAGTACCCCCCCAAGATACAGCAGCTGGTCCAGGACATACTCTCTTGGAAATCTCAGACCTCAACGAGCTCCTGAAGAAAACGTTGAAGTCGGGCTTGTGCCGATGGGTGGTGTGATGTCTGGGGCTGTCCCTGCTGCGAGGCGGTGGAAGAAGATATCCCCATAGCGAAAGAACGGACACATTTCACACCGAGGCGAAGCCCGTGGACAAAGTGAAGCTGATCAAGGAAATCAAGAAGGCATCAACCTCGTCCAGGCAAAGAAGCTGGTGGAGTCCCTGCCCCAGGAAATGTCGCCAAAGCTGAGGCGGAGAAGATCAAGGCGGCCCTGGAGGCGGTGTGGTTCTGGAGTAGCCTCCAGCTCGGAGGACTTGTGTTCAGGGGTCCTGGGCCCCGGG'
# genbank ascesion #E01991


newSequence = []
for base in pbar(testSequence):
    currentBase = base
    i = 0
    while i != years:
        if currentBase == 'T':
            transition = np.random.choice(transitionName[0], replace=True, p=transitionMatrix[0])
            if transition == 'TT':
                pass
            elif transition == 'TC':
                currentBase = 'C'
            elif transition == 'TA':
                currentBase = 'A'
            else:
                currentBase = 'G'
        elif currentBase == 'C':
            transition = np.random.choice(transitionName[1], replace=True, p=transitionMatrix[1])
            if transition == 'CT':
                currentBase = 'T'
            elif transition == 'CC':
                pass
            elif transition == 'CA':
                currentBase = 'A'
            else:
                currentBase = 'G'
        elif currentBase == 'A':
            transition = np.random.choice(transitionName[2], replace=True, p=transitionMatrix[2])
            if transition == 'AT':
                currentBase = 'T'
            elif transition == 'AC':
                currentBase = 'C'
            elif transition == 'AA':
                pass
            else:
                currentBase = 'G'
        else:
            transition = np.random.choice(transitionName[3], replace=True, p=transitionMatrix[3])
            if transition == 'GT':
                currentBase = 'T'
            elif transition == 'GC':
                currentBase = 'C'
            elif transition == 'GA':
                currentBase = 'A'
            else:
                pass
        i += 1
    newSequence.append(currentBase)
x = sum(i != j for i, j in zip(testSequence, newSequence))
print(x)
print(testSequence)
print(''.join(newSequence))
