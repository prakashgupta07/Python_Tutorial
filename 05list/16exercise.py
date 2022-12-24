# define a frnction that ake list of words as argument and 
# return list with reverse of erery element in that list

def reverse_str(s):
    str=[]
    for i in s:
        i[::-1]
        str.append(i[::-1])
    return str

str1=["prakash","kumar","gupta"]
print(reverse_str(str1))