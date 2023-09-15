#Classes
#From classes objects can be instantiated
#A class is the type of an object
#Example: Create a class Dog using the 'class' keyword

#Inheritence 
class Animal:
    def walk(self):
        print('Walking...')
#Adding parentheses next to the Dog class and adding Animal as parameter 
#Will inherit properties of the Animal class
class Dog(Animal):
    #Create a constructor using __init__
    def __init__(self, name, age):
        self.name = name
        self.age = age
    #Add method to the class by using the def keyword
    def bark(self):
        print('Woof!')
#Create a dog named roger    
roger = Dog('Roger', 8)
print(roger.name) #Returns - 'Roger
print(roger.age) #Returns - '8'
roger.bark() 
roger.walk() #Roger inherited the walking property from the Animal class
print(type(roger)) #Returns - '<class '__main__.Dog'>

