import random
from termcolor import cprint

###Cards and Suits
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K"]
suits = ["♠", "♥", "♣", "♦"]
###Creates a list of each possible card
def decks():
    deck = []
    idv_card = 0
    try:
        for card in cards:
            for suit in suits:
                idv_card = str(card) + str(suit)
                deck.append(idv_card)
    except:
        print("uh oh, this is awkward, we've got no deck")
    return deck


###Deals out the hands randomly, simulating shuffling and removes the card from the deck to avoid doubles
def hands_dealt(deck):
    hand = []
    count = 0
    try:
        while count < 2:
            hand.append(random.choice(deck))
            deck.pop(deck.index(hand[-1]))
            count+=1
    except:
        print("uh oh, this is awkward, no hands?")
    return hand


###Returns the value of each card
def value(card):
    if card[0] == "A":
        return 1
    elif card[0] == "J":
        return 10
    elif card[0] == "Q":
        return 10
    elif card[0] == "K":
        return 10
    else:
        return int(card[0])

###Check for aces
def check_aces(hand):
    count = 0
    for items in hand:
        if items[0]=="A":
            count+=1
    return count

###Strip a hand from its suits return a list of only its values
def only_values(hand):
    num_values = []
    for items in hand:
        num_values.append(value(items))
    return num_values 

###Get the total of a hand using the only_values helper function
def hand_total(hand):
    total = 0
    try:
        get_values = only_values(hand)
        for items in get_values:
            total += items
        return total
    except:
        print("uh oh, this is awkward, what's our total?")
        return hand

###Draws a card from the deck and removes said card from the deck to avoid doubles
def draw_card(hand, deck):
    try:
        hand.append(random.choice(deck))
        deck.pop(deck.index(hand[-1]))
    except:
        print("uh oh, this is awkward, we can't seem to draw a card")
    return hand

###Declares winner and displays on screen and adds points to the total score
def winner(comps, users, comps_hand, users_hand):         
    try:
        if comps > users:
            cprint("Dealer win", "red", "on_yellow")
            return 0,1
        elif comps < users:
            cprint("You win", "red", "on_yellow")
            return 1,0
        else:
            if comps==users:
                if len(comps_hand) > len(users_hand):
                    cprint("You win with less cards", "red", "on_yellow")
                    return 1,0
                else:
                    cprint("Dealer wins with less cards", "red", "on_yellow")
                    return 0,1
            else:
                cprint("Nothing lost, Nothing gained, its a tie", "red", "on_yellow")
                return 0,0
    except:
        print("uh oh, this is awkward, looks like we won't know who won?")


