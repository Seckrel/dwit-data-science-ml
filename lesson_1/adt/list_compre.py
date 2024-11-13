print("Using List Comprehension")
li = [x**2 for x in range(10)]
print(li)

print("For Loop version")
li2 = []
for i in range(10):
    li2.append(i**2)

print(li2)

# list Comprehension with condition

print("\nList Comprenhension with condition")
square_even = [ i**2 for i in range(10) if i%2==0 ]


print("\nList Comprenhension with if...else")
square_of_even = [i**2 if i%2==0 else i for i in range(10)]
print(square_of_even)

