#making a function
def goodDay(start_name, end_greet):
    print(f"Hello {start_name} ,have a good day")
    print(end_greet)
    return "Done"

a=goodDay("Nihar", "Thank You")
print(a)
#----------------------------

#Factorial through recursion
def factorial(n):
    if(n==1 or n==0):  #base-cases are very important
        return 1
    return n*factorial(n-1) #Ye apne apko he call krta jayga aur multiply hota jayga

num01= int(input("Enter a number: "))
print(f"factorial of {num01} is {factorial(num01)}")
#---------------------------

#Greates among abc
a_num=1
b_num=2
c_num=3

def greatest(a_num, b_num, c_num):
    if(a_num>b_num and a_num>c_num):
         return a_num
    elif(b_num>a_num and b_num>c_num):
         return b_num
    elif(c_num>a_num and c_num>b_num):
         return c_num

print(greatest(a_num, b_num, c_num))
#-----------------------------

#Sum of n using recursion
input_num= int(input("enter a number: "))
#Creating a function
def rec_of_num(u):
    if(u==1):    #base-case
        return 1
    return rec_of_num(u-1) + u  #func calling, 9+8+7+6+...

print(f"Sum of {input_num} is {rec_of_num(input_num)}")
#-----------------------------


#Remove a word and strip it from the list at same time
def rem(my_list, word):
    n=[]
    for item in my_list:
        if not(item==word):
            n.append(item.strip(word))
    return n


my_list=["Nihar", "Rohan", "an"]
print(rem(my_list, "an"))