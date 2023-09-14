#Objects
#Python is an object oriented programming language 
#Almost everything in python is an object with its prop and methods
#A class is like an object constructor - 'blueprint'

#create a simple class - thisClass with a property named - thisProperty
# use the class keyword
class thisClass:
    thisProperty = 'example property'
    
#Create an Object
#Now the the class named thisClass has been created we can create objects
#create an object named thisObject and print the value of thisProperty
thisObject = thisClass()
print(thisObject.thisProperty)

