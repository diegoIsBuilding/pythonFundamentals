#Step 1 - Create a variable of suits, rank, and value - Hearts, K, and 10
#Then print the # values
import random

cards = []
suits = ['hearts', 'spades', 'diamonds', 'clubs']
ranks = [
    {'rank': 'A', 'value': 11},
    {'rank': '2', 'value': 2},
    {'rank': '3', 'value': 3},
    {'rank': '4', 'value': 4},
    {'rank': '5', 'value': 5},
    {'rank': '6', 'value': 6},
    {'rank': '7', 'value': 7},
    {'rank': '8', 'value': 8},
    {'rank': '9', 'value': 9},
    {'rank': '10', 'value': 10},
    {'rank': 'J', 'value': 10},
    {'rank': 'Q', 'value': 10},
    {'rank': 'K', 'value': 10},
]
for suit in suits:
    for rank in ranks:
        cards.append([suit, rank])
        
def shuffle():
    random.shuffle(cards)
    
def dealCard(number):
    cardsDelt = []
    for x in range(number):
        card = cards.pop()
        cardsDelt.append(card)
    return cardsDelt
    
shuffle()
card = dealCard(1)[0]
print(card[1]['value'])









'''cardsDelt = dealCard(2)
card = cardsDelt[0]
rank = card[1]

if rank == 'A':
    value = 11
elif rank == 'J' or rank == 'Q' or rank == 'K':
    value = 10
else:
    value = rank
    
    
rank_dictionary = {
    'rank': rank, 
    'value': value
}'''




#Neet trick: double click variable name and press CMD + D 
#This selects all the same variables and can type on diff lines

