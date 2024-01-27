#!/usr/bin/env python
# coding: utf-8

# # BlackJack
# Below is an implementation of a simple game of Blackjack using core python

# IMPORT STATEMENTS AND VARIABLE DECLARATIONS:

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

playing = True

# CLASS DEFINTIONS:

class Card:
    
    def __init__(self,suit,rank):
        """
        This function is an constructor and initializes two attributes `self.suit`
        and `self.rank` with the given parameters `suit` and `rank`.

        Args:
            suit (str): The `suit` input parameter sets the value of the object's
                `suit` attribute.
            rank (int): The `rank` input parameter determines the value of the card.

        """
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        """
        This is a Python method defined for a class (not shown) that returns a
        string representation of the object.

        Returns:
            str: The output returned by this function is the string representation
            of the card object: the rank followed by "of" followed by the suit.

        """
        return self.rank + 'of' + self.suit
    

class Deck:
    
    def __init__(self):
        """
        This function defines a constructor for a class named `CardDeck` that
        initializes the deck with a list of all possible cards (suits x ranks).

        """
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
                
    def __str__(self):
        """
        This function defines a method (i.e., an special behavior) for objects of
        the class `Deck` to output themselves as a string. It creates an empty
        string and appends to it the print string of each `Card` object contained
        within the `deck`.

        Returns:
            str: The output returned by this function is:
            
            "The deck has:
            
            ..."
            
            Where the dots represent multiple blank lines and each Card object's
            print string.

        """
        deck_comp = ''  # start with an empty string
        for card in self.deck:
            deck_comp += '\n '+card.__str__() # add each Card object's print string
        return 'The deck has:' + deck_comp
                
    def shuffle(self):
        """
        The function "shuffle" randomizes the order of the cards within the deck.

        """
        random.shuffle(self.deck)
        
    def deal(self):
        """
        This function called `deal` takes no argument and it removes one card from
        the `deck` attribute of the object it's defined on.

        Returns:
            : The output returned by the function is a single card from the deck.

        """
        single_card = self.deck.pop()
        return single_card
    

class Hand:
    
    def __init__(self):
        """
        This function defines an initializer method for an object of the class Hand.

        """
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        """
        This function adds a card to a hand object and updates the hand's value
        and aces count based on the card's rank.

        Args:
            card (dict): The `card` input parameter passes a single card object
                to the function and stores it at the end of the list within the
                class attribute.

        """
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1  # add to self.aces
    
    def adjust_for_ace(self):
        """
        This function decreases the value of the object by 10 if the current value
        is greater than 21 and the object has an Ace card.

        """
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
            

class Chips:
    
    def __init__(self):
        """
        This function is an object constructor (i.e.

        """
        self.total = 100
        self.bet = 0
        
    def win_bet(self):
        """
        The `win_bet` function increases the value of the `total` attribute of the
        object by the amount of the `bet` attribute.

        """
        self.total += self.bet
    
    def lose_bet(self):
        """
        This function subtracts the value of `bet` from `total`.

        """
        self.total -= self.bet
        

# FUNCTION DEFINITIONS:

def take_bet(chips):

    """
    This function repeatedly prompts the user to input a number of chips to bet
    until a valid integer is entered. If the user enters a non-integer value or a
    bet greater than their current total number of chips. it prints an error message
    and tries again.

    Args:
        chips (dict): The `chips` input parameter is used as a reference to the
            current player's chip stack and is modified within the function by
            setting its `bet` attribute to the integer value entered by the user.

    """
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except ValueError:
            print('Sorry, a bet must be an integer!')
        else:
            if chips.bet > chips.total:
                print("Sorry, your bet can't exceed",chips.total)
            else:
                break

def hit(deck,hand):
    """
    This function adds the top card from a deck to a player's hand and adjusts the
    hand's value if an Ace is drawn.

    Args:
        deck (): In the given function `hit`, the `deck` input parameter is used
            to pass a deck of cards to be shuffled and dealt.
        hand (list): The `hand` parameter is modified within the function;
            specifically `hand.add_card(deck.deal());`.

    """
    hand.add_card(deck.deal())
    hand.adjust_for_ace()
    
def hit_or_stand(deck,hand):
    """
    This function allows the player to choose whether to hit or stand after receiving
    their initial hand of cards. It repeatedly prompts the player for a choice
    until they enter a valid response (either "h" for hit or "s" for stand).

    Args:
        deck (): The `deck` input parameter passed to the `hit_or_stand()` function
            is not used or referenced within the function at all.
        hand (list): The `hand` parameter is the current hand of cards held by the
            player.

    """
    global playing
    
    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")
        
        if x[0].lower() == 'h':
            hit(deck,hand)  # hit() function defined above

        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False

        else:
            print("Sorry, please try again.")
            continue
        break

    
def show_some(player,dealer):
    """
    This function takes two arguments `player` and `dealer` and prints the cards
    they hold.

    Args:
        player (): The `player` input parameter passes the player's hand of cards
            to the function as a list of card objects.
        dealer (): In the given function `show_some(player , dealer)`, the `dealer`
            input parameter is passed by the caller to display information about
            the dealer's hand during the game.

    """
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    
def show_all(player,dealer):
    """
    The `show_all` function prints the values of both players' hands (Dealer and
    Player). It uses *unpacking to print the cards as strings separated by newlines
    (`sep='\n '`).

    Args:
        player (): The `player` input parameter is passed to the `show_all()`
            function and it is used as a variable name to reference the player's
            hand of cards.
        dealer (): The `dealer` input parameter is passed to the `show_all()`
            function and is used to display information about the dealer's hand
            alongside the player's hand.

    """
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)
    
def player_busts(player,dealer,chips):
    """
    The `player_busts()` function prints a message indicating that the player has
    busted and then calls the `lose_bet()` method on the `chips` object to deduct
    the bet amount from the player's balance.

    Args:
        player (int): The `player` input parameter passes the player's hand (i.e.,
            their cards) to the function for bust checking.
        dealer (None): The `dealer` input parameter is not used within the
            `player_busts()` function at all.
        chips (dict): The `chips` input parameter is used to deduct the losing bet
            amount from the player's balance after they bust.

    """
    print("Player busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    """
    This function prints "Player wins!" and calls the `win_bet` method on the
    `chips` object.

    Args:
        player (str): The `player` input parameter passes a reference to the player
            object that will receive the win notification and have their chips updated.
        dealer (): The `dealer` input parameter represents the dealer's hand (or
            card) that is being compared to the player's hand.
        chips (): The `chips` input parameter is used to call the `win_bet()`
            method on the `chips` object when the player wins.

    """
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    """
    The `dealer_busts` function prints "Dealer busts!" and calls the `win_bet`
    method on the `chips` parameter to award the player the winnings when the
    dealer's hand busts.

    Args:
        player (None): The `player` input parameter is not used within the function
            `dealer_busts`.
        dealer (): The `dealer` input parameter is used to pass the dealer's hand
            to the function.
        chips (): The `chips` input parameter is used to call the `win_bet()`
            method of the `chips` object to give the player their winnings when
            the dealer busts.

    """
    print("Dealer busts!")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    """
    The `dealer_wins()` function prints "Dealer wins!" and causes the `chips`
    object to lose their bet.

    Args:
        player (int): The `player` input parameter represents the player's hand
            or bets placed during the game.
        dealer (int): The `dealer` input parameter passes a reference to the
            dealer's hand as a playing card object.
        chips (): The `chips` input parameter is used to represent the player's
            bet and is modified within the function to reflect the loss of the bet
            when the dealer wins.

    """
    print("Dealer wins!")
    chips.lose_bet()
    
def push(player,dealer):
    """
    This function prints "Dealer and Player tie!" when it is called with arguments
    'player' and 'dealer', indicating a "push" result.

    Args:
        player (): The `player` input parameter is not used anywhere within the
            code of the function.
        dealer (): In the `push()` function above (defined using the Python `def`
            statement), the input parameters `player` and `dealer` both have a
            null value (represented by `<undefined>`), which means that neither
            is being passed any argument values.
            
            So the effect of calling the `push()` function as `push( player )`
            will be the same as if no arguments were passed at all. In this case:
            The statement inside the body of the function "Dealer and Player tie!"
            etc.) gets executed with none of the parameters being used.

    """
    print("Dealer and Player tie! It's a push.")
    
# GAMEPLAY!

while True:
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n    Dealer hits until she reaches 17. Aces count as 1 or 11.')
    
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    
    # Set up the Player's chips
    player_chips = Chips()  # remember the default value is 100
    
    # Prompt the Player for their bet:
    take_bet(player_chips)
    
    # Show the cards:
    show_some(player_hand,dealer_hand)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player_hand)
        show_some(player_hand,dealer_hand)
        
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break
    
    # If Player hasn't busted, play Dealer's hand        
    if player_hand.value <= 21:
        
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)
            
        # Show all cards
        show_all(player_hand,dealer_hand)
        
        # Test different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)

        else:
            push(player_hand,dealer_hand)

    # Inform Player of their chips total    
    print("\nPlayer's winnings stand at",player_chips.total)
    
    # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("Thanks for playing!")
        break






