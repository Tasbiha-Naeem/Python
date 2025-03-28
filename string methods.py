#strings are immutable
a="harry"
print(a.upper())#you get the new string
b="CoDe"
print(b.lower())

#rstrip removes any trailing characters
a="tasbiha naeem!!!!!"
print(a.rstrip("!"))
#replace all accourence of a string with another string
name="tasbiha naeem"
print(name.replace("tasbiha","Hiba"))
#the split method split the given string at the specified instance and return the separated string as list items.
y="mango orange banana"
print(y.split(" "))
#the capitalize method turn only the first character in upper case and rest of the in lower case
surname="RajPUT"
print(surname.capitalize())
#the center method aligns the string to the center as per the given parameter
str="welcome to code help"
print(len(str))
print(str.center(50))
print(len(str.center(50)))
#count:returns the number of times the given value has occured with in the given string
name="Tasbiha Naeem"
print(name.count("m"))
#endswith() method checks if the string ends with a given value if yes then return true else return false
str1="Welcome to the console!!!!"
print(str1.endswith("!!!!"))
print(str1.endswith("to",4,10))
#find method searches for the first occurence of the given value and returns the index where it is present.If given value is absent from the string then return -1.
str2="He is a world champion"
print(str2.find("is"))
#index method is similar to find but index raises an exception if value is absent whereas find does not
print(str2.index("is"))
#isalnum method check that your string is alphanumeric or not it give true if string consist of A-Z,a-z,0-9
newstr="Hello1rabia"
print(newstr.isalnum())
#isalpha chech that your string is consist of A-Z a-z
print(newstr.isalpha())
#islower check that all the character of the string are in lower case if yes then return true otherwise false
print(newstr.islower())
#isprintable method return true is all the values with in the given string are printable,if not,then return False.
str4="Cyber security is a tech field"
print(str4.isprintable())
#istitle return true if all the word first letter is capital
str5="Artificial Intelligence"
print(str5.istitle())
#startswith method check that if a string start with a given value if yes then return true else return false
str7="Artificial intelligenve vs human intelligence"
print(str7.startswith("Artificial"))
#swapcase change the upper case into lower case and lower case into upper case
str9="i am learnIng pYthon"
print(str9.swapcase())
#title capitalize each letter of the word in the string
str1="Hello I am dua"
print(str1.title())












