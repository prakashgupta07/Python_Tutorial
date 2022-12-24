user={}
name=input('enter your name')
age=int(input('enter your age'))
fav_movie=input('enter your tune seprated by commma').split(',')
fav_song=input('enter your song seprated by comma').split(',')

user['name']=name
user['age']=age
user['fav_movie']=fav_movie
user['fav_song']=fav_song
print(user)
for key,value in user.items():
    print(f"{key} : {value}")