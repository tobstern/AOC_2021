from time import perf_counter as pfc
from collections import defaultdict, Counter
#
data = [i.split('\n') for i in open('day14.txt', 'r').read().strip().split('\n\n')]
# initial sequence
seq = data[0][0]
# initial pairs
pairs = Counter([seq[i:i+2] for i in range(len(seq)-1)])
# build dictionary with rules
d = defaultdict(str)
#
for k in data[1]:
  a = k.split(' -> ')
  d[a[0]] = a[1]
#
def insert1(seq, d, lim):
  # for part 1, building the string
  while lim > 0:
    new_seq = ''
    for i in range(len(seq)-1):
      new_seq += seq[i] + d[seq[i:i+2]]
    new_seq += seq[-1]
    seq = new_seq
    lim -= 1
  count = Counter(new_seq)
  return max(count.values()) - min(count.values())
#
def insert2(pairs, seq, d, lim):
  # for part 2, counting occurences of pairs
  c = Counter(seq)
  while lim > 0:
    new_pairs = Counter()
    # add the new pairs - after inserting the Letter by the rules in d, two new pairs are added.
    for k,f in pairs.items():
      new_pairs[k[0] + d[k]] += f
      new_pairs[d[k] + k[1]] += f
      # adding the count of the current pair to the newly inserted Letter by the rules (d[k]).
      c[d[k]] += f
    pairs = new_pairs
    lim -= 1
  return max(c.values()) - min(c.values())
#
# Part 1:
start1 = pfc()
print('Part 1 result is:', insert1(seq, d, 10), ', t =', pfc()-start1)
# Part 2:
start2 = pfc()
print('Part 2 result is:', insert2(pairs, seq, d, 40), ', t =', pfc()-start2)
