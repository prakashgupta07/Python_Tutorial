#file I/O :write to file
#w
#a
#r+

with open('file.txt','r+') as f:
        f.seek(len(f.read()))
        f.write('please do it')