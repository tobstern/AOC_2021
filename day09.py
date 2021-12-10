from time import perf_counter as pfc
import numpy as np
#
caves = np.array([list(i) for i in open('day09.txt', 'r').read().strip().splitlines()], dtype='int')
#
def find(c):
  lp = {}
  grid = np.ones((len(c) + 2, len(c[0]) + 2), dtype='int') * 10
  grid[1:-1, 1:-1] = c
  for i in range(1,len(grid)-1):
    for j in range(1,len(grid[0])-1):
      # check with 4 adjacents (in the field):
      if grid[i, j] < grid[i-1, j] and grid[i, j] < grid[i+1, j] and grid[i, j] < grid[i, j-1] and grid[i, j] < grid[i, j+1]:
        lp[str(str(i) + ',' + str(j))] = grid[i, j]
  return lp, grid
#
def get_pos(n, grid, num):
  # here we will get each adjacent of the basin, in recursive style.
  p = list(map(int, n.split(',')))
  current = grid[p[0], p[1]]
  up,down,left,right = grid[p[0]-1, p[1]], grid[p[0]+1, p[1]], grid[p[0], p[1]-1], grid[p[0], p[1]+1]
  up_pos,down_pos,left_pos,right_pos = ','.join(map(str, [p[0]-1, p[1]])), \
                                       ','.join(map(str, [p[0]+1, p[1]])), \
                                       ','.join(map(str, [p[0], p[1]-1])), \
                                       ','.join(map(str, [p[0], p[1]+1]))
  # now lets check if we are still in the current basin
  if up < 9 and up_pos not in num.keys():
    num[up_pos] = up
    get_pos(str(str(p[0]-1) + ',' +  str(p[1])), grid, num)
  if down < 9 and down_pos not in num.keys():
    num[down_pos] = down
    get_pos(str(str(p[0]+1) + ',' +  str(p[1])), grid, num)
  if left < 9 and left_pos not in num.keys():
    num[left_pos] = left
    get_pos(str(str(p[0]) + ',' +  str(p[1]-1)), grid, num)
  if right < 9 and right_pos not in num.keys():
    num[right_pos] = right
    get_pos(str(str(p[0]) + ',' +  str(p[1]+1)), grid, num)
  return num.values()
#
def basin(lp, grid):
  pos = []
  # use the lowest point (found in part 1) to find each whole basin
  for i in lp:
    num = {}
    num[i] = lp[i]
    pos.append(get_pos(i, grid, num))
  return np.prod(sorted([len(i) for i in pos])[-3:])
#
# Part 1:
start1 = pfc()
lp, grid = find(caves)
print('Part 1 result is:', np.sum([l + 1 for l in lp.values()]), ', t =', pfc()-start1)
# Part 2:
start2 = pfc()
print('Part 2 result is:', basin(lp, grid), ', t =', pfc()-start2)
