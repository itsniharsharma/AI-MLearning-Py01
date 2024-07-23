name= "niharSharma" # is a string
name01= """ Nihar Sharma is multi line string
            it can be in this line too"""

#String have an idex, if counting from left, 0,1,2,3,4...
# if counting from opposit side, -1,-2,-3,-4......

#now, how to obtain a shortString for any string?___ Its called slicing
#see positive slicing
nameshort = name[0:4] #start from index 0 all the way till 4, excluding 4
print(nameshort)

#negative slicing is
print(name[-4:-1])
#Just dont do it like that, make it +ve
print(name[1:4])


#say if written like this
print(name[:]) # staring from 0, till len(name)-1

#understand skip value
# say
a = "0123456789"
print(a[1:7:3])
#means, slicing till 6, from 1 with a gap of 3
# output will be 14 