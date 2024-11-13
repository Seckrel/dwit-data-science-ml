str_inp = input("Enter a String: ")
counter = dict()

for i in str_inp:
    if i in counter.keys():
        counter[i] += 1
    else:
        counter[i] = 1


print(counter)


# Better Apporach
from collections import Counter
str_inp = input("Enter a String: ")
counted = Counter(str_inp)
print(counted)
