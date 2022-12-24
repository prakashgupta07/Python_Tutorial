# common elements finder function 
#define a function which takes  2 list as input and return a list 
#which contain common elemtnt  of both list 
def common_list(a,b):
    li=[]
    for i in a:
        if i in b:
            li.append(i)
    return li

number=[1,5,7,6,3]
number2=[1,5,7,6,3,9] 
print(common_list(number,number2))

    
