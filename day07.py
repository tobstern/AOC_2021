from time import perf_counter as pfc
from collections import defaultdict
#
pos = [int(i) for i in open('day07.txt', 'r').read().strip().split(',')]
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
        fuel[i] += int(abs(j-i) * (abs(j-i) + 1) / 2)
    rem.append(i)
  return min(fuel.values())
# Part 1:
start1 = pfc()
print('Part 1 result is:', find(pos), ', t =', pfc()-start1)
# Part 2:
start2 = pfc()
print('Part 2 result is:', find2(pos), ', t =', pfc()-start2)
