# --- Variables and Data Types ---
a = 10
print (a)
print(type(a)) # a is an integer, a whole number w no decimals

b = 1.5
print (b)
print(type(b)) # b is a float, with a decimal 

c = 3j 
print(c)
print(type(c)) #c is complex, that has an imaginary component

d = "Hello"
print(d)
print(type(d)) #d is a string, as it is a phrase 

e = [1,2,3]
print(e)    
print(type(e)) #e is a list of numbers 

f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f)) #f is a dictonary, as it has multiple defined values 

g = (1,2)
print(g)
print(type(g)) #g is a tuple, an ordered collection of elements 

h = ["apple", "banana", "strawberry"]
print (h)
print(type(h)) #h is a list of fruits 

i = True
print (i)
print(type(i)) #i is a boolean, that takes on true or false 

j = None 
print(j)
print(type(j)) #j is nonetype as an object indicates no value 

k = [True, "blue", 12]
print (k)
print(type(k)) #k is a list as it stores multiple items in a single variable

l = str(14)
print(l) 
print(type(l)) #l is a string as str converted the integer into string

m = 1e4
print(m)
print(type(m)) #m is a float as its 10000.0 that has a decimal 

#I found nine different types of data
# I found integer, float, complex, string, list, dictionary, tuple, boolean, and nonetype.
# B and M are floats. D and L are strings. E, H, and K are lists. 
#The data type of l is a string. It's not an integer as the str() is a built in function in python that converts a specified value into a string.
#This is a range. 

x = range(5)
print(x)
print(type(x)) #this is a range that represents the sequence without storing values 

print(10>9) #True, 10 is greater than 9
print (10==9) #False, 10 is not equal to 9 
print(10<=9) #False, 10 is not less than 9 
print(bool("abc")) #True, because any non-empty string is True 
print(bool(["apple", "cherry", "banana"])) #True, because any non-empty string is True 
print(bool(True)) #True, as it was set to Truth
print(bool(False)) #False, as it was set to False 
print(bool(0)) #False because there is no quantity
print(bool("")) #False because its an empty string 
print(bool(" ")) #True because its not an empty string
print (bool([])) #False becaue its an empty list 
print(bool({})) #False because its an empty dictionary  
print(bool(True and False)) #False, both can't be true
print(bool(True and True)) #True, both are true 
print(bool(False and False)) #False, both are false 
print(bool(True or False)) #True, at lease one in the table is true 
print(bool(True or True)) #True, at least one is True
print(bool(False or False)) #False, at least one false 
print(bool(not(False))) # True as it flips the False
print(bool(not(True))) #False as it flips the True

#Python has True when something is there or a sucess happens. It represents False when it represents nothing or is a failure. 
#I was suprised that print(bool(" ")) returned True even though it doesn't look like anything is in it. 
#print(bool(not(False or False))) The inside expression will return False and then it flips because of the not to return True. 
#print(bool(not(True and True))) The inside expression will return True and the not will flip it to False. 

print(10+5) #15, + preforms addition
print(10-5) #5, - preforms subraction
print(2*4) #8, * preforms multiplication
print(6/3) #2.0, / preforms division
print(5%2) #1, % preforms the remainder
print(3**2) #9, ** preforms exponential power
print(15//2) #7, // preforms whole number division
print (5==2) #False, 5 does not equal 2 
print(10 != 10) # False, 10 is not not equal to 10
print (2<5) #True, 2 is less than 5
print (12>5) #True, 12 is greater than 5 
print (5<=6) #True, 5 is less than or equal to 6
print (1>=10) #False, 1 is not greater than or equal to 10 

x = 5 
x+=5
x-=4
x*=3
print(x)

#The and operator returns True if both sides are True. bool(True and True) returns True and bool(False and False) returns False. 
#The or operator returns True if at least one side is true. bool(True or False) returns True and bool (False or False) returns False. 
#The operator not flips the value of what it should be. bool(not False) returns True and bool(not True) returns False. 

#The / is the common division and the // gives the whole number division instead of specific value. 
#The % is the remainder of the division an the // gives how many times the whole number fits into the other number.
#I would use the % operator to calculate the remainder of the two numbers. 11%5 would be 1.
#Assignment operators work by updating and modifying the assigned variable using operations. 

my_string = "hello"
print(my_string) #prints: hello
print (my_string[0]) #prints:h
print (my_string[1]) #prints:e
print (my_string[2]) #prints:l
print (my_string[3]) #prints:l
print (my_string[4]) #prints:o
print (my_string[-1]) #prints:o
print (my_string[1:3]) #prints:el
print (my_string[0:5:2]) #prints:hlo 
print (len(my_string)) #prints: 5
print(my_string + " goodbye") #prints: hello goodbye
print ((my_string + " ")*7) #prints:hello hello hello hello hello hello hellod

#The string is sliced in my_string[1:3] and my_string [0:5:2]. 
name = "Oski"
print ("Hello, my name is", name)
#This prints Hello, my name is Oski 
name = "Oski"
print(f"Hello, my name is {name}")
#This prints Hello, my name is Oski
#The difference between the two is that the commas seperate out the first one and combines it and the second one uses an f-string which substitutes directly in the {}. 

#cd
#Changes directories. Use it to move from one folder to another. 
#Example: cd desktop 

#ls
#lists the files and folders in current directory.
#Example: ls  

#ls-a 
#Lists all files including the hidden ones 
#Example: ls-a  

#mkdir 
#Creates new directory under the current directory you are in
#Example: mkdir yourname

#cat
#Displays the contents of a file in terminal 
#Example: cat files.py 

#pwd
#prints the working directory or the current one
#Example: pwd 

#cd.. 
#moves up one directory closer to the parent folder
#Example: cd .. 

#cd . 
#refrences the current directory you are in
#Example: cd . 

#cd ∼ 
#moves to the home directory
#Example: cd ∼

#cp
#copies files from location to the next 
#cp file.py file2.py

#mv
#renames a directory
#Example: mv file.py file2.py

#rm
#deletes a file
#Example: rm file.py

#clear
#clears the terminal screen on device 
#Example: clear 

#grep
#searches for specific text inside files 
#Example: grep "hello world" file.py 

#nano: opens a file that you can edit it ex: nano file.py 
#touch: creates a new, empty file ex; touch file2.py
#echo: prints text to file ex: echo "Hello World"

#ls and ls-a both show files but ls only shows visible files while ls-a shows all files including hidden ones
#A hidden file have typically settings and data in files. 
#ls-l: shows files in long format ex: ls-l
#rm-r: deletes contents in a directories ex: rm-r file.py
#cat-n: numbers the output lines in a file ex:cat-n file.py 
