import numpy as np
bs = np.array([list(i) for i in open('day03.txt','r').read().strip().split('\n')], dtype='int')
def b2d(b):
  return sum([n * 2**i for i,n in enumerate(b[::-1])])
# Part 1
gr = [1 if sum(bs[:, i]) > len(bs[:, i])/2 else 0 for i in range(len(bs[0,:]))]
er = [2**i % 2 for i in gr]
print('Part 1 result is:', b2d(gr)*b2d(er))
# Part 2
def filt(bits, j, mode):
  if len(bits[:, j]) > 1:
    if mode == 'oxy' :
      bs = 1 if sum(bits[:, j]) >= len(bits[:, j])/2 else 0
    if mode == 'co2':
      bs = 0 if len(bits[:, j]) - 2*sum(bits[:, j]) <= 0 else 1
    bits = np.array([b for b in bits if b[j] == bs])
  if bits.shape[0] < 2:
    return list(bits[0])
  j += 1
  bits = filt(bits, j, mode)
  return bits
print('Part 2 result is:', b2d(filt(bs.copy(), 0, 'oxy')) * b2d(filt(bs.copy(), 0, 'co2')))
