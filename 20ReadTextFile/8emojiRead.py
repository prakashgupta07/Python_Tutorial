# # read emojis from file
# with open('1file.txt','r',encoding='utf-8') as f:
#         print(f.encoding)
#         data= f.read()
#         print(data)

with open('1file.txt','r',encoding='utf-8') as f:
        data=f.read(100)
        while len(data)>0:
                print(data)
                data=f.read(100)