
import pdb
# import pdb module
#module-Python file contains usefull classes and functions wrote
#by developer


#according to wikipedia- Debugging is the prodess of finding and resolving defects or problems 
# within a computer program that prevent correct operation of computer software or a system

# why debugging?
#1.) our programm is not running and causing unexpected error.
#2.) our program is working fine but notworking that same way we want.

# steps for debugging
#1.)set trace
#2.) execute code line by line
pdb.set_trace()
name=input("enter your  name")
age=input("enter your age")
print(f"hello {name} your age is {age}")
age2=int(age)+5
print(f"{name} your age is {age2} in next five years")

# # note:1:)"l":-show the line where the code line are stopa  in program
#           2:) "n":- run that line you are in ProgrammingError
#           3:) "q":-quit the program Execution
#           4:) "c":- continoue  the program to execute
