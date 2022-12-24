# Define is_palindrome function that take one words in string as input 
# return True if it is  palindrome else return False 
# Palindrome-- the words that reads same backwards as forwards  



#def is_palindrome(words):
#    reverse=words[::-1]
#    if reverse==words:
#        return True 
#    return False



#def is_palindrome(word):
#    if word==word[::-1]:
#        return True
#    return False 

def is_palindrome(word):
    return word==word[::-1]
n=input("enter word")
print(is_palindrome(n)) 
