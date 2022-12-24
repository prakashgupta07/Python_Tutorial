# read and write
# read data from fie 1 and write data in file 2

with open("file.txt",'r') as af:
        with open('file1.txt','w') as wf:
                wf.write(af.read())
