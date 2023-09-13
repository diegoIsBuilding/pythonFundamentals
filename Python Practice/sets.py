# Sets
nameSetOne = {'Roger', 'Syd', 'Daisy', 'Rose'}
nameSetTWo = {'Rose'}

intersect = nameSetOne & nameSetTWo
print(intersect) #Returns 'Rose' both sets have the string 'Rose'

mod = nameSetOne | nameSetTWo
print(mod) #Returns 

differenceInSets = nameSetOne - nameSetTWo
print(differenceInSets)

#Subset
subSetOne = nameSetOne > nameSetTWo
subSetTwo = nameSetOne < nameSetTWo
print(f'This is subSetOne {subSetOne}') #Does one set have everything in another set
print(f'This is subSetOne {subSetTwo}') #Does one set have everything in another set

#Sets can be converted to lists with list() method
convertSetToList = list(nameSetOne)
print(convertSetToList)

#A set can cannot have duplicates 