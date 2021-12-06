import numpy as np
fishies = [int(i) for i in open('day06.txt', 'r').read().strip().split(',')]
# Part 1 solved with numpy, but too slow -> exponetial increase of list -> instead count occurences
# of every fishtype (0-8), e.g. with a dictionary...:
def populate(f, lim):
  i = 0
  while i < lim:
    f = f - np.ones((len(f)), dtype='int')
    l = len(f[f == -1])
    f = np.concatenate((f[f > -1], [6,8] * l))
    i += 1
  return len(f)
print('Part 1 result is:', populate(np.array(fishies.copy()), 80))
