from time import perf_counter as pfc
#
area = [i.split('=')[1].split('..') for i in open('day17.txt', 'r').read().strip()[13:].split(', ')]
area = [[int(i[0]), int(i[1])] for i in area]
print(area)
#
def throw(a):
  t = -1e9
  for i in range(a[1][0], 200):
    l = set()
    y = 0
    while True:
      y += i
      i -= 1
      l.add(y)
      if a[1][0] <= y <= a[1][1]:
        t = max(t, max(l))
        break
      if y < a[1][0]:
        break
  return t
#
# Part 1:
start1 = pfc()
print(f'Part 1 result is: {throw(area)}, t = {pfc()-start1}')
