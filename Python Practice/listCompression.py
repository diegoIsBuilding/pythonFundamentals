#List Compression 
#List compression offers a shorter syntax when you want to create 
#a new list based on the values of an existing list

#Essentially list compreshions are simpler and sometimes prefered over loops
#Example
numbers = [1, 2, 3, 4, 5]
numbersPowerOf2 = [n**2 for n in numbers] #This was written in one line
print(numbersPowerOf2)

#Example of raising a number to the power 2 with a loop
numbersPowerOf2 = []
for n in numbers:
    numbersPowerOf2.append(n**2)

#Example with the map function
numbersPowerOf2 = list(map(lambda n : n**2, numbers))
