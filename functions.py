name="Nihar"
print(len(name)) #5
print(name.endswith("har")) #True
print(name.startswith("nih")) #False


#say, 
name01= "tejas"
print(name01.capitalize()) #Tejas


#Some other important functions
x="Nihar is a good person"
print(x.replace("good", "bad"))
# Nihar is a bad boy


#----------------Concepts of f string
name04=input("enter your name: ")
print(f"Good Afternoon, {name04}")
#----------------

letter='''<Name> You are selected! 
           <Date>'''

print(letter.replace("<Name>", "Nihar").replace("<Date>", "23 July 2024"))

#--------How to detect any double space?
# Lets see

quote="I am Investing and Trading at  same time"
print(quote.find(" "))
print(quote)
print(quote.replace("  ", ""))
print(quote)
