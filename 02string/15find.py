#find  (to find the place of element in given string ) 
str="she is beautiful and she is good dancer" 
print(str.find("is"))
print(str.find("is",5))# 5 is a position (and find after 5 position) 



#to find the second is position 

is_fosition1=str.find("is") 
is_position2=str.find("is",is_fosition1+1)#position of first +1
print(is_fosition1) 
print(is_position2)