# prakash,100
#mohit, 500
# aaditya,100
# nitist,200
import pdb
pdb.set_trace()
with open("file.txt",'r') as rf:
        with open('file1.txt','a') as wf:
                for lines in rf.readlines():
                        name,salary=lines.split(',')
                        wf.write(f"{name}\'s your salary is {salary}")




