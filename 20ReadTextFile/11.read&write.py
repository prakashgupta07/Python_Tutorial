#read data from csv file1 and write in another
from csv import DictReader,DictWriter
with open('file2.csv','r') as f:
        with open('file1.csv','w',newline='') as w:
                csv_reader=DictReader(f)
                csv_writer=DictWriter(w,fieldnames=['first_name','last_name','age'])
                csv_writer.writeheader()
                for row in csv_reader:
                        fname,lname,age=row['firstname'],row['lastname'],row['age']
                        csv_writer.writerow({
                                'first_name':fname.upper(),
                                'last_name':lname.upper(),
                                'age':age
                        })

