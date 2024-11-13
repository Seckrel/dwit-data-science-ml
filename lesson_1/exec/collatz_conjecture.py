def collatz_formula(num):
    is_even = num % 2 == 0
    return num // 2 if is_even else 3 * num + 1

starting_number = int(input("Starting point for collatz conjecture: "))
n = int(input("How many hailstone seriers: "))


for i in range(n):
    print(starting_number)
    starting_number = collatz_formula(starting_number)



    

