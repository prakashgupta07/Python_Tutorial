#import random 
import random
winning_number=random.randint(1,100) 
n=int(input("enter your number"))
guess_time=1 
game_over=False
while not game_over:
    if n==winning_number: 
        print(f"you win!!  and your guess time is {guess_time}")
        game_over=True
    else:
        if n>winning_number:
            print("too high!!")
            n=int(input("try again!!"))
            guess_time+=1 
        else:
            print("too low!!")
            n=int(input("try again!!")) 
            guess_time+=1
            