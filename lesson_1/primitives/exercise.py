# Print a truth table for AND, OR, and XOR operators using padding
print(f"{'X':^1} {'Y':^1}\t{'R(&)':^5} {'R(or)':^5} {'R(xor)':^5}") 
print(f"{'T':^1} {'T':^1}\t{True and True:^5} {True or True:^5} {True ^ True:^5}")
print(f"{'T':^1} {'F':^1}\t{True and False:^5} {True or False:^5} {True ^ False:^5}")
print(f"{'F':^1} {'T':^1}\t{False and True:^5} {False or True:^5} {False ^ True:^5}")
print(f"{'F':^1} {'F':^1}\t{False and False:^5} {False or False:^5} {False ^ False:^5}")

