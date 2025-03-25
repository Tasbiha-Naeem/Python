#There are two types of functions,one is built in and other one is user defined function.
#min() max() len() sum() type() range() dict() list() tuple() set() print()...etc
def calculategmean(a,b):
    mean=(a*b)/(a+b)
    print(mean)
def greaternumber(a,b):
    if(a>b):
        print(a,"is greater")
    else:
        print(b,"is greater")
def lessernumber(a,b):
    pass #pass mean will write the function body later
a=9
b=8
calculategmean(a,b)
greaternumber(a,b)
c=8
d=7
calculategmean(c,d)
greaternumber(c,d)
