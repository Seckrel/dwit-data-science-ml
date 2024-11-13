from functools import reduce

li = range(99)

_sum = reduce(lambda x,y: x+y, li)

print(_sum)
