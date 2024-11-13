import sys

bool1 = True
bool2 = False

print(bool1, bool2)
print(type(bool2))

print(sys.getsizeof(bool1))
print(sys.getsizeof(bool2))

print(bool(bool1))
print(bool(bool2))

x = 0
print("0", bool(x))

x = []
print("[]", bool(x))

x = set()
print("set", bool(x))

y = 1
print("1", bool(y))

y = [1,2]
print("[1,2]", bool(y))

y = {'a': 1}
print("{a: 1}",bool(y))