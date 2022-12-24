#advace min() and max() function
# numbers=[1,2,4,5,7]
# print(max(numbers))

# def fun(items):
#         return len(items)     
# names=['prakash','kumar','gpta']
# print(max(names,key=fun))

# #with the help of lambda function
# print(min(names,key=lambda item:len(item)))

students1={
        'prakash':{'score':90,'age':24},
        'mohit':{'score':75,'age':19},
        'rohit':{'score':76,'age':23}
}
print(max(students1,key=lambda item:students1[item]['score']))
print(min(students1,key=lambda item:students1[item]['score']))


# students2=[
#         {'name':'prakash','score':90,'age':24},
#         {'name':'mohit','score':75,'age':19},
#         {'name':'rohit','score':76,'age':25}
# ]
# print(max(students2,key=lambda items:items.get('score'))['name'])
# print(max(students2,key=lambda items:items.get('age'))['name'])
