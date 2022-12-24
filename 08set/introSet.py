#set data type 
# unordered collection of unique tiems 
# you can't store list,dictionary,tuple  in set

s={1,2,3}#repeatation of element are not print
# print(s)#{1, 2, 3, 4} output
# print(s[1])# are not allow int set because of unordered collection of items

# l=[1,2,3,4,2,1,3,2,4,45,56,6,7,5,4,11]
# # remove dublicate 
# s2=set(l)# convert list into set 
# s2=list(set(l))# convert set into list
# print(s2)

# add element in set
# s.add(4)
# s.add(5)
# print(s)

# remove element
# s.remove(3)
#s.remove(4)# if element are not present in the set it give error
#s.discard(3)
#s.discard(4)# if element are not present in the set it will not give error
#print(s)

#  clear method 
# s.clear()
# print(s)

###copy method 
s1=s.copy()
print(s1)