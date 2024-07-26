'''
1 for snake
-1 for water
0 for gun
'''
import random

comp_choice= random.choice([1, -1, 0]) #generate a rendom choice
user= input("enter a choice: ")
my_dict= {"s":1, "w":-1, "g":0}
reverse_dict={1:"snake", -1:"water", 0:"gun"}

user_choice= my_dict[user]
print(f"You choose {reverse_dict[user_choice]}\n and computer choose {reverse_dict[comp_choice]}")

if(comp_choice==user_choice):
    print("drawnn!")

else:
    if(comp_choice== -1 and user_choice== 1):
       print("you win!")
    elif(comp_choice== -1 and user_choice== 0):
       print("you loose")
    elif(comp_choice== 1 and user_choice== -1):
       print("you loose")
    elif(comp_choice== 1 and user_choice== 0):
       print("you win!")
    elif(comp_choice== 0 and user_choice== -1):
       print("you win!")
    elif(comp_choice== 1 and user_choice== 0):
       print("you loose")
    else:
       print("wrong input")