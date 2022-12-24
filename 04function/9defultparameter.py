# defult parameter
def defult_parameter(first_name,last_name,age=22):
    print(f"your first name is{first_name}")
    print(f"your last name is {last_name}")
    print(f"your age is {age}")
 
print(defult_parameter("prakash","gupta")) 


#defult parameter comes last to first
# if defult parameter not in last  and it coms in start or middle it gives error 
#  def defult_parameter(first_name,last_name,age=):