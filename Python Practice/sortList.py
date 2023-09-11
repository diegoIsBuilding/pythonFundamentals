randomList = ['Hi', 'Hola', 'Nin Hao', 'Koonichiwa', 'Anyeonghaseyo', 
              'Bonjour', 'Salve']
#Sort the random list using the sort() method
randomList.sort()
print(randomList) #Returns - ['Anyeonghaseyo', 'Bonjour', 'Hi', 'Hola', 'Koonichiwa', 'Nin Hao', 'Salve']
#The strings are in alphabetical order 
#Sort method sorts uppercase letter first then lower case
#Sort by alphabetical order regardless of capitalization key=str.lower
randomListTwo = ['Hi', 'Hola', 'Nin Hao', 'Koonichiwa', 'Anyeonghaseyo', 
              'Bonjour', 'Salve', 'a random string', 'dolphin', 'halo']
randomListTwo.sort(key=str.lower)
print(randomListTwo) #Returns the following string - ['a random string', 'Anyeonghaseyo', 'Bonjour', 
# 'dolphin', 'halo', 'Hi', 'Hola', 'Koonichiwa', 'Nin Hao', 'Salve']

#Copy the original randomList
randomListCopy = randomList[:] #Return the original list

#Sort a list without returning a new list
#use the sorted() function - pass in two parameter
#first the list and second it the way to sort
print(sorted(randomListTwo, key=str.lower))
