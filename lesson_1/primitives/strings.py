single_q = 'Hello World'
double_q = "Hello World2"
multiline_sq = '''Hello
World'''
multiline_dq = """Hello
Wwrold"""

"""Indexing"""
# print()
# print("Indexing")
# print(single_q[0])
# print(single_q[-1])

# print(ord('a'))
# print(chr(97))



# """Contact String"""
# print('\nConcat')
# first = "Hello"
# last = "World"
# first_last = first + last
# print(first_last)
# first_last = first + " " + last
# print(first_last)
# print(first, last)  # auto adds space inplace of comma

# """String Methods"""
print("\nString Methods")
word = "    Hello World    "
word2 = "hello world"
print("lower:", word.lower())
print("upper:", word2.upper())
print("capitalize:", word2.capitalize())
print("swapcase:", "hElLo wOrlD".swapcase())
print("length:", len(word))
print("length:", len(word2))
print("2strip:", word.strip())
print("replace:", word.replace(' ', '-'))

print("chaining methods", word.strip().upper().replace(" ", "-"))
print("Hello world".split())
print("hello,world, class".split(','))

print("title:", word2.title())


# """String Formatting"""
# print("\nString Formatting")
# value = 12
# old_style_template = "Value of number is %d" %value
# print(old_style_template)

# name = "Deerwalk"
# age = 15
# str_format_template = "Name: {} | age: {}"
# print(str_format_template.format(name, age))

# # Literal String Interpolation. F literal
# name = "Jack"
# area_of_circle = 3.14 * 3
# f_template = f"Area of Circle is {area_of_circle} calculate by {name}"
# print(f_template)

# # Formatting option
# radius = 3.3234
# area_of_circle = 3.14 * radius
# print(f"Area of Circle with {radius} is {area_of_circle:.3f}")

# val = 42
# print(f"Start{val}End")
# print(f"Start{val:>5}End")
# print(f"Start{val:<5}End")
# print(f"Start{val:^5}End")
# print(f"S{val:0>4}E")
# print(f"S{val:0<4}E")
# print(f"decimal: {val:d} | hex: {val:x} | ocatal: {val:o} | binary: {val:b}")

# large_number = 10000000
# print(f"{large_number:,}")


# # """
# # Multi Line
# # Comment
# # """
# # print(single_q)
# # print(double_q)
# # print()
# # print(multiline_sq)
# # print()
# # print(multiline_dq)

