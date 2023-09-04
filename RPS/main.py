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

    
    
check_win("rock", "paper")
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