#Loops
#In python there are two types of loops 
#For Loops
#While Loops

#While Loops
#They use the while keyword and repeat the block of code until the conditon
#is met
#Example
condition = True 
while condition == True:
    print('This condition is true')
    #The while loop stops once the condition changes or meets a certain criteria
    #For this case after the first iteration the conditon changes to false
    #and the loop only runs once
    condition = False
    
#Example While Loop + Counter
count = 0 #count starts at 0
while count < 10: #since the value of count is less than 10 - print the 
    #following statement
    print('The condition is True') #This will print until the count reaches
                                    #the condition
    count = count + 1 #after each iteration the count is incremented by 1
#After count reaches 10 iterations the following statement prints
print('This prints after the loop reaches the count max/limit')

#For Loops
#We can tell python to iterate over a sequence (list, tuple, dictionary, a set, a string)
#With a for loop you use the FOR keyword to execute a set of statements once for each item in a sequencce 
#Example
items = [1, 2, 3, 4, 5] #This is the sequence python will go through
for item in items: #We are telling python to do some action for each item in the items list
    print(f'Print each item {item}') #The loop ends up printing an each item until it has gone through the entire list of items
    
#Example - Range 
#The range() function returns a sequence of number starting from 0 by default
#And increments by 1 and ends at a specific number
for x in range(15):
    print(x + 1) #Prints 1 through 15
    print(x) #prints 0 through 14
    
#Example - Enumerate
#The enumerate() function adds a counter/index as the key of the enumerated object
numberItems = [1, 2, 3, 4, 5]
for index, number in enumerate(numberItems):
    print(index, number)