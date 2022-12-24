# we use enumerate function with for loop to tract position of our 
# itms in iterable
#  how we can do this without enumerate function 
names=['abc','abcdef','prak'] 
#o--'abc'
#1---'abcdef'
################  with the help of for loop##################
# pos=0
# for name in names:
#     print(f"{pos}---->{name}")
#     pos+=1

########### with the help of enumerate function################
for position,name in enumerate(names):
    print(f"{position}---->{name}")

#define a function that take two arguments
# 1.)list containg string
# 2.) string that want to find in your list 
# and this function will return the index of string in your list and 
#if string is not present then return -1
# def find_pos(l,target):
#     for pos,name in enumerate(l):
#         if target==name:
#             return pos
#     return -1
# print(find_pos(names,"prak"))