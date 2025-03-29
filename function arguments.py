'''There are fourtypes of arguments that we can provide in a function:
1.default arguments
2.keyword arguments
3.variable length arguments
4.required arguments
default argument:
we can provide a default value while creating a function.This way the function assumes
a default value even if a value is not provided in the function call for that argument.'''
def name(fname,lname="maha",nname="saba"):
    print("Hello",fname,lname,nname)
name("alishba")
'''keyword arguments
we can provide arguments with key=value,this way the interpreter
recognizes the arguments by the parameter nme.Hence,the order in ehich the arguments are passed does not matter'''
def name(fname,lname,nname):
    print("Hello",fname,lname,nname)
name(fname="sana",nname="aisha",lname="laiba")
'''required arguments:in case we dont pass the arguments with a key=value syntax,then it is necessary to pass the arguments in the correct positionl order and the number of arguments passed should match with actual function definition.'''
def name(fname,lname,nname):
    print("Hello",fname,lname,nname)
name("sana","yumna","fiza")
'''Variable length argument:sometimes we need to pass more arguments than those defined in the actual function.This can be done using variable length arguments.there are two ways to achieve this:
Arbitary arguments:while creating a function pass a* before the parameter name while defining the function.The function accesses the arguments by processing them in the form of tuple.'''
def average(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    print("Average is:",sum/len(numbers))
average(5,6)   
'''keyword arbitary arguments:while creating a function pass a* before the parameter name while defining the function.The function accesses the arguments by processing them in the form of dictionary.'''
def name(**name):
    print("Hello",name["fname"],name["lname"],name["nname"])
    
name(fname="sara",lname="minahil",nname="dua")
#return statement:the return statement is used to return the vlue of the expression back to the calling function.
def sum(a,b):
    sum=a+b
    return sum
print("sum:",sum(10,20))

