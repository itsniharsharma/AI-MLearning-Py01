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


#below is called chaining
letter='''<Name> You are selected! 
           <Date>'''

print(letter.replace("<Name>", "Nihar").replace("<Date>", "23 July 2024"))
#----------------------------------



#--------How to detect any double space?
# Lets see

quote="I am Investing and Trading at  same time"
print(quote.find(" "))
print(quote)
print(quote.replace("  ", ""))
print(quote)

#See, strings are imutable!
#But Lists are mutable 
#Diff b/w List and Tuples?, tuples are immutable
#Original string will always remain the same!

#Have some basic functionss:
# funct.append(append at last)
# funct.sort(sort in asc ord)
# funct.reverse(reverse the string)
# funct.insert(Insert at index x, value of y)
# funct.pop(index : x), It delete element at idx x 

#Tuple:-------------

u=(1,2,3,4,False,"Rohan")
print(type(u)) #tupple
#u[0]=32 #error, can't be muted!

tup01=(1,24,False,"Shivam",24)
print(tup01)

no=tup01.count(24)
print(no)  # return 2

print(u.index(False))  #4

#----------------------

marks=[]

st1=input("enter marks:")
marks.append(st1)
st2=input("enter marks:")
marks.append(st2)
marks.sort()
print(marks)

