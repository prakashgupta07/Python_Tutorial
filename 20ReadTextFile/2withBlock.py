#f=open('file1.txt')
# f.read()
# f.closed()


#### with block###
# context manager

with open('file1.txt') as f:
        data=f.read()
        print(data)