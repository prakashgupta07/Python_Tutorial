#map function
numbers=[1,2,3,4]
def square(a):
    return a**2
# squares=list(map(square,numbers))
# # same things with the help of lambda function
# squqres1=list(map(lambda a:a**2,numbers))
# print(squqres1)
# print(squares)
# # same things with the help of list comperhension
# print([a**2 for a in numbers])

new_list=[]
for num in numbers:
    new_list.append(square(num))

print(new_list)

names=["abc","abcd","abcde"]
length=map(len,names)
for i in length:
    print(i)
##through map function you can iterate only one time
# if you want to iterate map function again and again then you convert into list

