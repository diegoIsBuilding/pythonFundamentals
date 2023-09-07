#String data type
name = 'Diego'
#Check the data type by using the type function
print(type(name) == str) #TRUE
#The result will return true because the string 'Diego' assigned to the variable name is a string

#The following code will use the isinstance() function to see if name is an instance of a string
#The following code will return true
print(isinstance(name, str)) #TRUE


#The number 26 is a data type of integer and is assigned the variable name 'age'
#Using the isinstance() function will show the age is an instance of an integer
age = 26
print(isinstance(age, int))#TRUE

#The following integer is a float because it has a decimal
example_age = 26.8
print(isinstance(example_age, float))#TRUE

#You can also convert an integer into a float by using the float function
print(float(age))#Returns 26.0

#You can also convert a string number into an integer by using the integer function int()
str_age = '26'
print(int(str_age))#Converts '26' -> 26

#This is a list of different data types
#bool for booleans
#list for lists
#tuple for tuples
#range for ranges
#dict for dictionaries
#set for sets
