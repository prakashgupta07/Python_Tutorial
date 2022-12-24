#define function 
# input
# num,iterable(tuple,list) containg number as args
#example=[1,2,3]
#to_power(3,*nums)
#output list--->[1**3,8,27]
# if you didn't pass any args then it give a user  " hey you didn't pass any args"
#else
# return list 
# use list comperhension 

def to_power(num,*args):
    if args:
        return [i**num for i in args]
    else:
        return "you didn't pass any args"

#print(to_power(2,3,4,5))
nums=[1,2,3]
print(to_power(3,*nums))