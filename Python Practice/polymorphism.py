#Polymorphism
class Dog:
    def eat(self):
        print('Eating dog food')
        
class Cat:
    def eat(self):
        print('Eating cat food')
        
animalOne = Dog()
animalTwo = Cat()

animalOne.eat()
animalTwo.eat()


