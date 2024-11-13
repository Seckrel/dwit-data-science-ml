di = {"a": 1, 
      "b": 2, 
      "c": "hello", 
      2: "world"}

print(di["a"])

di[2] = "bye"
print(di[2])

di[-1] = 8

print(di.items())



# try:
#     print(di['z'])
# except KeyError as e:
#     print(e)

# di['a'] = 123
# print(di)

# di.update({'a': 1, 'b': 22})
# print(di)

# print('\nPop')
# val = di.pop('a')
# print(val)
# print(di)

# print('\nPopItem')
# new_di = di.popitem()
# print(new_di)
# print(di)

# print('\nDel')
# del di['b']
# print(di)

# print('\nClear')
# di.clear()
# print(di)

# print('\nDict Comprehension')

# di = {k:k**2 for k in range(1, 12)}
# print(di)

# di = {i:i**2 for i in range(1, 12) if i % 2 == 0}
# print(di)

# print('\nNested')
# di = {
#     'person1': {'name': "Jack", 'age': 22},
#     'person2': {'name': "Mary", 'age': 25}
# }

# print(di)
# print(di['person1'])
# print(di['person1']['name'])

# di['person1']['name'] = "Harry"
# print(di)

# di['person2'] = "New item"
# print(di)
