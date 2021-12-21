from time import perf_counter as pfc
import numpy as np
#
message_hex = list(open('day16.txt', 'r').read().strip())
#
def b2d(b):
  # binary to decimal conversion
  return sum([n * 2**i for i,n in enumerate(b[::-1])])
#
def hex2bin(hexa):
  # dictionary for hex to bin conversion
  lookup = {
  '0' : [0,0,0,0],
  '1' : [0,0,0,1],
  '2' : [0,0,1,0],
  '3' : [0,0,1,1],
  '4' : [0,1,0,0],
  '5' : [0,1,0,1],
  '6' : [0,1,1,0],
  '7' : [0,1,1,1],
  '8' : [1,0,0,0],
  '9' : [1,0,0,1],
  'A' : [1,0,1,0],
  'B' : [1,0,1,1],
  'C' : [1,1,0,0],
  'D' : [1,1,0,1],
  'E' : [1,1,1,0],
  'F' : [1,1,1,1]
  }
  bi = []
  for s in hexa:
    bi += [lookup[s]]
  return bi
#
def literal(b):
  bGroup = b[6:]
  bi_res = []
  for i,digi in enumerate(bGroup):
    if i % 5 == 0:
      if digi == 0:
        bi_res += bGroup[i+1:i + 5]
        b = bGroup[i:]
        break
      elif digi == 1:
        bi_res += bGroup[i+1:i + 5]
      # ignore trailing zeros - important?, we'll see...
  le = 6 + len(bi_res) + int(len(bi_res) / 4)
  return le, bi_res
#
def parse(b):
  # sum of versions (V) for part 1.
  V = b2d(b[:3])
  T = b2d(b[3:6])
  versum = V
  if T == 4:
    l, r = literal(b)
    le = l
    res = b2d(r)
  else:
    sub_res = []
    # now it is an operator packet
    # same header
    # determine mode (0|1):
    if b[6] == 0:
      # length of bits of following sub-packets
      sub_le = 22
      le = sub_le + b2d(b[7:22])
      while sub_le < le:
                l, v, r = parse(b[sub_le:le])
                sub_le += l
                versum += v
                sub_res.append(r)
    else:
      # number of following sub-packets
      le = 18
      numb = b2d(b[7:18])
      for i in range(numb):
                l, v, r = parse(b[le:])
                le += l
                versum += v
                sub_res.append(r)
  # part 2 additional calculations:
    match T:
      case 0:
        res = sum(sub_res)
      case 1:
        res = np.prod(sub_res)
      case 2:
        res = min(sub_res)
      case 3:
        res = max(sub_res)
      case 5:
        res = 1 if sub_res[0] > sub_res[1] else 0
      case 6:
        res = 1 if sub_res[0] < sub_res[1] else 0
      case 7:
        res = 1 if sub_res[0] == sub_res[1] else 0
  return le, versum, res
#
def main(m_hex):
  b = sum(hex2bin(m_hex), [])
  return parse(b)
#
# Part 1:
start1 = pfc()
res = main(message_hex)
print('Part 1 result is:', res[1], ', t =', pfc()-start1)
# Part 2:
start2 = pfc()
print('Part 2 result is:', res[2], ', t =', pfc()-start2)
