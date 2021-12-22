from time import perf_counter as pfc
from math import sqrt
#
area = [i.split('=')[1].split('..') for i in open('day17.txt', 'r').read().strip()[13:].split(', ')]
area = [[int(i[0]), int(i[1])] for i in area]
#
def move(p, v):
  vx,vy = v[0],v[1]
  p = (p[0] + vx, p[1] + vy)
  if v[0] > 0:
    vx -= 1
  elif vx < 0:
    vx += 1
  else:
    vx = 0
  vy -= 1
  return p, (vx, vy)
#
def hit(p, a):
  if a[0][0] <= p[0] <= a[0][1] and a[1][0] <= p[1] <= a[1][1]:
    return True
  else:
    return False
#
def count(a):
  # brute force like approach:
  vs = set()
  # maxs and mins
  xmin, xmax = a[0][0], a[0][1]
  ymin, ymax = a[1][0], a[1][1]
  # vx_min, vx_max
  vx_min = round(sqrt(2 * xmin + 1/4))
  vx_max = xmax
  # vy_min, vy_max
  vy_min = ymin
  vy_max = -2*ymax
  # loop through all possible velocities in bounds
  for vx in range(vx_min, vx_max+1):
    for vy in range(vy_min, vy_max+1):
      pos = (0,0)
      v0 = (vx, vy)
      p,v = pos, v0
      # move in possible range and add v0, if probe hits area
      while p[0] <= xmax and p[1] >= ymin:
        p, v = move(p, v)
        if hit(p, a):
          vs.add(v0)
          break
  return len(vs)
#
# Part 2:
start2 = pfc()
print(f'Part 2 result is: {count(area)}, t = {pfc()-start2}')
