#Variable
#Created a variable called player_choice and 
#assigned the string 'rock' to it
#   player_choice = 'rock'
#Create a variable named computer_choice and 
#assign a string 'paper' to it
#   computer_choice = 'paper'

#Note: A function is a set of code that only runs
#When it is called 

#Note: Indentation is important in python

#Define (def) a function named get_choices
def get_choices():
    player_choice = 'rock'
    computer_choice = 'paper'
    choices = {
    'player': player_choice,
    'computer': computer_choice
}
    return choices

#Example Function
#def greeting():
    #return 'Hi'

#To call the function you write the name of the function
#followed by parenthesis
#greeting()

#A function can also be assigned to a variable
#Example:
#response = greeting()
#Then print the varible to get the string in the
#function greeting()
#print(response)
#returns the string 'Hi'


choices = get_choices()
print(choices)

#Dictionaries
#These are like objects in javascript 
#Used to store data values in key:value pairs
#They are changeable and do NOT allow duplicates
#Example
#choices = {
#    'player': player_choice,
#    'computer': computer_choice
#}