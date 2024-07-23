#Chap01 is about: comments/ modules/ pip

print("hello world")  #our first python hello! 

#Module is something written by someone else
#Module is installed using pip, pip is a package manager for python, just like npm for Node.js
#like, pip install pyjokes
#installed, and now will import the module

import pyjokes

joke = pyjokes.get_joke()
print(joke)

#So, it printed a joke ! 
#Python if opend in terminal, does Read, Evaluate, Print, Loop (REPL)
#Hence in terminal, it can be used as calculator :)

"""
This is a multi line comment
It need to be written inside 
tripple quotes

"""

#------------------------------
# Problem01-twinkle star poem

print(""" 
Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the traveler in the dark
Thanks you for your tiny spark;
He could not see which way to go,
If you did not twinkle so.

In the dark blue sky you keep,
And often through my curtains peep,
For you never shut your eye
Till the sun is in the sky.

As your bright and tiny spark
Lights the traveler in the dark,
Though I know not what you are,
Twinkle, twinkle, little star.

Twinkle, twinkle, little star,
How I wonder what you are!

""")

#---------------------------------
#Problem02: Install external module and perform any operation of ur intrest
#pip install pyttsx3
#All the below code is available on pyttsx3

import pyttsx3
engine = pyttsx3.init()
# engine.say("Hey! Nihar whatsup! Nice to meet you.")
# engine.runAndWait()

#change the voice to female

voices = engine.getProperty('voices')  
engine.setProperty('voice', voices[1].id)
engine.say("Hey! Nihar whatsup! Nice to meet you.")
engine.runAndWait()

#----------------------------------------------------
#Problem03- write content of directory using os module
#Used Chatgpt

import os

#Specify the directory you wanna list
directory_path = '/'

#List all files and directories in the specified path
content = os.listdir(directory_path)

#Print each file and directory name
for item in content:
    print(item)


