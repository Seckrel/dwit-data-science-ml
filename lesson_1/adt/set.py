# setA = {1, 2, 3}
# setB = set([2, 3, 4, 4])
# setC = {1, 5, 7}

# print(setC)
# setC.add(9)
# print(setC)

# setC.update([1,4,5,8])
# print(setC)

# print(f"Union:", setA.union(setB))
# print(f"Union using |:", setA | setB)

# print(f"Intersection:", setA.intersection(setB))
# print(f"Intersection using &:", setA & setB)

# print(f"Difference:", setA.difference(setB))
# print(f"Difference using -:", setA-setB)

# print(f"Symmetric Diff:", setA.symmetric_difference(setB))
# print(f"Symmetric Diff using ^:", setA ^ setB)

s = {1,2}
s1 = {1,2,3,4}

print("\nSubset")
print(s.issubset(s1))
print(s1.issubset(s))

print("\nSuperset")
print(s.issuperset(s1))
print(s1.issuperset(s))