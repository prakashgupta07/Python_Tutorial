# filter odd even
# define a function  
# intput 
# list ------- [1,2,3,4,5,6,7,8,9,10]
def odd_even(num):
    odd=[]
    even=[]
    list=[]
    for i in num:
        if i%2==0:
            even.append(i) 
        else:
            odd.append(i)
    list.append(even)
    list.append(odd)
    #output=[even,odd]
    return list

number=list(range(1,11))
print(odd_even(number))
    