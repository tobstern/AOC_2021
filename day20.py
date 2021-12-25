from time import perf_counter as pfc
from collections import defaultdict
from copy import deepcopy as dp
import numpy as np
from math import sqrt
#
i = [list(s) for i in open('day20.txt', 'r').read().strip().split('\n\n') for s in i.split('\n')]
alg, image = dict(), dict()
[alg.update({k: 1}) if v == '#' else alg.update({k: 0}) for k,v in enumerate(i.pop(0))]
[
  image.update({(k1, k2): 1}) if v == '#' else image.update({(k1, k2): 0})
  for k1,l in enumerate(i)
  for k2,v in enumerate(l)
]
#
def b2d(b):
  # binary to decimal conversion
  return sum([n * 2**i for i,n in enumerate(b[::-1])])
#
def proc(out_image, alg, lim):
  t = 0
  while t < lim:
    out_image = defaultdict(lambda: 1 if t%2==1 else 0, out_image)
    image = dp(out_image)
    for r in range(-t-1, 101+t):
      for c in range(-t-1, 101+t):
        out_image[(r, c)] = alg[
                                b2d(
                                    [image[(ro, co)] for ro in range(r-1, r+2) for co in range(c-1, c+2)]
                                   )
                                ]
    t += 1
  return sum(out_image.values())
#
# Part 1:
start1 = pfc()
print(f'Part 1 result is: {proc(image, alg, 2)}, t = {pfc()-start1}')
# Part 2:
start2 = pfc()
print(f'Part 2 result is: {proc(image, alg, 50)}, t = {pfc()-start2}')
