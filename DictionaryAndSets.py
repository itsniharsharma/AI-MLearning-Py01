#Dictionary is set of Key value pairs, just like json in react
#Examples
d={} #empty dictionary

marks={
    "Nihar":100,
    "Shubham": 90,
    "Gitanjali":95
}

marks02={1,2,34,78,9} #it's called a set
emptySet= set() 

print(marks, type(marks)) #type---> 'dict'
print(marks["Nihar"]) #gives 100
#in this we can only search by key, not by value

#Dictionary is mutable! 
marks.update({"Nihar": 99})
print(marks)

#what is difference between both? both give 99
print(marks.get("Nihar"))
print(marks["Nihar"])

#Difference is
#say

# print(marks.get("Nihar0234")) #return none
# print(marks["Nihar0234"]) #return error
#--------------------------------------------


#Methods in sets
s={1,23,7,9, False, "Nihar"}
print(s, type(s))

#in sets, we can't access element by index
#We have to enter value of Key! Like:

word={
    "Chaku": "Knife",
    "ekHazar": 1000,
     "Kela": "banana",
     "RemainingPoor": False
}

key=input("Enter the meaning u want:")
print(word[key]) #Access it by key only, word[Key]=value

#---------Very Important Interview Question

set01= set()

set01.add(20)
set01.add(20.0)
set01.add('20') #What is expected size of set01? probably 3

print(set01) #But it's 2, cauz 20==20.0 (== oprater checks value only, nomaters datatype)



