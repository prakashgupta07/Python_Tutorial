import os
# print(os.getcwd())
# os.mkdir('movie') # create folder
# print(os.path.exists('movie'))# to check folder in your 'cwd' or not it give true ,false in  value

# if os.path.exists('movie'):
#         print('already exists')
# else:
#         os.mkdir('movie')
########## make folder in other locatiol
#1):-
# copy path and make folder
# os.mkdir(r'D:\prakash')
#2):-
# os.chdir(r'D:\\')# change path 
# os.mkdir('prakash')
###### listdir() # make a list of all file and folder in "cwd"
#print(os.listdir())
#print(os.listdir(r'D:'))
### path of file
#1:) 
# os.chdir(r'D:\\')
# for item in os.listdir():
        # print('D:'+'\\'+item)

#2:)
os.chdir(r'D:\\')
for item in os.listdir():
        print(os.getcwd() +item)
        #print(os.path.join(os.getcwd(),item))
        