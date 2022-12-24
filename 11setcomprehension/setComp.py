#only one video 
#set comprehension 
# s={k**2 for k in range(1,11)}
# print(s)
names={'prakash','kumar','gupta'}
s={name[0] for name in names}
print(s)

# Creating an empty Dictionary
Dict = {}
print("Empty Dictionary: ")
print(Dict)
 
# Creating a Dictionary
# with dict() method
Dict = dict({1: 'Geeks', 2: 'For', 3:'Geeks'})
print("\nDictionary with the use of dict(): ")
print(Dict)
 
# Creating a Dictionary
# with each item as a Pair
Dict = dict([(1, 'Geeks'), (2, 'For')])
print("\nDictionary with each item as a pair: ")
print(Dict)