conditionOne = True
conditionTwo = False

print(not conditionOne) #Basically saying NOT TRUE which is equal to FALSE
print(not conditionTwo) #Vice Verse - saying NOT FALSE which is equal to TRUE

print(conditionOne and conditionTwo) #Using the "AND" - this will only return true if both conditions are true
                                     #Since one of the conditions is false it returns false
print(conditionOne or conditionTwo)  #This will return true if one of the conditions is TRUE

#More of the OR operator
#Since the OR operator returns the first value that is NOT A FALSY value
print(0 or 1) #0 is a Falsy value and so it returns 1
print(False or 'Hola') #Since the first value is false it will return "Hola"
print('Hola' or 'Bienvenido') #Since the first value is a truthy it will return 'Hola"
print([] or False) #Since the first value is a falsy (empty bracket) it will return the second condition
print(False or []) #Since the first value is False it returns the second condition []