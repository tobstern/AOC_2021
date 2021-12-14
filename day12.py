from time import perf_counter as pfc
from collections import defaultdict
#
d = defaultdict(list)
# get every node as key and its corresponding neighbours
with open('day12.txt', 'r') as txt:
  for l in txt:
    conn = l.strip().split('-')
    d[conn[0]].append(conn[1])
    d[conn[1]].append(conn[0])
#
def visit1(p, node, visited):
  # recursively find paths - and add 'em to res (resulting list)
  res = []
  new_visit = visited + [node]
  if node == 'end':
    return [new_visit]
  for n in p[node]:
    if n != 'start':
      if n not in visited or n.isupper():
        temp_res = visit1(p, n, new_visit)
        res.extend(temp_res)
  return res
#
def visit2(p, node, visited):
  # recursively find paths - and add 'em to res (resulting list)
  res = []
  # next visited node
  new_visit = visited + [node]
  if node == 'end':
    return [new_visit]
  for n in p[node]:
    if n != 'start':
      # uppercase nodes can be visited any time
      if n.isupper():
        temp_res = visit2(p, n, new_visit)
        res.extend(temp_res)
      else:
        # any lowercase node - just one can be visited twice
        l_case = [i for i in new_visit if i.islower()]
        twice = any([True for i in l_case if l_case.count(i) > 1])
        if (twice and new_visit.count(n) < 1) or (not twice and new_visit.count(n) < 2):
          temp_res = visit2(p, n, new_visit)
          res.extend(temp_res)
  return res
#
# Part 1:
start1 = pfc()
print('Part 1 result is:', len(visit1(d, 'start', [])), ', t =', pfc()-start1)
# Part 2:
start2 = pfc()
print('Part 2 result is:', len(visit2(d, 'start', [])), ', t =', pfc()-start2)
