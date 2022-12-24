## read csv file use reader,dictreader

# # read csv file with reader
# from csv import reader
# with open('file.csv','r') as f:
#         csv_reader=reader(f) 
#         print(next(csv_reader))
#         print(next(csv_reader))
#         # for i in csv_reader:
#         #         print(i)

## read csv file with dictReader
from csv import DictReader
#order dict
with open('file.csv','r') as f:
        csv_reader=DictReader(f)# BY defult ',' seperated csv file
        #csv_reader=DictReader(f,delimiter='|')  #when csv file is seperated with "|"  or other things
        for i in csv_reader:
                print(i["name"])
