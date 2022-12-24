# list is a data structure  that can hold any type of data

#create list
words=['prakash','gupta']

# you can store anything inside list 
mixed=[1,2,3,[4,5,6],'seven',8.0,None]
#print(mixed[1])
#print(mixed[3]) #3rd position pr list hai jo ki ek hi items mani jayegi

# add data to our list  
# append method  
#mixed.append(10) # add element in last
#mixed.append([10,20,30]) # list is also added  
#print(mixed)

# extend method 
#mixed.extend([10,20,30])# list will not add only element of list will add  
#print(mixed)

# join list 
# list=l1+l2

#insert method 
#mixed.insert(1,"str") # will add the element to  particular position
#print(mixed)


##########
#to remove data from list  
#popped=mixed.pop()# remove last items
#print(mixed)
#popped=mixed.pop(1) # only positional element remove
#print(mixed)
#print(popped)

# remove function
#print(mixed)
#mixed.remove("seven") # removr element in your list
#print(mixed)

#del statement
#del mixed[3] # delete the posioinal element
#print(mixed)
