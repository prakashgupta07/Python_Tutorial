#  list comprehension with nested if 
# example---->[[1,2,3],[1,2,3],[1,2,3]]
nested_list=[[i for i in range(1,4)] for j in range(3)]
print(nested_list) 

# normal method
nested_list=[]
for i in range(3):
    nested_list.append([j for j in range(1,4)])

print(nested_list)
# for i in range(3):
#     for j in range(1,4): 
#         nested_list.append(1)
#         print(nested_list)
