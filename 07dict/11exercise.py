#1convert two list it into dicitonary
#l1=['ten','twenty','thiety']
#l2=[10,20,30]
#dict1=dict(zip(l1,l2))
#print(dict1) 
#2 merge following two python dictionaries into one
#dict2={'fourty':40,'fifty':50,'sixty':60}
#dict3={**dict1,**dict2}
#print(dict3)
             ## other version with update method 
#dict3=dict1.copy()
#print(dict3)

#3 Access the value of key "history" from the below dict
#sampledict={
 #   'class':{
  #      'student':{
   #         'name':'mike',
    #        'marks':{
     #           'physice':70,
      #          'history':80
       #     }
#        }
#    }
#}
#print(sampledict['class']['student']['marks']) 
 
#4 initialize dictionary with defult values
#employees=['kelly','emma','john']
#defult={'designation':'Application Developer','salary':8000}
#redict=dict.fromkeys(employees,defult)
#print(redict)

#5 creat a new dictionary by exracrting the following keys from the below dictionary
#SampleDict={
#    'name':'Kelly',
#    'age':25,
#    'salary':8000,
#    'city':'new york'
#}
#keys=['name','salary']
#newDict={i:SampleDict[i] for i in keys}
#print(newDict)

#6  delete set of keys from a dictionary
#SampleDict={
#    'name':'Kelly',
#    'age':25,
#    'salary':8000,
#    'city':'new york'
#}
#keys=['name','salary']
#new={SampleDict.pop(i) for i in keys}
#print(SampleDict)

#7 check if a value 200 exists in a dictionary
#sampleDict={'a':100,'b':200,'c':300}
#print(200 in sampleDict.values())

# 8 rename key city to location in the following dictionary
#SampleDict={
#    'name':'Kelly',
#    'age':25,
#    'salary':8000,
#    'city':'new york'
#}
#SampleDict['location']=SampleDict.pop('city')
#print(SampleDict)

#9 get the key of the minimum value from the following dictionary



#sampledict={
#    'physice':82,
#    'math':65,
#    'history':75
#}
#print(min(sampledict,key=sampledict.get))

#10 change brad's salary to 8500from a given python dictionary
sampledict={
    'emp1':{'name':'john','salary':7500},
    'emp2':{'name':'emma','salary':8000},
    'emp3':{'name':'brad','salary':6500}
}
sampledict['emp3']['salary']=8500
print(sampledict)