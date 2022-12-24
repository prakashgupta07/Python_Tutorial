#1 reverse a given list in python
#alist=[100,200,300,500]
#alist=alist[::-1]
#print(alist)

#2 concatenate two lists index-wise
#list=['M','na','i','Ke']
#list2=['y','me','s','lly']
#list3=[i+j for i,j in zip(list,list2)]
#print(list3)

#3 Given a python list of a list into its spuare
#alist=[1,2,3,4,5,6,7]
#alist=[x*x for x in alist]
#print(alist)

#4 concatenate two list in the following order
#list=['Hello ','take ']
#list1=['dear','sir']
#new=[y + x for y in list1 for x in list]
#print(new)

#5 Given a two python list. Iterate both lists simultaneously such that list1 should display items in original order and list2 in reverse order
#list1=[10,20, 30, 40]
#list=[100,200,300,400]
#for x,y in zip(list1,list[::-1]):
#    print(x,y)

# 6 remove empty string from the list of string
#list1=['mike','','Emma','Kelly','','Brad']
# use a filter() function to remove NONE type from the list
#newlist=list(filter(None,list1))
#print(newlist)
# 7 add items 7000 after 6000 in the following python list
#list1=[10,20,[300,400,[500,600],500],30,40]
#list1[2][2].append(7000)
#print(list1)

#8 given a nested list entend it by adding the sub list["h","i","j"] in such a way that it 
  #will look like the fowwling list
#list1=["a","b",["c",["d","e",["f","g"],"k"],"l"],"m","n"]
#sublist=["h","i","j"]
#list1[2][1][2].extend(sublist)
#print(list1)

##Given a python list, find value 20 in list , and if it is present ,replace it with 
# 200. only update the first occurrence of a value 
list1=[5,10,15,20,25,50]
index=list1.index




