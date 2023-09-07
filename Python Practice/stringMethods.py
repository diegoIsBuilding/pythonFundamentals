#Python has a set of built in methods that can be used on strings
weird_string = 'cattywampus'
weird_string2 = 'CATTYWAMPUS'
weird_string3 = 'special person'
print(weird_string.capitalize()) #converts the first character to upper case
print(weird_string2.casefold()) #converts string into lower case
print(weird_string.lower()) #converts a string to lower case
print(weird_string3.title()) #capitalizes the first letter in each word
print(weird_string2.islower()) #checks if all the charaters are lower case - in this case returns False

# isalpha()	Returns True if all characters in the string are in the alphabet
# index()	Searches the string for a specified value and returns the position of where it was found
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rsplit()	Splits the string at the specified separator, and returns a list
# split()	Splits the string at the specified separator, and returns a list
# swapcase()	Swaps cases, lower case becomes upper case and vice versa

#all these methods return a new altered/modified string. They do not alter or modify the original string


### ESCAPING CHARACTERS ###
quote = "\"May the Force be with you\" - Star Wars, 1997"
print(quote)

#Other Methods - Using single and double quotes
quote2 = '"The greats never sacrifice the important for the urgent. \nThey handle the immdiate problem and still make sure to secure teh future" \n- Bobby "Axe" Axelrod'
print(quote2)
