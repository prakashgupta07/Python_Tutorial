# sorted function
# sort function with list
fruits=["grapes","mango","apple"]
fruits.sort()
print(fruits)
# sorted function with tuple 
fruits2=("grapes","mango","apple")
print(sorted(fruits2))
print(fruits2)
#sorted function with set
fruits3={"grapes","mango","apple"}
print(sorted(fruits3))
#dictionary
guitar=[
        {"model":"yamaha","price":8400},
        {"model":"yamaha","price":50000},
        {"model":"yamaha","price":35000},
        {"model":"yamaha","price":8400000}
]
print(sorted(guitar,key=lambda d:d["price"],reverse=True))
