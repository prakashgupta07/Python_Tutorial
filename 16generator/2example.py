#create your first generator with generator function
# 1.) generator function
#2.) generator comprehernion

#input-10 output-1 to 10



def nums(n):
        for i in range(1,n+1):
                yield(i)
print(nums(10))
numbers=nums(10)# this is generator
#we can convert generator into list 
# number=list(nums(10))
for num in numbers:# only once we can print generator noy again and again
        print(num)
for num in numbers:#if you want to print again and again then you have to convert generator into,list ,tuple, dict etc 
        print(num)

# number=nums(10)
# print(next(number))
# print(next(number))
# print(next(number))

#once we convert generator into list,tuple,dict etc the we will loss generator feature