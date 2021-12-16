from time import perf_counter as pfc
import numpy as np
from scipy.signal import convolve2d
#
grid = np.array([list(i) for i in open('day11.txt', 'r').read().strip().splitlines()], dtype='int')
#
def flash_count1(g, lim):
  c = []
  while lim > 0:
    # my first approach was by position finding and recursion...
    # with some help and inspiration.
    # done by convolution of the mask - all neighbouring octopi and the octopi to be flashed in
    # flashing (is Truth array).
    mask = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    flashed = np.zeros(grid.shape, dtype='bool')
    g += 1
    while np.any(flashing := g > 9):
      flashed |= flashing
      g += convolve2d(flashing, mask, mode='same')
      g[flashed] = 0
    # and finally append the sum of flashed octopi to a list
    c += [flashed.sum()]
    lim -= 1
  return sum(c)
#
def flash_count2(g):
  c = []
  lim = 0
  # just use same function, but counting up to the point....
  while True:
    mask = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    flashed = np.zeros(grid.shape, dtype='bool')
    g += 1
    while np.any(flashing := g > 9):
      flashed |= flashing
      g += convolve2d(flashing, mask, mode='same')
      g[flashed] = 0
    c += [flashed.sum()]
    lim += 1
    # ...where all octopi are flashing and g has just zeros.
    if np.all(g == 0):
      step = lim
      return step
#
# Part 1:
start1 = pfc()
print('Part 1 result is:', flash_count1(grid.copy(), 100), ', t =', pfc()-start1)
# Part 2:
start2 = pfc()
print('Part 2 result is:', flash_count2(grid), ', t =', pfc()-start2)
