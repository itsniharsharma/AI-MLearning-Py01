a= int(input("Enter Your Age:"))

if(a>=18):
    print("You are adult")
elif(a<0):
    print("entring wrong age")
else:
    print("You are Minor")

#---------------------------------------

p1="Make lots of money"
p2="Buy everything"
p3="I am studing in Thapar"

message=input("enter message:")

if((p1 in message) or (p2 in message) or (p3 in message)):
    print("This is spam")

else:
    print("Not a Spam")

#--------------------------------------------

post=input("Enter Post:")

if("Nihar".lower() in post.lower()): #it's will grant words like niHar etc and says in post
    print("It's in post")            # Reson is, comparision when both in lower case hence true
else:
    print("It's not")