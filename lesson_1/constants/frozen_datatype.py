from collections import namedtuple

DAYS_OF_WEEK = ('Sun', 'Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat')
print(type(DAYS_OF_WEEK))

PRIME_NUM = frozenset([2,3,5,7])
print(type(PRIME_NUM))

Point = namedtuple('Point', ['x', 'y'])
ORIGIN = Point(1, 1)
print(ORIGIN)


ORIGIN.x = 2 # namedtuple is same as tuple cannot be setF
DAYS_OF_WEEK[1] = 'Jan' # does not run as tuples are immutable
