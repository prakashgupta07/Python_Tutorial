# function as argument
def square(l):
        return l**2
li=[1,2,3,4]
#print(list(map(square,li)))

def my_map(func,l):
        my_list=[]
        for i in l:
                my_list.append(func(i))
        return my_list
# print(my_map(square,li))
# #with the help of lambda function
# print(my_map(lambda a:a**3,li))
#with help of list comperhension
def my_map2(func,l):
        return [func(i) for i in l]
print(my_map2(square,li))
