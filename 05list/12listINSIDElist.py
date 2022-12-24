#list inside list
matrix=[[1,2,3],[4,5,6],[7,8,9]]# 2d matrix 
#3itmes inside matrix
for sublist in matrix:
    for i in sublist:
        print(i)

print(matrix[1][1]) 
# type function    find the type of variable
print(type(matrix))