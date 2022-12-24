#summary dictionary
# what is dictionary?
# unordered collection of data
d={'name':'prakash','age':23}


#####  or  ############
d1=dict(name='prakash',age=23)

#####or######### 
d2={
    'name':'prakash',
    'age':23,
    'fav':[]
} 

## how to access data from dictionary
# you can not do like
# d[0]   because there is no order inside dictionary

###### syntax  print(dictname[keyname])
#print(d['name']) 

### add data inside enpty dict
#empty_data={}
#empty_data['key1']='value1'
#empty_data['key2']='value2'
#print(empty_data) 

### check existence of value inside dict
## use in keywords to check for keys
#if 'name' in d:
#   print('present')

##### how to iterate over dictionary
# most common method
#for key,value in d.items():
#    print(f"key is {key} and value is {value}")

#print all keys 
#for i in d:
#    print(i)

#to print all value
#for i in d.values():
#    print(i)


# most common dict metthods
# get methods ( to access a key and check existance)  
#print(d.get('name'))


## Q--why we use get
# A--to get rid of error
#  example
#print(d['names']) # if key are not avilable in dict then it gives error
#print(d.get('names'))# if key are not avilable in dict then it give none 

## to delete items ###################
# pop ----take one argument which is keyname
#popped=d.pop('name')
#print(popped)
#print(d)

#popitems
#popped=d.popitem()# it delete ramdamly
#print(popped)

















