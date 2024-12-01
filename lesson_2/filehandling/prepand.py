with open("myfile.txt", 'r+') as f:
    content = f.read()
    f.seek(0)
    f.write("hello".rstrip('\r\n') + '\n' + content)
    print("Inside with",f)

print(f)