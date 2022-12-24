#readfile       
#open function
# read method
#seek method 
#tell method    :- tell the position of cursor
#readline method
#readlines method
# close method
# f=open("file1.txt")#throuth file name
f=open(r"D:\python_tutorials\file1.txt") #open with path
# print(f'cursor position -{f.tell()}')

# print(f.readline(),end="")
# print(f.readline())

# print(f.read())
# print(f'cursor position -{f.tell()}')
# print("before seek method")
# f.seek(30)
# print(f'cursor position -{f.tell()}')

# print("after seek method")
# print(f.read())
# lines=f.readlines()
# print(lines)
# print(len(lines))
# for line in lines:
        # print(line,end='')
print(f.name)
print(f.closed)
f.close()
print(f.closed)
