from time import perf_counter as pfc
import numpy as np
#
grid = np.array([list(i) for i in open('day25.txt', 'r').read().strip().splitlines()])
#
def move(g):
  k = 0
  next_g = g.copy()
  while True:
    k += 1
    for i in range(len(g)-1, -1, -1):
      for j in range(len(g[0, :])-1, -1, -1):
        if g[i, j] != '>':
          continue
        # wrap around if exceeding
        e,s,w = (j+1) % len(g[0, :]), (i+1) % len(g), \
                (j-1) if j-1 >= 0 else len(g[0, :])-1
        # estern moving
        # check for right neighbour
        if g[i, j] == '>' and g[i, e] == '.':
          next_g[i, e] = '>'
          next_g[i, j] = '.'
    # save eastern moves
    g = next_g.copy()
    for i in range(len(g)-1, -1, -1):
      for j in range(len(g[0, :])-1, -1, -1):
        if g[i, j] != 'v':
          continue
        # wrap around if exceeding
        e,s,w = (j+1) % len(g[0, :]), (i+1) % len(g), \
                (j-1) if j-1 >= 0 else len(g[0, :])-1
        # southern moving
        # check for downward neighbour
        if g[i, j] == 'v' and g[s, j] == '.':
          next_g[i, j] = '.'
          next_g[s, j] = 'v'
    # test if grid has changed - if not break.
    if np.all(g == next_g):
      break
    g = next_g.copy()
  return k
#
# Part 1:
start1 = pfc()
print(f'Part 1 result is: {move(grid)}, t = {pfc()-start1}')
