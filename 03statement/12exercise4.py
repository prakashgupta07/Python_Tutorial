# ask user to input a number containg  more than one digit 
#ex= 1123356 
# calculate    1+1+2+3+35+6  


n=input("enter a number more then one digit")
total=0
i=0 
while i<len(n):
    total+=int(n[i]) 
    i+=1 
print(total)

