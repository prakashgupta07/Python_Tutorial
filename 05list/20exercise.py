#count list inside list 
def sublist(l):
    count=0
    for i in l:
        if type(i)==list:
            count+=1
    return  count

num=[1,[1,1],[],[]]
print(sublist(num))