import numpy as np
inst = list([i.split(' ')[0], int(i.split(' ')[1])] for i in open('day02.txt','r').read().strip().split('\n'))
# Part 1
d = sum([i[1] if i[0] == 'down' else -i[1] if i[0] == 'up' else 0 for i in inst])
f = sum([i[1] for i in inst if i[0] == 'forward'])
print('Part 1 result is:', d*f)
# Part 2
inst = np.array(inst)
d,aim,h = 0,0,0
for n,i in zip(inst[:, 0], inst[:, 1]):
  if n == 'down':
    aim += int(i)
  elif n == 'up':
    aim -= int(i)
  if n == 'forward':
    h += int(i)
    d += aim * int(i)
print('Part 2 result is:', d*h)
