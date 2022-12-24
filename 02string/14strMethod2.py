#string method part 2
#string method and solve problem of spaces
name="       prakash      "
name1="......prakash......."  

#lstrip() function   (lstrip() removre the left side of variable)
print(name.lstrip())
print(name1.lstrip("."))   
 
# rstrip() function  (rstrip() remove the right side of variable)
print(name.rstrip()) 
print(name1.rstrip(".")) 

# strip() function  ( srtrip() remove the both side of variable)
print(name.strip()) 
print(name1.strip(".")) 

#replace() function (replace() function replace  argument  to other argument)
print(name.replace(" ",".")) 
print(name1.replace("a","@")) 
str="she is beautiful and she is good dancer" 
print(str.replace(" ","_"))
print(str.replace("is","was")) 
print(str.replace("is","was",1))#it replace the 1 is 
print(str.replace("is","was",2))
