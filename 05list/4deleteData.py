# # method to delete data in your list ?   clear ,pop, del, remove?
#pop() method 
fruits=['apple','banana','mango','kiwi','pear','apple']
#fruits.pop()# it delete last element of list if you not pass position of element
#fruits.pop(1)


#del[] operator 
#del fruits[0] # delete the positional element

#remove() mrthod # you know particular element position in your list 
#fruits.remove('kiwi') # remove kiwi from your list 

#fruits.remove('apple') # if you havr two or more same element in your list  then remove method remove first one  


#clear method   #   clear method delete whole element from your list
fruits.clear()
print(fruits)