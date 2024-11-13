pattern = "*****"
n = len(pattern)

for i in range(n):
    print(f"{pattern[:i+1]}")

print()
temp = ''
for i in range(n):
    # print(f"{pattern[:i+1].rjust(5, ' ')}")
    print(f"{temp:*>{n-i}}")

print()
for i in range(0, n, 2):
    print(f"{pattern[:i+1]:^{n}}")

