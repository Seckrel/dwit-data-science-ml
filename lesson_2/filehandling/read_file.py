file = open(
    "/Users/aayamojha/DWIT-TC/data_science_ml/lesson_2/filehandling/files/example.txt"
)

print(file)
print("is file close", file.closed)

# data = file.readline()
# data = file.read()
data = file.readlines()
print(data)

file.close()

print(file.closed)
