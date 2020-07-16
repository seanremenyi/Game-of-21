import random

cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K"]
suits = ["♠", "♥", "♣", "♦"]

def decks():
    deck = []
    idv_card = 0
    for card in cards:
        for suit in suits:
            idv_card = str(card) + str(suit)
            deck.append(idv_card)
    return deck

def hands_dealt(deck):
    hand = []
    count = 0
    while count < 2:
        hand.append(random.choice(deck))
        deck.pop(deck.index(hand[-1]))
        count+=1
    return hand 

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

def check_aces(hand):
    count = 0
    for items in hand:
        if items[0]=="A":
            count+=1
    return count

def only_values(hand):
    num_values = []
    for items in hand:
        num_values.append(value(items))
    return num_values 

def hand_total(hand):
    total = 0
    get_values = only_values(hand)
    for items in get_values:
        total += items
    return total

def draw_card(hand, deck):
    hand.append(random.choice(deck))
    deck.pop(deck.index(hand[-1]))
    return hand

def winner(comps, users):         
    if comps > users:
        print("Dealer win")
        return 0,1
    elif comps_total < users_total:
        print("You win")
        return 1,0
    else:
        if len(comps_hand) > len(users_hand):
            print("You win")
            return 1,0
        else:
            print("Dealer win")
            return 0,1



