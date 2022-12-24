# try,Except: exception hendling, python tutorial 207#
#try 
# except 
# else finally
## except ValueError(this error come in on excution time)
# multiple "except" block can be heppen for "try"

while True:
        try:
                age=int(input('enter your age'))
                break
        except ValueError:
                print("invlid input")
        except:
                print("unexcepted error....")
if age<18:
        print('you can\'t play game')
else:
        print('you can play game')
