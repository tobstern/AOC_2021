from time import perf_counter as pfc
import numpy as np
#
data = [i.splitlines() for i in open('day13.txt', 'r').read().strip().split('\n\n')]
pos = np.array([(int(i.split(',')[1]), int(i.split(',')[0])) for i in data[0]])
inst = [[i.split('=')[0][-1], int(i.split('=')[1])] for i in data[1]]
#
def fold(p, i, part):
  # get dimensions (there occurs a problem with the shape, if I initialize ydim with max()+1)
  ydim, xdim = np.max(p[:, 0]) + 2, np.max(p[:, 1]) + 1
  page = np.zeros((ydim, xdim), dtype='object')
  # save ones at the dot-positions
  p = tuple(map(tuple, p))
  for pos in p:
    page[pos] = 1
  for k,inst in enumerate(i):
    # now go through fold instructions
    c,b = inst[0], inst[1]
    if c == 'y':
      mirrored = np.transpose(np.array([list(reversed(page[b+1:, r])) for r in range(len(page[0,:]))]))
      page = np.logical_or(page[:b, :], mirrored)
    if c == 'x':
      mirrored = np.array([list(reversed(page[l, b+1:])) for l in range(len(page))])
      page = np.logical_or(page[:, :b], mirrored)
    if k == 0 and part == 1:
      # this is the result return for part 1.
      return len(page[page == 1])
  # print to read the 8 letters
  page[page == 1] = '#'
  page[page == 0] = ' '
  print('\nThe Code is:')
  for l in page.tolist():
    print(''.join(l))
#
# Part 1:
start1 = pfc()
print('Part 1 result is:', fold(pos, inst, 1), ', t =', pfc()-start1)
# Part 2:
start2 = pfc()
fold(pos, inst, 2)
print('t =', pfc()-start2)
