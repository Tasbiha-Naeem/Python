#f-strings is used to insert variable in the string
letter = "Hey my name is {0} and I am from {1}"
country = "India"
name = "Harry"
#format method in string
print(letter.format(country, name))
#fstring
print(f"Hey my name is {name} and I am from {country}")
age=21
print(f" age is {{age}} year")
#-------------------------------------------------------------------------
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49.09999))





