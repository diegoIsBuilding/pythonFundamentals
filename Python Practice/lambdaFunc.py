#Lambda Functions
#lamnda functions are annonymous functions 
#These functions can take any number of arguments but can only have one
#expression
#it has to return a value
#simple version of a function
lambda num : num * 2

lambda a, b: a * b
#can not invoke directly but can be assigned to variables
multiply = lambda c, d: c * d
print(multiply(23, 4)) #returns 92
