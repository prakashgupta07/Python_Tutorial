#define generator function
#take one number as argument
#generate a sequence of even numbers from 1 to that number

def is_even(n):
        for num in range(1,n+1):
                if num%2==0:
                        yield num  
        

n=10
numbers=is_even(n)
print(numbers)
for num in numbers:
        print(num)
