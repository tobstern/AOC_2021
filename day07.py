from time import perf_counter as pfc
from collections import defaultdict
import sys
#
pos = [int(i) for i in open('day07.txt', 'r').read().strip().split(',')]
sys.setrecursionlimit(2*max(pos))
#
def consumed(i):
  # 1+2+3+4+5+6+7+8+9...
  if i <= 1:
    return i
  j = consumed(i-1)
  return i + j
#
def find(pos):
  fuel = defaultdict(int)
  rem = []
  for i in pos:
    for j in pos:
      if i not in rem:
        fuel[i] += abs(j-i)
    rem.append(i)
  return min(fuel.values())
#
def find2(pos):
  fuel = defaultdict(int)
  rem = []
  for i in pos:
    for j in pos:
      if i not in rem:
        fuel[i] += consumed(abs(j-i))
    rem.append(i)
  return min(fuel.values())
# Part 1:
start = pfc()
#print('Part 1 result is:', find(pos), ', t =', pfc()-start)
# Part 2:
print('Part 2 result is:', find2(pos), ', t =', pfc()-start)
