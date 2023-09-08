#done = True
done = False
if done:
    print('Yes')
else:
    print('No')
    
#Numbers are always true except for Zero 
#Zero is considered falsy (Even a negative number is considered a truthy)
zero = 0
some_number = -227
if zero:
    print('This is a truthy')
else:
    print('Zero is a falsy value')

if some_number:
    print('This is a truthy')
else:
    print('Zero is a falsy value')
    
#Strings are always true except for when empty
full_string = 'Daisy'
empty_string = ''

if empty_string:
    print(f'The string has the following content [{full_string}]')
else: 
    print('An empty string is a falsy value')
    
if full_string:
    print(f'The string has the following content [{full_string}]')
else: 
    print('An empty string is a falsy value')
    
#Checking if True or False are booleans

checkType = True
print(type(checkType)) #Prints ---> <class 'bool'>
print(type(checkType) == bool) #Prints ---> True

#Example code: any() function
book_one_read = True
book_two_read = False
#any() - This function checks if any item in a list is True
#If nothing in the list is true then it will return False
#If list or object is empty the any() function will also return False
read_any_book = any([book_one_read, book_two_read])
#The function will check if any of the books were read 
#Since book one was read (True) - the variable read_any_book will be assigned the value True

#Example code: all() function
ingredients_purchased = True
meal_cooked = False

#The all() function checks if all items in a list are True
#otherwise it will return False
#in this case since all food items were purchased but the meal hasnt been cooked then 
#the meal is not ready to serve
#So the all() function will return False and assign the value false to ready_to_serve
ready_to_serve = all([ingredients_purchased, meal_cooked])