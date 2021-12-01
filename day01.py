depths = [int(j) for j in open('day01.txt','r').read().strip().split('\n')]
# Part 1
def compare(depths):
  res = []
  for i,n in enumerate(depths):
    if i != 0 and n > depths[i-1]:
      res.append(1)
    elif i != 0:
      res.append(0)
  return res
#
c = sum(compare(depths))
print('Part 1 result is:', c)
# Part 2
def compare_wins(depths):
  win = 3
  res = []
  for i,m in enumerate(depths):
    nex = sum(depths[i+1:i+win+1])
    prev = sum(depths[i:i+win])
    if i <= len(depths)-win and nex > prev:
      res.append(1)
    else:
      res.append(0)
  return res
#
c2 = sum(compare_wins(depths))
print('Part 2 result is:', c2)
