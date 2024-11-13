li = [1,2,3,4,5,6,7,8,9]
print(li[2:6])
print(li[:4])
print(li[4:])

print("\n[1:8:2]")
print(li[1:8:2])

print("\n[-4:]")
print(li[-4:])

print("\n[-6:-2]")
print(li[-6:-2]) # index -2 is excluded

print("\nReverse")
print(li[::-1])

print("\n[8:4:-1]")
print(li[8:4:-1]) # reverses list starting at 8 to 4th index (excluding 4th index)

print("\n[::2]")
print(li[::2]) # starts at 0 to end of list every 2 item in list

print("\nCreate shallow copy using slice")
print(li[:])
