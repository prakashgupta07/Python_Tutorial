#continue statement 
# print 1 to 10 but not 5 
for i  in range(1,11):
    if i==5: #only 5 will not print 
        continue
    print(i)