# write csv file writer,DictWriter
#1):- WRITER 
# from csv import writer
# with open('file1.csv','w',newline='') as f:
#         csv_writer=writer(f)
#         #methods-writerow,writerows
#         # csv_writer.writerow(['name','country'])
#         # csv_writer.writerow(['rohit','india'])
#         # csv_writer.writerow(['prakash','india'])

#         ###writerows method
#         csv_writer.writerows([['name','country'],['rohit','india'],['prakash','india']])

#2):- DictWriter
from csv import DictWriter
with open('file2.csv','w',newline='') as f:
        csv_writer=DictWriter(f,fieldnames=["firstname","lastname",'age'])
        csv_writer.writeheader()
        # writerow,writerows
        # csv_writer.writerow({
        #         'firstname':'prakash',
        #         'lastname':'gupta',
        #         'age':24
        # })
        # csv_writer.writerow({
        #         'firstname':'rakash',
        #         'lastname':'gupta',
        #         'age':24
        # })
        #writewors---[dict,dict,dict]
        csv_writer.writerows([
                {'firstname':'prakash',
                'lastname':'gupta',
                'age':21},
                {'firstname':'rakash',
                'lastname':'gupta',
                'age':22},
                {'firstname':'sam',
                'lastname':'gupta',
                'age':23}])
        