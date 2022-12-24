# min function( to find the mi(nimum number in your list)
numbers=[2,10,78,90,50]
print(min(numbers))

# max function( to find the maximum number in your list)
print(max(numbers)) 


# function who find the difference between max and min
def difference(li): 
    return max(li)-min(li)

print(difference(numbers)) 