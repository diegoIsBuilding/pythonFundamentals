#Map(), Filter(), Reduce()

#The map() function executes a specified function for each item in an iterable. 
#The item is sent to the function as a parameter 

#Example you can pass in a list, dictionary, or object and function will
#change each item in the function and return a new list

#Example
#The list we are working with
numbers = [1, 2, 3]

#The double function - take a number and mulitplies it by 2
def double(a):
    return a * 2

#The result variable will contain the new list of numbers that were multiplied
#The map() function - runs the double function on each item in the numbers list

result = map(double, numbers)
print(result) #Returns a map object: <map object at 0x10e477040>
print(list(result)) #Returns a list of [2, 4, 6]

#This can also be done with lambda functions
doubleLamb = lambda a : a * 2
resultLamb = map(doubleLamb, numbers)
print(list(resultLamb))

#Now I wonder if i can write the function directly in the map funtion
#Answer is no

###Filter
filterNumbers = [4, 5, 6, 7]

def isEven(n):
    return n % 2 == 0 #When the number is divided by 2 and returns a remained of 0
#it returns true and that num
#any even number is going to be added to the resutFilter list and any odd 
#will not be added

#this can also be done with a lambda function

resultFilter = filter(isEven, filterNumbers)
print(list(resultFilter))
resultFilterLambda = filter(lambda a : a % 2 == 0, filterNumbers)
print(list(resultFilterLambda))

###Reduce()
#The for/in loop works similar to the reduce function
expenses = [
    ('Dinner', 89),
    ('Oil Change', 169)
]

sum = 0
for expense in expenses:
    sum = sum + expense[1]
    
    print(sum)
    
#Rewrite the function using the reduce() function
#REduce can only be used from functools library
from functools import reduce

sumReduce = reduce(lambda a, b: a[1] + b[1], expenses)
print(sumReduce)