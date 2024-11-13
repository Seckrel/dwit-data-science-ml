li = [1,2,3]
print(li[0]) # list starts at 0th index
print(li[-1]) # last item of the list
print(li[-2]) # second to last item

# change value
print("\nBefore", li)
li[1] = 11
print("After", li)
print()

# del 
print("\nBefore", li)
del li[1]
print("After", li)
print()

# del 
li = [1,2,3,4,3]
print("\nBefore", li)
li.remove(3) # removes first occurence of 3 from left to right
print("After", li)
print()

# pop at last
li = [1,2,3,4,3]
print("\nBefore", li)
default_pop = li.pop()
print("After", li)
print("Popped item", default_pop)

# pop at idex
li = [1,2,3,4,3]
print("\nBefore", li)
pop_at_3 = li.pop(3)
print("After", li)
print("Popped item", pop_at_3)
print()

# insert item
li = [1,2,3,4,5]
print("\nBefore", li)
li.insert(3, "apple")
print("After", li)

# list sort
li = [51, 1, 97, 11, 3, 2, 1, 1, 7, 8]
print("\nBefore", li)
li_sorted_asc = sorted(li)
print("Sorted Function", li_sorted_asc)
li_sorted_desc = sorted(li, reverse=True)
print("Sorted Function Desc", li_sorted_desc)

# list sort in-place
li = [51, 1, 97, 11, 3, 2, 1, 1, 7, 8]
print("\nBefore", li)
li.sort()
print("Sorted Function", li_sorted_asc)
li.sort(reverse=True)
print("Sorted Function Desc", li_sorted_desc)

# reverse 
li = [11, 98, 5, -2, 3.1]
print("\nBefore", li)
li.reverse()
print("Reversed", li)

# join
li = ["Hello", "Mr.", "Jackson"]
print("\nJoin")
print(" ".join(li))
print(",".join(li))