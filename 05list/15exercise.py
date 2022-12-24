# define a function which all takes list as a argument and this function will return a reverse list 
def reverse_list(l):
    l.reverse()
    return l

#def reverse_list(l):
 #   return l[::-1]

#def reverse_list(l):
#    r_list=[]
#    for i in range(len(l)):
#        popped_list=l.pop()
#        r_list.append(popped_list)
#    return r_list


num=["prakash","gupta"]
print(reverse_list(num))
