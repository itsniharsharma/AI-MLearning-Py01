'''
 So in python, sequence of a programe is 
-we write a code
-It's compiled and temporarily loaded in RAM and then run
-Code isn't stored anywhere 
-To store it, we use File I/O
-RAM= Volatile memory, temp loaded
-HDD= Non Volatile, permanant persistance

-From file, we can read and write, append
'''

# file= open("iofile01.txt")
# data= file.read()
# print(data) 
# file.close()

# I am not getting my file, plz help

st="Hey Nihar, how are You?"

f=("myNewFile.txt", "w")
f.write(st)
f.close()

#In order to avoide close statemet, we use with statement
#Just like
with open("myfile.txt") as f:
    print(f.read())


