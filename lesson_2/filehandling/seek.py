file = open(
    "/Users/aayamojha/DWIT-TC/data_science_ml/lesson_2/filehandling/files/example.txt"
)
# line = file.readline()
# line2 = file.readline()

# print(line)
# print(line2)

line = file.readline()
file.seek(0, 1)
line2 = file.readline()
print(line)
print(line2)

file.close()
