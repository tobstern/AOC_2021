import numpy as np
vents = [[i.split(' -> ')[0].split(','), i.split(' -> ')[1].split(',')] for i in open('day05.txt','r').read().strip().split('\n')]
v = np.array(vents, dtype='int')
# Part 1:
def scan(v, part):
  grid = np.array([[0] * (max(max(v[:, 0, 1]), max(v[:, 1, 1])) + 3)] * (max(max(v[:, 0, 0]), max(v[:, 1, 0])) + 3))
  for l in v:
    x,y = l[:, 0], l[:, 1]
    if x[0] == x[1]:
    # for vertical lines from part 1
      ys = sorted(y.copy())
      grid[ys[0]:ys[1] + 1, x[0]] += 1
    elif y[0] == y[1]:
      # for horizontal lines from part 1
      xs = sorted(x.copy())
      grid[y[0], xs[0]:xs[1] + 1] += 1
    elif part == 2:
      # for the diagonal lines from part 2
      pos_y = range(y[0], y[1]-1, -1) if y[0] > y[1] else range(y[0], y[1] + 1)
      pos_x = range(x[0], x[1]-1, -1) if x[0] > x[1] else range(x[0], x[1] + 1)
      for i,j in zip(pos_y, pos_x):
        grid[i,j] += 1
  return sum([1 for row in grid for col in row if col > 1])
print('Part 1 result is:', scan(v, 1))
# Part 2:
print('Part 2 result is:', scan(v, 2))
