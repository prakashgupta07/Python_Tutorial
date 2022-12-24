## filter function

def Is_even(a):
    return a%2==0
numbers=[1,2,3,4,5,6,7,8,9]
even=tuple(filter(Is_even,numbers))
even1=tuple(filter(lambda a:a%2==0,numbers))
print(even1)
print(even)
for i in even:
    print(i)

new_even=[i for i in numbers if i%2==0]
print(new_even)