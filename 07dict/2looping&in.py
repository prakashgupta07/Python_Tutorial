# in keywords and iterations in dictionary
user_info={
    'name':'prakash',
    'age':23,
    'fav_movie':['avtar','iron man'],
    'fav_tune':['awakening','fair fal']
}


# check if key exist in dictionary 
#if 'names' in user_info:
#    print("present")
#else:
#    print("not present")


#check if value exist in dictionary ---- values method 
#if 'prakash' in user_info.values():
#    print("present")
#else:
#    print("not present")


#loops in dictionaroies 
#for i in user_info: # it only gives key
#    print(i)


#for i in user_info.values(): # it gives value
 #   print(i) 

#value method 
#user_info_values=user_info.values()# it help to make the value in list but it is not list ,it is actually distiornaries
#print(user_info_values)
#print(type(user_info_nalues))

### keys methods 
#user_info_keys=user_info.keys() # it help to make the (key ) into list format
#print(user_info_keys)
#print(type(user_info_keys))

# loop in dictionaries 
#for i in user_info: # in this ways you print value 
#    print(user_info[i])

#################  items method ################ 
user_items=user_info.items()
print(user_items)#[('name', 'prakash'), ('age', 23), ('fav_movie', ['avtar', 'iron man']), ('fav_tune', ['awakening', 'fair fal'])])
print(type(user_items))

for key,value in user_info.items():
    print(f"key is{key} and is value {value}")
 