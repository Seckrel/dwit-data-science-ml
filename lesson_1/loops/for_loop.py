word = "Python"

# for letter in word: # it calls next function in word
#     print(letter)

# print("final")
import time

start = time.time()
sum = 0
for i in range(0, 100_000_000,2):
    sum = sum + i

print("TIme taken", time.time() - start)

start = time.time()
sum = 0
for i in range(0, 100_000_000,):
    if i % 2 == 0:
        sum = sum + i

print("TIme taken", time.time() - start)


# range_to_15 = range(15) # last number is not included
# print(type(range_to_15))
# print(list(range_to_15))

# range_to_15 = range(5, 15)
# print(range_to_15)
# print(list(range_to_15))

# range_to_15 = range(5, 15, 5)
# print(range_to_15)
# print(list(range_to_15))

# for i in range(15): 
#     print(i)