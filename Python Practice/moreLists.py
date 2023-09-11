#Lists lesson
exampleListOne = ['Daisy', 'Rose', 'Milo', 1, 2, 'Oppenheimer', True, False]
#Check if an item is in a list with the in operator
if 'Daisy' in exampleListOne:
    print('Yes!')
else:
    print('No!')
    
exampleListTwo = []
#Check if the list has items or if empty
#An empty list is a falsy value
if exampleListOne == True:
    print('The list has items!')
else:
    print('It is empty...')

#Reference Items in a list - use brackets and the first items index value 
#is 0 and the last item can be reached by using -1
#print(exampleListOne[0]) #Prints Daisy
#print(exampleListOne[5]) #Prints Oppenheimer
#print(exampleListOne[-1]) #Prints False

#Update the Index 4 with a new string
exampleListOne[4] = "This index point has been updated"
#print(exampleListOne)

#SLICING a list by indicating where to start and where to end with a colon
#Ex: list[3:7] - This will select every item from the 3 to 7 index except
#the 7th index itself
#print(exampleListOne[3:6])
#Slice the list from the start to the 3rd index point
#print(exampleListOne[:4])

#Using the len() function will show how many items are in a list
#print(len(exampleListOne))

#Can add items to a list by using the append method
exampleListOne.append('This has been appended to the end of the list')
#print(exampleListOne)

#The extend() method is also another way to add items to a list
#Combine two lists together using the extend() method
newList = [1,2,3,4,5]
exampleListOne.extend(newList)  #The exampleListOne is being extended with
                                #the newList list
#print(exampleListOne)

#A list can be extended / added to another list by using the += operator
newNewList = ['on', 'off']
exampleListOne += newNewList
#print(exampleListOne)

#If you forget to add the brackets to the new list
#The += operator will add each letter or number as a
#new item in the list
wonkyList = 'dog'
exampleListOne += wonkyList
#print(exampleListOne) #The last three items are 'd','o','g'

#Items from a list can be removed by using the remove() method
#Remove 'd','o','g'
#Error - the remove() method only take one arguement
exampleListOne.remove('d')
exampleListOne.remove('o')
exampleListOne.remove('g')
#print(exampleListOne)

#The pop() method removes the last item on the list and returns the last item
popElement = exampleListOne.pop()
#print(popElement) #Returns 'Off'
#print(exampleListOne)

#Items can be instered into different points of a list
#Insert a new item at index 1
exampleListOne.insert(1, 'This item was added to the list using the insert() method')
#print(exampleListOne)
#To add multiple items at a specific index uses slices - ex: list[1:1]
#Create a new list with random items
#Add a list of elements at index 3 
exampleSlicingList = [1,2,3,4,5]
sliceInList = ['Add','with','slicing']
exampleSlicingList[3:3] = sliceInList
print(exampleSlicingList)