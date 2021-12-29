from time import perf_counter as pfc
from collections import defaultdict as dd
from itertools import product
import numpy as np
#
steps = [
          [
            i[0],
            [
              [int(s.split('..')[0][2:]), int(s.split('..')[1])] for s in i[1].split(',')
            ]
          ]
          for i in [l.split(' ') for l in open('day22.txt', 'r').read().strip().splitlines()]
        ]
#
def gen_pos(s):
  # to get all combinations of the positions:
  return list(product(*[list(range(l[0], l[1]+1)) for l in s]))
#
def reboot(stp):
  f = dd()
  k = 0
  for m, spans in zip([i[0] for i in stp], [i[1] for i in stp]):
    k += 1
    if k > 20:
      continue
    pos = gen_pos(spans)
    for p in pos:
      f.update({tuple(p): 1 if m=='on' else 0})
  return sum(f.values())
#
# Part 1:
start1 = pfc()
print(f'Part 1 result is: {reboot(steps)}, t = {pfc()-start1}')
