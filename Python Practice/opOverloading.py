#Operator Overloading

class Dog: 
    '''The Dog Class'''
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    def __gt__(self, other):
        return True if self.age > other.age else False
        pass
    
roger = Dog('Roger', 8)
syd = Dog('Syd', 7)
print(roger > syd)