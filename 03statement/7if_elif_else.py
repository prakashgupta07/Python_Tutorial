# show ticket pricing 
# 1 to 3  (free) 
# 4 to 10  (150)
#11 To 60 (250)
# above 60 (200)
age=int(input("enter your age"))
if 0<age<=3:
    print("ticket price is:free")
elif 3<age<=10:
    print("ticket price: 150")
elif 10<age<=60:
    print("ticket price: 250")
else:
    print("ticket price:200")