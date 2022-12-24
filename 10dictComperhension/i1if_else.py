# dictionary comprehension with if_else
#  EXAMPLE---> {1:;ODD,2:EVEN}
odd_even={i:('even' if i%2==0 else 'odd') for i in range(1,11)}
# print(odd_even)
# for key,value in odd_even.items():
#     print(f"{key}:{value}")

# it is not dictionary comrehension .it is simple dictionary
# print key in dictionary 
# for i in odd_even:
#     print(i)
###### print in values in dictionary
for i in odd_even.values():  #/for i in odd_even:
    print(i)#/print(odd_even[i])
# value method (value look like list ,but it is not list)
# odd_even_values=odd_even.values()
# print(odd_even_values)
# print(type(odd_even_values))

# #keys method (keys lool like list , but it is not list) 
# odd_even_keys=odd_even.keys()
# print(odd_even_keys)
# print(type(odd_even_keys)) 
