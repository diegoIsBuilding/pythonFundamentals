#Docstrings
#Python documentation strings or docstrings provide a convenient way
#of associatign documentation with python modules, functions, 
# classes, and methods

'''
Dog Module

This module does... and provides the following class:
-Dog

'''
class Dog:
    '''A class representing a dog'''
    def __init__(self, name, age):
        '''Initialize a new dog'''
        self.name = name
        self.age = age
        
    def bark(self):
        '''Let the dog bark'''
        print('Woof Woof!')
        
        
print(help(Dog))