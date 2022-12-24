from lib2to3.pytree import type_repr


def divide(a,b):
        try:
                return a/b
        except ZeroDivisionError as err:
#                print(" you can't divde number by zero ")
                print(err)   
        except TypeError as err:
                # print("you are not dividing with int")    
                print("number most be int or float")
        except:
                print('unexcepted error')
print(divide(10,"0"))


# note:- 1:  In place "err"  you can choose any things
# note:- 2:  print(err) by defult system prvided error statement
# note:- 3:  except TypeError :
                # print("type error ") you can print your own statement
                # not  sustem defult
# note:-4: except TypeError as err:
#                 print(err) # you can print system statement
#                 print("type error")# you can print your statement 
#                 # it depend on you 