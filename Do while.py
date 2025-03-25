#Emulate do while loop by using infinite while loop and break statement.
i=0
while True:
    print(i)
    i=i+1
    if(i%100==0):
        break
