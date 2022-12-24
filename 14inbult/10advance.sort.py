# # advnce shorted fuction
# fruits=['gapes','mango','apple']
# # fruits.sort()
# # print(fruits)h
# ####tuples are immutable
# fruits2=('gapes','mango','apple')# shorted function doesnot change it
# print(sorted(fruits2)) # shorted function gives shorted list
# print(fruits2) # but it doesnot change in original tuple

## set is immutable
fruits3={'gapes','mango','apple'}
print(sorted(fruits3))#sorted function gives sorted list
print(fruits3)# it doesnot change in original set

guitars=[
        {'model':'yamaha f310','price':8400},
        {'model':'faith naptune','price':50000},
        {'model':'faith apollo venues','price':35000},
        {'model':'taylor 814ce','price':450000}
]
print(sorted(guitars,key=lambda d:d['price'],reverse=True))
