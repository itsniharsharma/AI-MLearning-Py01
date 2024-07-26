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