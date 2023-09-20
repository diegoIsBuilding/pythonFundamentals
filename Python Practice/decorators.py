#Decorators 
#A decorator is a special type of function - that changes the behaviour of
#another function - a decorator takes a function as an argument - and returns
#a new function

#Basic Example
#Time how long it takes a function to run. (This can be done with a decorator)
#
#Create a function that we can decorate 
import time ### We import the time module to record time ###
#This is the decorator function
def timer_decorator(func): ### Define a decorator - that takes func as an argument
    def wrapper():
        start_time = time.time() #This records the start time
        func() #Calls the original function
        end_time = time.time() #Records the end time
        print(f'Elapsed time: {end_time - start_time}') #Prints the elapsed time (end minus start)
    return wrapper

@timer_decorator
def my_function():
    print('Executing my_function!')
    
