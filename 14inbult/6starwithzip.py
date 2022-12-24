# * args with zip
l=[(1,2),(3,4),(5,6),(7,8)]
# l convert with two list---l1=[1,3,5,7],l2=[2,4,6,8]  
print(list(zip(*l)))# it convert two tuple in alist[(1, 3, 5, 7), (2, 4, 6, 8)]
l1,l2=list(zip(*l))
print(l1)# it's give tuple value(1, 3, 5, 7)
print(list(l1))
print(l2)# it's give tuple value (2, 4, 6, 8)
print(list(l2)) 
new_list=[]
for i in zip(l1,l2):
        new_list.append(max(i))
print(new_list)