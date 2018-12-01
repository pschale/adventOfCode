import numpy as np
import time
# Day 1: the first task is to sum a list of integers

fname = 'input_day1.txt'

freq_changes = np.fromfile(fname, sep='\n').astype(int)

print('Solution to part 1: {}'.format(np.sum(freq_changes)))

# next, we find the first time the cumulative sum repeats
# if we get to the end of the list, the list repeats

# this is a pretty dumb way of doing it
start = time.time()

freqs = np.cumsum(freq_changes)

while True:
    if len(np.unique(freqs)) < len(freqs):
        break
    freqs = np.append(freqs, freqs[-1] + freqs)

for i in range(1,len(freqs)):
    if freqs[i] in freqs[:i]:
        solution = freqs[i]
        position = i
        break
else:
    print('No solution found :(')
end = time.time()

print('Solution to part 2: frequency {}, found at {}, in {} seconds'.format(solution, position, end-start))
