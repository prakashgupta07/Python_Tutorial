#iterator vs iterable
number=[1,2,3,4]
square=map(lambda a:a**2,number)
# for i in number:
    # print(i)

# step call iter function
#iter(number)---->iterator
# next(iter(number))
next_numbwer=iter(number)
print(next(next_numbwer))
print(next(next_numbwer))
print(next(next_numbwer))
print(next(next_numbwer))

print(iter(number))