'''python lists
lists are ordered collection of data items.
They store multiple items in a single variable
List items are separated by commas and enclosed with in square brackets
List are changeable meanung we can alter them after creation'''
#list are mutable
#list store different data types.
list1=[1,2,3,4,5,6]
print(list1)
list2=["cyber","artificial","probability"]
print(list2)
print(list1[0])
print(list1[1])
print(list1[2])
#List Index

#Each item/element in a list has its own unique index. This index can be used to access any particular item from the list. The first item has index [0], second item has index [1], third item has index [2] and so on.
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#         [0]     [1]      [2]      [3]      [4]

print(colors[len(colors)-3])
if "blue" in colors:
    print("yes")
else:
    print("no")
if "lue" in "Blue":
    print("yes")
else:
    print("no")
print(colors[2:5])
#jump index->skip the element
print(colors[1:4:2])
print(colors[:])
lst=[i for i in range(4)]
print(lst)
list0=[i*i for i in range(10)]
print(list0)
