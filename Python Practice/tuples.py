#Tuples - Python Data structure - immutable groups of objects
#Can not add or remove items from a list
tupleExample = ('Daisy', 'Rose', 'Tulip')
#Can get its values by referencing an index
print(tupleExample[0]) #Returns Daisy
print(tupleExample.index('Daisy')) #Returns 0

if "Daisy" in tupleExample:
    print('Yes!')
else: 
    print('No!')
    
#Create new tuple by using the + operator
newExampleTuple = tupleExample + ('Sunflower', 'Dandelion')
print(newExampleTuple)

#Cannot add or remove items from tuples

#newExampleTuple.pop()
#print(newExampleTuple) #Returns - AttributeError: 'tuple' object has no attribute 'pop'
#print(newExampleTuple.append('Hi')) AttributeError: 'tuple' object has no attribute 'append'
