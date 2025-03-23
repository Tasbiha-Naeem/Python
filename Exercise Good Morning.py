import time
timestamp=time.strftime("%H:%M:%S")
print(timestamp)
hour=int(time.strftime("%H"))
print(hour)
if(4<= hour <12):
    print("Good Morning")
elif(12<= hour<15):
    print("Good Afternoon")
elif(15<= hour<=19):
    print("Good Evening")
else:
    print("Good Night")
