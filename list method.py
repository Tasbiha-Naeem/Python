#append
#sort
#reverse
#index
#count
#copy
#insert
#extend
#concatenate
l=[45,22,33,43,33,33,33]
print(l)
l.append(8)
print(l)
l.sort()  #ascending order
print(l)
l.sort(reverse=True)  #The reverse=True argument tells Python to sort the list in descending order (from largest to smallest).
print(l)
l.reverse()
print(l)
print(l.index(33))
print(l.count(33))
m=l
m[0]=0
print(l)
s=l.copy()
s[0]=14
print(l)
print(s)
fruit=["mango","orange","banana"]
fruit.insert(1,"strawberry")
print(fruit)
#extend(): This method adds an entire list or any other collection datatype (such as a set, tuple, or dictionary) to an existing list.
fruit=["mango,orange,banana,pineapple"]
dryfruit=["almond","walnut"]
fruit.extend(dryfruit)
print(fruit)
#list concatenation
color1=["red","green","blue"]
color2=["pink","yellow","white"]
print(color1+color2)











