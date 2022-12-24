# # create a list square of list of 1,10
# square=[]
# for i in range (1,11):
#     square.append(i**2)
# print(square)

# ### in single line
# square2=[i**2 for i in range(1,11)]
# print(square2)

negative=[]
for i in range(1,11):
    negative.append(-i)
print(negative)

negative2=[-i for i in range(1,11)]
print(negative2)

names=['Prakash','Kumar','Gupta']
new_list=[]
for i in names:
    new_list.append(i[0])
print(new_list)
 
list=[i[0] for i in names]
print(list)     