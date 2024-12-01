read_file = open("/Users/aayamojha/DWIT-TC/data_science_ml/lesson_2/filehandling/files/assignment.txt")

while line:=read_file.readline():
    if '+' in line:
        (num1, num2) = (int(i) for i in line.strip().split('+'))
        print(num1+num2)

    elif '-' in line:
        (num1, num2) = (int(i) for i in line.strip().split('-'))
        print(num1 - num2)

    elif '/' in line:
        # (num1, num2) = (int(i) for i in line.strip().split('/'))
        stipped_line = line.strip()
        number_li = stipped_line.split('/')
        num1 = int(number_li[0])
        num2 = int(number_li[1])
        print(num1 / num2)