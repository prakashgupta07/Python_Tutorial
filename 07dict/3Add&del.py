# add and delete data 
user_info={
    'name':'prakash',
    'age':23,
    'fav_movie':['avtar','iron man'],
    'fav_tune':['awakening','fair fal']
} 

# how to add data 
#user_info['fav_song']=['song1','song2']
#print(user_info)


#pop method 
#popped=user_info.pop('fav_tune') #pop items from dictiornaries
#print(user_info)
#print(popped) # popped items return list type

#popitems method
popped_items=user_info.popitem()
print(user_info)
print(popped_items)
print(type(popped_items)) # popped items return tuple type 



