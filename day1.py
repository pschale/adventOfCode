import numpy as np

# Day 1: the first task is to sum a list of integers

fname = 'input_day1.txt'

freq_changes = np.fromfile(fname, sep='\n').astype(int)

print('Solution to part 1: {}'.format(np.sum(freq_changes)))

# next, we find the first time the cumulative sum repeats
# if we get to the end of the list, the list repeats

# this is a pretty dumb way of doing it

f = freq_changes.copy()
while True:
    freqs = np.cumsum(f)
    if len(np.unique(freqs)) < len(freqs):
        break

    f = np.append(f, freq_changes)

for i in range(1,len(freqs)):
    if freqs[i] in freqs[:i]:
        solution = freqs[i]
        position = i
        break
else:
    print('No solution found :(')

print('Solution to part 2: frequency {}, found at {}'.format(solution, position))
