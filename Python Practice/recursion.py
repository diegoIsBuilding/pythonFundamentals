#Recursion
#In python a defined function can call itself
#This is a common mathematical and programming concept
#The benefit is that you can loop through data to reach a desired result
#Double Edged Case: a dev can accidently write a function which never terminates
#and uses excessive amounts of memory or processor power
#When written correctly can be very efficient 

#Example
def factorial(n): #The function is named factorial and takes a parameter 'n' 
    if n == 1: return 1 #base case - the function checks if n is equal to 1
    #the base case is necessary to eventually stop the recursion
    
    return n * factorial(n-1) #recursive case - if n is not 1 the function
#returns 'n * factorial(n-1)' --> the function is calling itself with a smaller number
#THe function will keep doing this going down by 1 until it reaches the base case


print(factorial(10))