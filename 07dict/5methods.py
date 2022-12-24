# fromkeys, get,copy ,clear methods


##### fromkeys use to creat distionaries 
# eg--d={'name':'unknown','age':'unknown'}

#d=dict.fromkeys(['name','age','height'],'unknown') # list
#print(d)

#d=dict.fromkeys(('name','age','height'),'unknown')# tuple
#print(d)

#d=dict.fromkeys("abc",'unknown')#{'a': 'unknown', 'b': 'unknown', 'c': 'unknown'}
#print(d)

#d=dict.fromkeys(range(1,6),'unknown') # RANGe function
#print(d)#{1: 'unknown', 2: 'unknown', 3: 'unknown', 4: 'unknown', 5: 'unknown'}
#d=dict.fromkeys(['name','age'],['unknown','unknown']) 
# print(d)#{'name': ['unknown', 'unknown'], 'age': ['unknown', 'unknown']}


##### get method (useful)
d={'name':'unknown','age':'unknown'}
#print(d['name'])
#print(d.get('name'))
#print(d.get('names'))# if keys are not present in the dictionaries it give (none)


#if 'name' in d:
#    print("present")
#else:
#    print("not present")

#if d.get('name'):
#    print("present")
#else:
#    print("not present")    

#  if none-------false, else------true


#### clear mrthod
#d.clear()
#print(d)


###### copy method  
d1=d.copy()
print(d1)
