'''
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program: hello world! 123
Then, the output should be: LETTERS 10 DIGITS 3
'''
























str_inp = input("Enter a String: ")

num_of_letters = 0
num_of_digit = 0

for i in str_inp:
    if i.isdigit():
        num_of_digit += 1
    else:
        num_of_letters += 1

print(f"LETTERS {num_of_letters} DIGITS {num_of_digit}")
