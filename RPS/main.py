#import the random library
import random

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
    #Get an input by the user by using the 
    #input function --> input()
    player_choice = input('Enter a choice (rock, paper, scissors)')
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    choices = {
    'player': player_choice,
    'computer': computer_choice
}
    return choices
#create a function to check the winner
#pass in two pieces of information
def check_win(player, computer):
    #Example Str Concat
    print(f"You chose {player} and the computer chose {computer}.")
    #if statement will check if a statement is true
    #in this case who is the winner
    if player == computer:
        return("It's a tie!")
    # Create an elif statement to check alternative outcomes
    elif player == 'rock' and computer == 'scissors':
        return('Rock Smashes Scissors! You Win!')
    elif player == 'rock' and computer == 'paper':
        return('Paper beats rock! You Lose!')
    
    # Refactor the if/elif/else statement above
    elif player == 'rock':
        if computer == 'scissors':
            return('Rock Smashes Scissors! You Win')
        else:
            return('Paper covers Rock! You Lose!')
    elif player == 'paper':
        if computer == 'rock':
            return('Paper covers Rock! You Win!')
        else:
            return('Scissors cuts paper! You Lose!')
    elif player == 'scissors':
        if computer == 'paper':
            return('Scissor cuts paper! You Win!')
        else:
            return('Rock smashes Scissors! You Lose!')
#The following variable is going to return a dictionary
#How to access a specific element in a dictionary

choices = get_choices()
result = check_win(choices['player'], choices['computer'])
print(result)
    
#check_win("rock", "paper")
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


#choices = get_choices()
#print(choices)

#Dictionaries
#These are like objects in javascript 
#Used to store data values in key:value pairs
#They are changeable and do NOT allow duplicates
#Example
#choices = {
#    'player': player_choice,
#    'computer': computer_choice
#}

#Lists
#Lists are like arrays in javascript
#Example: food = ['pizza', 'carrots', 'hamburgers', 'donuts']
#use the 'random' library to get a food item from the 
#food list
#Example: snack = random.choice(food)

#Example: If Statement 
# a = 3
# b = 5
# if a < b:
# print("Yes")

#Example f-String
#f strings make it easier to add python variables and expressions inside of strings
#age = 25
#print(f"Jum is {age} years old.")

#Example of Else and Elif Statments
#If/Else Statement
# age = 20
# if age >= 18:
#   print('You are an adult')
# else:
#   print('You are not an adult)

#Elif Statement
# age = 20
# if age >= 18:
# print('You are an adult')
# elif age > 12:
#   print('You are a teenageer')
# elif age > 1:
#   print('You are a child')
# else:
#   print('You are a baby')

#Accessing a Specific Element in a Dictionary
#Example
#choices = {'player': 'rock', 'computer': 'paper'}

#You can access the items of a dictionary by referring to its key name inside of square brackets
#Example below

#player_choice = choices['player']