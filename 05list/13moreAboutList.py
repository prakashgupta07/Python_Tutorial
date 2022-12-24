#more about list
# generate list with range function 
numb=list(range(1,11))
print(numb)
#numb.append(1)

# more with pop function 
#numb.pop()
#print(numb) 
#print(numb.pop()) # what pop function delete you can also print 


#indedx method   ( to help finding the position of items in list) (index(list element,start,stop))
#print(numb.index(8)) 

# function with list
number=[1,2,3,4,5,6,7,8,9] 
def negative_list(l):
    negative=[]
    for i in l:
        negative.append(-i)
    return negative
    
print(negative_list(number))



 