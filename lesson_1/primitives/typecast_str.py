str1 = "123"
str2 = "a123"
str3 = "123a"
str4 = "12.3"
str5 = "12.34a"

print(int(str1))

'Broken cause this conversion is not allowed'
# print(int(str2))
# print(int(str3))
# print(int(str4))
# print(int(str5))

print('\nStr to Float')
print(float(str1))
print(float(str4))

print("\nStr to Bool")
str_bool = "False"
print(bool(str))
print(bool("1"))
print(bool("0"))

print("\nInt to Str")
val = 12321
print(str(val))
print(type(str(val)))

print("\nFloat to Str")
val = 1.23
print(str(val))
print(str(1.))
val = 3e4
print(str(val))

print("\nBool to Str")
flag = True
print(str(flag))
print(type(str(flag)))


