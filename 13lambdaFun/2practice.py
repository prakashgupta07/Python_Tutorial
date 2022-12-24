# # lambda exepression practice 
# # normal way
# def is_even(a):
#     if a%2==0:
#         return True
#     else:
#         return False

# n=int(input("enter number"))
# print(is_even(n))


# # lambda expression 
# is_even2=lambda a: a%2==0
# print(is_even2(6))

# #### last  character of string 
# def last_char(s):
#     return s[-1]

# last_char2=lambda s:s[-1]
# print(last_char2('prakash'))


## lambda with if -else
# def func(s):
#     return len(s)>5# it also give TRUE ,FALSE 

# print(func("prakash"))

func2=lambda s: True if len(s)>5 else False # lambda s:len(s)>5 (both are same)
print(func2("prakash"))
