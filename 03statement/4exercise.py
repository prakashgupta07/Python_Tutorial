#make any variable like winning_number and assign any variable 
#ask user to guess a number 
#if useer guess correctly then print "you win!!"
# if user guess incorredtly then :
         # if user guess lower number then actual number then print " too low"
         # if user guess higher number then actual number then  print" too high"  


winning_number= 25 
user_number=int(input("enter your number"))
if winning_number==user_number:
    print("you win !!")
else:
    if winning_number>user_number:
        print("too low") 
    else:
        print("too high")