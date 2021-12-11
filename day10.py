from time import perf_counter as pfc
#
chunks = [i for i in open('day10.txt', 'r').read().strip().splitlines()]
#
def check_syntax(ch):
  d = {'(': ')', '[': ']', '{': '}', '<': '>'}
  points = {')': 3, ']': 57, '}': 1197, '>': 25137}
  incom = []
  invalid = []
  invalid_pos = []
  # fill up stack, and check if next is closing bracket, if so, pop() (remove from top)
  for j,c in enumerate(ch):
    stack = []
    for i,b in enumerate(c):
      if b not in d.values():
        stack.append(b)
      elif b in d.values():
        if b == d[stack[-1]]:
          stack.pop()
        else:
          # found invalid closing bracket
          invalid.append(b)
          invalid_pos.append(j)
          break
    incom.append(stack)
  return sum([points[i] for i in invalid]), invalid_pos, incom

#
def score_of_incomplete(ch, inv_pos, sts):
  points = {'(': 1, '[': 2, '{': 3, '<': 4}
  score = []
  for i,char in enumerate(sts):
    # ignore all invalid positions
    if i not in inv_pos:
      sc = 0
      # calculate point score of the stacks, found in part 1.
      for c in range(len(char)-1, -1, -1):
        s = char[c]
        sc *= 5
        sc += points[s]
      score.append(sc)
  return sorted(score)[int(len(score)/2)]
#
# Part 1:
start1 = pfc()
score1, inv_pos, stacks = check_syntax(chunks)
print('Part 1 result is:', score1, ', t =', pfc()-start1)
# Part 2:
start2 = pfc()
print('Part 2 result is:', score_of_incomplete(chunks, inv_pos, stacks), ', t =', pfc()-start2)
