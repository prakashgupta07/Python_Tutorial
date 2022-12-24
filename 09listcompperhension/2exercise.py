#define a function that take list of strings
#list containing reverse of every string
#note - use list comperehension because we already did this exercise 
# using normal method 

# def reverse_string(l):# old method
#     new_list=[]
#     for i in l:
#         new_list.append(i[::-1])
#     return new_list

# l=['abc','def','ghi']
# print(reverse_string(l))

# list comperhension
def reverse_str(names):
    return[name[::-1] for name in names]

l=['abc','def','ghi']
print(reverse_str(l))

