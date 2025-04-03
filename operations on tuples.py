'''Manipulating Tuples
Tuples are immutable, hence if you want to add, remove or change tuple items, then first you must convert the tuple to a list. Then perform operation on that list and convert it back to tuple.
'''
countries=("Italy","Japan","England","America","Korea")
temp=list(countries)
temp.append("Russia")  #add item
temp.pop(3)   #remove item
temp[3]="Finland"   #change item
countries=tuple(temp)
print(countries)
#concatenate tuple
coursesem1=("programming fundamentals","ICT","calculas")
coursesem2=("object oriented programming","digital logic design","expository writting")
sem1andsem2=(coursesem1+coursesem2) # a new tuple will be created.
print(sem1andsem2)
#index() method
#The index() method returns the first occurrence of the given element from the tuple.
tup=(1,2,3,4,5,6,7,8,9,10)
print(tup.index(3))
print(tup.index(8,4,9)) #(element,start,end)
res=len(tup)
print(res)












