#list comperhension with if statement
numbers=list(range(1,11)) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
# # normal mrthod 
# def even_list(l):
#     even=[]
#     for i in l:
#         if i%2==0:
#             even.append(i)
#     return even

# print(even_list(numbers))

## list comperhension 
# def even_list(l):
#     return[i for i in l if i%2==0]
# print(even_list(numbers))


## odd list with normal methods
# def odd_list(l):
#     odd=[]
#     for i in l:
#         if i%2!=0:
#             odd.append(i)
#     return odd 
# print(odd_list(numbers))

# # odd list with list comperhension 
# def odd_list(l):
#     return[i for i in l if i%2!=0]

# print(odd_list(numbers))