# define a function take any no of the list containing number 
# def average_finder(l1,l2):
#         average=[]
#         for i in zip(l1,l2):
#                 average.append(sum(i)/len(i))
#         return average
# print(average_finder([1,2,3],[4,5,6]))
# # if you want to use more then two list use two list
# def average_find(*args):
#         averages=[]
#         for i in zip(*args):
#                 averages.append(sum(i)/len(i))
#         return averages
# print(average_find([1,2,3],[4,5,6],[7,8,9]))

average_finder=lambda *args:[sum(i)/len(i) for i in zip(*args)]
