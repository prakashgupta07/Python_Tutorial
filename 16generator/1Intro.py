#introduction of generator
#generators
#generator are iterators
#iterator ,iterable
l=[1,2,3] #iterable
# for i in l:
#     print(i)

# i=iter(l)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))

for num in map(lambda a:a**2,l):#iterator
    print(num)
############### note:- we can run loop with both iterable or iterator
#if you wanna run your loop iterator you no need to iterable to iterator

#memory------[whole list create in the memory it uses more memory] in case of list
#memory-------in case of generator at a time only one element generate ,it congueme less memory
