num = 123215
cached_num = num
rev = 0

while num != 0:
    unit_digit = num % 10
    rev = rev * 10 + unit_digit
    num = num // 10

if cached_num == rev:
    print("palindrom")
else:
    print("not a palindrom")

# # print("Palindrom"
# #       if num == int(str(num)[::-1])
#       else "Not Palindrom")
