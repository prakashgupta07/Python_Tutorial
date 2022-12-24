# Else finally with try except

while True:

        try:
                age=int(input("enter your age:"))
        except ValueError:
                print("invalid input")
        except:
                print("unexcepeteed errror")
        else:
                print("your are exigable to play")
                break
        finally:
                print("finally block....")
if age>18:
        print("you can play")
else:
        print("you can't play")