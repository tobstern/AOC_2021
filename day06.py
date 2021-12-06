from collections import Counter, defaultdict
fishies = [int(i) for i in open('day06.txt', 'r').read().strip().split(',')]
# Part 1:
def populate(f, lim):
  i = 0
  # use Counter (dictionary) for counting only occurences of each fish type (0-8).
  f = Counter(f)
  while i < lim:
    a = defaultdict(int)
    for l in f:
      if l > 0:
        # decrease fish counter by 1
        a[l-1] += f[l]
      else:
        # fish counter is 0 -> reset its counter to 6 and increase 'new fish' counter (8)
        a[6] += f[l]
        a[8] += f[l]
    f = a
    i += 1
  return sum(f.values())
print('Part 1 result is:', populate(fishies.copy(), 80))
# Part 2:
print('Part 2 result is:', populate(fishies.copy(), 256))
