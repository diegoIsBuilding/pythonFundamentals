#Step 1 - Create a variable of suits, rank, and value - Hearts, K, and 10
#Then print the # values
''' This module will be used later to shuffle the deck '''
import random

''' The 'Card' class represents indvidual playing cards with suits and ranks '''
class Card:
    ''' This constructor method is called when a 'Card' is created '''
    ''' The method take three parameters - self, suit, and rank '''
    ''' self - this refers to the instance of the object itself '''
    ''' suit - this refers to the suit of the card '''
    ''' rank - this refers to the rank of the card '''
    def __init__(self, suit, rank):
        ''' the self.suit and self.rank store the passed in values of suit and rank
            in the instance of the object '''
        self.suit = suit
        self.rank = rank
    ''' the __str__ method determines what should return when you try to 
        convert the object to a string or when you try to print it '''
    ''' the __str__ method will return a string representation of the card'''
    def __str__(self):
        ''' this fetches and returns the cards attributes
            self.rank["rank"] fetches the rank of the card
            self.suit directly fetches the suit of the card '''
        return f'{self.rank["rank"]} of {self.suit}'
        

''' The class named Deck will represent a standard 52 card deck '''
class Deck:
    ''' The __init__() method initializes a deck of cards '''
    def __init__(self):
        ''' A deck self.cards starts off as an empty list '''
        self.cards = []
        ''' suits is a list of the 4 card suits '''
        suits = ['hearts', 'spades', 'diamonds', 'clubs']
        ''' ranks is a list of dictionaries - each dictionary representing
            a card rank and its associated value '''
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
        ''' below is a nested loop - the deck is created by combining each
            each suit with each rank - making 52 cards'''
        
        ''' outer loop '''
        ''' this loop iterates over each suit item in the suits string list'''
        for suit in suits:
            ''' inner loop '''
            ''' for ever suit item in the outer loop - this inner loop
                iterates over each rank dictionary item in the ranks list '''
            for rank in ranks:
                ''' inside the inner loop - combine each suit item and rank
                    dictionary item - append this new list item to self.cards'''
                self.cards.append(Card(suit, rank))
    
    ''' The shuffle method randomizes the order of the cards in the self.cards deck '''
    def shuffle(self):
        ''' Conditional Check: this line checks the number of cards in self.cards deck
            by using the len() function - the shuffle operation will only happen 
            if there is more than one card in the deck - this is logical because you can not
            shuffle a deck with one or zero cards'''
        if len(self.cards) > 1:
            ''' if the statement above is true - then the random.shuffle funciton is called
            random is a python module - it randomizes the order of the items in a list'''
            random.shuffle(self.cards)
    
    ''' This method is designed to 'deal' a certain number of cards from the self.cards deck
        The number of cards dealt is determined by 'number argument - the cards are dealt from
        the top/end of the deck'''        
    def dealCard(self, number):
        ''' Initialize an empty list - cardsDelt = [] '''
        ''' The list will store the cards that are dealt - it is initally empty
        because the are no cards to deal '''
        cardsDelt = []
        ''' the for loop runs as many times as the 'number' argument indicates
            if the number is 2 it only deals two cards'''
        for x in range(number):
            ''' before dealing any cards the if statement checks it the 
                deck has any cards to deal - the are no cards it cant deal '''
            if len(self.cards) > 0:
                ''' the pop() method removes the top card from the self.card list
                    and returns it - this card is then store in the card variable 
                    - the deals one card from the top of the deck'''
                card = self.cards.pop()
                ''' The dealt card in the previous step is then stored in the
                    cardsDelt list - this keeps track of all the cards that have been 
                    dealt '''
                cardsDelt.append(card)
                ''' once the loop is complete and the specified number of cards 
                have been dealt the method then returns the 'cardsDelt' '''
        return cardsDelt

''' This defines the class of 'Hand' '''
class Hand:
    ''' Initialize the constructor method '''
    def __init__(self, dealer = False):
        ''' self.cards keeps track of cards in hand '''
        self.cards = []
        ''' self.value sets the value of the hand to 0 '''
        self.value = 0
        ''' self.dealer checks if the hand is for a dealer or player
            by default it is a players hand '''
        self.dealer = dealer
        
        ''' The add_card method allows you to add one or more cards to the hand
            It takes a lost of cards -> card_list and append them to self.cards '''
    def add_card(self, card_list):
        self.cards.extend(card_list)
        ''' The calculate_value method calculates the value of the hand based on
            on the cards it has - it starts by setting self.value to zero 
            and checking if there are any aces in the hand '''
    def calculate_value(self):
        self.value = 0
        has_ace = False
        ''' Goes through each card to get its value '''
        for card in self.cards:
            card_value = int(card.rank['value'])
            self.value += card_value
            ''' This method then checks if there is an Ace in the hand '''
            if card.rank['rank'] == 'A':
                has_ace = True
        ''' Then checks if the value of the hand is over 21 and has and Ace
            if it has and ace and value over 21 it then subtracts 10 '''
        if has_ace and self.value > 21:
            self.value -= 10
    
    ''' This method recalculates the value of the hand ''' 
    def get_value(self):
        self.calculate_value()
        return self.value
    ''' The method checks if the hand is a blackjack (a value of 21) 
        and returns True or False depending on the value '''
    def is_blackjack(self):
        return self.get_value() == 21
    ''' This method displays the hands cards and its value '''
    def display(self, show_all_dealer_cards=False):
        ''' If it is the dealers hand it shows the dealers hand '''
        if self.dealer == True:
            print('Dealers Hand: ')
        else: 
            ''' Otherwise it shows the players hand '''
            print('Your Hand: ') 
        ''' The dealers first card is hidden '''
        for index, card in enumerate(self.cards):
            if index == 0 and self.dealer and not show_all_dealer_cards and not self.is_blackjack:
                print('Hidden')
            else:
                ''' Unless the dealer has a blackjack or the game ends the first card is shown '''
                print(card)
        if not self.dealer:
            print('Value: ', self.get_value())
        print()
            
class Game():
    def play(self):
        game_number = 0
        games_to_play = 0
        
        while games_to_play <= 0:
            try:
                games_to_play = int(input('How many games do you want to play? '))
            except:
                print('Enter a number.')
        
        while game_number < games_to_play:
            game_number += 1
            
            deck = Deck()
            deck.shuffle()
            
            player_hand = Hand()
            dealer_hand = Hand(dealer=True)
            
            for i in range(2):
                player_hand.add_card(deck.deal(1))
                dealer_hand.add_card(deck.deal(1))
            
            print()
            print('*' * 30)
            print(f'Game {game_number} of {games_to_play}')
            print('*' * 30)
            player_hand.display()
            dealer_hand.display()
            
            if self.check_winner(self.player_hand, dealer_hand):
                continue
            
            choice = ''
            while self.player_hand.get_value() < 21 and choice not in ['s', 'stand']:
                choice = input('Hit or Stand: ').lower()
                print()
                while choice not in ['h', 's', 'hit', 'stand']:
                    choice = input('Enter H/S or Hit/Stand').lower()
                    print()
                if choice in ['h', 'hit']:
                    self.player_hand.add_card(deck.deal())
                    player_hand.display()
                    
            if self.check_winner(player_hand, dealer_hand):
                continue
            
            player_hand_value = player_hand.get_value()
            dealer_hand_value = dealer_hand.get_value()
        
            while dealer_hand_value < 17:
                dealer_hand.add_card(deck.deal())
                dealer_hand_value = dealer_hand_value.get_value()
            
            dealer_hand.display(show_all_dealer_cards=True)
            
            if self.check_winner(player_hand, dealer_hand):
                continue
            
            print('Final Results')
            print(f'Player Hand: {player_hand_value}')
            print(f'Dealers Hand: {dealer_hand_value}')
            
            self.check_winner(player_hand, dealer_hand, True)
            
        print('\nThanks for playing')
        
    def check_winner(self, player_hand, dealer_hand, game_over=False):
        if not game_over:
            if player_hand.get_value() > 21:
                print('Bust! Dealer Wins!')
                return True
            elif dealer_hand.get_value() > 21:
                print('Dealer Bust! You Win!')
                return True
            elif player_hand.is_blackjack() == dealer_hand.is_blackjack():
                print('Theres a tie!')
                return True
            elif player_hand.is_blackjack():
                print('Blackjack! You Win!')
                return True
            elif dealer_hand.is_blackjack():
                print('Dealer has blackjack! Dealer Wins!')
                return True
        else:
            if player_hand.get_value() > dealer_hand.get_value():
                print('You Win!')
            elif dealer_hand.get_value() == player_hand.get_value():
                print('Tie')
            else: 
                print('Dealer Wins!')
            return True
        return False
                
                
        
g = Game()
g.play()
