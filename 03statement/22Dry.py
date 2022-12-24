# dry pricipal of coading 
#DRY= do not repeat yourself
import random
winning_number=random.randint(1,100)
print(winning_number)
n=int(input("enter your number"))
guess_time=1
#game_over=False
#while not game_over:
#    if n==winning_number:
#        print(f"you win!! and your win time is{guess_time}")
#        game_over=True
#    else:
#        if n>winning_number:
#            print("too high")
#        else:
#            print("too low")
#        n=int(input("try ahain"))
#        guess_time+=1
while True: 
    
    
    if n==winning_number:
        print(f"you win!! and your guess time is {guess_time}")
        break
    else:
        if n>winning_number:
            print(f"too high")
        else:
            print("too tow")
        n=int(input("try again"))
        guess_time+=1 
        continue