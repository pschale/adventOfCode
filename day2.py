import numpy as np
from collections import Counter

fname = 'input_day2.txt'

ids = open(fname).read().split('\n')
ids = ids[:-1]

def has_num(s, j):
    counted = Counter(s)
    counts = [counted[ele] for ele in s]
    if j in counts:
        return 1
    else:
        return 0

num_with_2 = sum([has_num(ele, 2) for ele in ids])
num_with_3 = sum([has_num(ele, 3) for ele in ids])

print('solution to part 1: {}'.format(num_with_2*num_with_3))

def comp_strs(a, b):
    count = 0
    for i in range(26):
        if not a[i] == b[i]:
            place = i
            count += 1
        if count > 1:
            return [False, 0]
    else:
        if count == 1:
            return [True, place]
        print('this broke :(')

for j in range(len(ids)):
    for k in range(j+1, len(ids)):
        comp = comp_strs(ids[j], ids[k])
        if comp[0]:
            print('solution to part 2: {}'.format(ids[j][:comp[1]] + ids[j][comp[1] + 1:]))
            exit()

