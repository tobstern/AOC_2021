from time import perf_counter as pfc
#
start = [int(i[-1]) for i in open('day21.txt', 'r').read().strip().split('\n')]
#
def roll(d, c):
  d += 1
  c += 1
  d = d % 100 if d % 100 != 0 else 100
  return d, c
#
def move(p, t):
  p += t
  #print(p)
  p = p % 10 if p % 10 != 0 else 10
  #print(p)
  return p
#
def play(start):
  sc = [0, 0]
  pos = start
  # player 1 starts
  die = 0
  count = 0
  while True:
    win = False
    #print(count)
    # roll dice 3x, each turn - circular fields 10 to 1, and die 100 to 1
    # 2 player
    for i in range(2):
      # 3 turns each
      temp = 0
      for _ in range(3):
        die, count = roll(die, count)
        temp += die
      pos[i] = move(pos[i], temp)
      sc[i] += pos[i]
      if sc[0] >= 1000:
        res = count * sc[1]
        win = True
        break
      if sc[1] >= 1000:
        res = count * sc[0]
        win = True
        break
    if win:
      break
  return res
#
# Part 1:
start1 = pfc()
print(f'Part 1 result is: {play(start)}, t = {pfc()-start1}')
