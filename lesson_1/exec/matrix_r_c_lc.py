import pprint

rows = int(input("Enter number of required rows: "))
cols = int(input("Enter number of required columns: "))

# print("\nUsing Nested for loop")
# li = []
# for _ in range(rows):
#     temp_li = []
#     for __ in range(cols):
#         temp_li.append(0)
#     li.append(temp_li)

# print(li)


# print("\nUsing For loop with list creation")
# li = []
# for _ in range(rows):
#     li.append([0] * cols)

# print(li)

print("\nUsing List Comprehension")
li = [[0 for __ in range(cols)] for _ in range(rows)]

pprint.pprint(li, width=22)
