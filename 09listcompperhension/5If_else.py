#list comprehension with if else 
nums=list(range(1,11))
new_list=[]
for i in nums:
    if i%2==0:
        new_list.append(i*2)
    else:
        new_list.append(-i)
print(new_list)

# list comprehension 
new_list2=[i*2 if i%2==0 else -i for i in nums]
print(new_list2) 