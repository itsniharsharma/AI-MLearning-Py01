#Loops are like

for i in range(1, 6):
    print(i)   #1-->5
#-----------------------

list=[1, "Harry", "Nihar", False, 100]
i=0
while(i<len(list)):
    print(list[i])
    i+=1
#----------------------

#Test it's outcome
for x in range(0, 100, 4): #Here 4 is called step
   print(x)  #0,4,8,12...
#----------------------

#Traversing over a tupple
tupple=(1, "Nihar", True, 30.67)  #immutable
for i in tupple:
    print(i)
#----------------------

#For loop with Else
l=[1,8,7]

for item in l:
    print(item)
else:
    print("done") #This executes when loop exhausts
#----------------------

for g in range(100):
    if(g==34):
        break #Exit the loop abruptly
    print(g)

for t in range(100):
    if(t==34):
        continue #Skip this iteration
    print(t)
#----------------------

#pass is a null statement in python, instructs to do nothing
for loop_item in range(50):
   pass
#Now this whole loop is skipped
#--------------------------

#Wanna print a table of 16 using f statement
n=int(input("Enter a number: "))  #remb, not like, n=input("Enter a number: ") Xwrong

for i in range(1,21):
    print(f"{n} X {i}= {n*i}")
#---------------------------

#Print all the names starting with N in list
name_list=["Komal", "Nihar", "Nikhil", "Vaibhav", "Divyam", "Nirup", "Tushar"]
for name in name_list:
    if(name.startswith("N")):
        print(f"Name start with N is {name}")
#---------------------------

#Code for Factorial
number=int(input("Enter a Number: "))
product=1
for d in range(1, number+1):
    product=product*d
print(f"Factorial of {number} is {product}")
#-----------------------------

#Skipping Patterns :)

