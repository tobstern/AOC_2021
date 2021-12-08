from time import perf_counter as pfc
#
disp = [[i.split(' | ')[0].split(), i.split(' | ')[1].split()] for i in open('day08.txt', 'r').read().strip().split('\n')]
#
#easy_nums = ['cf', 'bcdf', 'acf', 'abcdefg']           # 1,4,7,8 are unique number of segments - their lengths are 2,4,3,7
easy_nums = [2,4,3,7]
def easy_digis(d, e_n):
  e = 0
  for i in d:
    for j in i[1]:
      if len(j) in e_n:
        e += 1
  return e
#
def get_digit(i, nums):
  return [str(pos) for pos,k in enumerate(nums) if ''.join(i) ==  ''.join(sorted(list(k)))][0]
#
def p2(d, e_n):
  res = []
  for i in d:
    for j in i[0]:
      j = frozenset(j)
      if len(j) == 2:
        one = j
      if len(j) == 4:
        four = j
      if len(j) == 3:
        seven = j
      if len(j) == 7:
        eight = j
    for j in i[0]:
      j = frozenset(j)
      if len(j) == 5:
        # 2,3,5
        if len(j - one) == 3:
          three = j
        if len(j - (four - one)) == 3:
          five = j
        if len(j - (eight - (four | seven))) == 3:
          two = j
      if len(j) == 6:
        # 0,6,9
        if len(j - one) == 5:
          six = j
        if len(j - four) == 2:
          nine = j
        if len(j - (four - one)) == 5:
            zero = j
    #
    nums = [zero,one,two,three,four,five,six,seven,eight,nine]
    temp = []
    for k in i[1]:
      j = sorted(k)
      temp.append(get_digit(j, nums))
    res.append(int(''.join(temp)))
  return sum(res)
#
# Part 1:
start1 = pfc()
print('Part 1 result is:', easy_digis(disp, easy_nums), ', t =', pfc()-start1)
# Part 2:
start2 = pfc()
print('Part 2 result is:', p2(disp, easy_nums), ', t =', pfc()-start2)
