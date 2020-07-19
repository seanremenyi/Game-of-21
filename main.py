#! /usr/sbin/python

import cards_and_deck
import drawings
from termcolor import cprint
import os
import sys
import extras






####Dealer Aces
######try/except
#####flags
#####rules
#####instructions










##This is the main function to play the game
##It also tracks scores and ask for rematches
def match():
    want_to_play = input("Want to play twenty_one? (Donn't worry, no money involved)\n")
    user_games = 0
    comp_games = 0
    while want_to_play =="yes":     
##twenty_one returns points for user and comp and is tracked
        if user_games == 15:
            cprint("Well Done! You've played quite a few, try running the game with the flag '--srem'", "red", "on_yellow")
            break
        else:
            points = twenty_one()
            user_games += points[0]
            comp_games += points[1]
            continue_the_game_one = input("")
            os.system('clear')

            cprint(f"So far it's your {user_games} games to my {comp_games} games", "red","on_yellow")
            want_to_play = input("Rematch?\n")
    cprint("Goodbye", "white", "on_blue")
    
### This is the rules of play of twenty_one
def twenty_one():
    ##creates deck
    deck = cards_and_deck.decks()
    ##users hand/total/check for aces/score if aces/display to screen
    users_hand = cards_and_deck.hands_dealt(deck)
    users_total = cards_and_deck.hand_total(users_hand)
    ##Acount for aces being possibly used for 11
    users_ace_high = cards_and_deck.check_aces(users_hand) *10
    users_total_ace_high=users_total+users_ace_high
    users_display = ""
    ##users hand/total/check for aces/score if aces/
    comps_hand = cards_and_deck.hands_dealt(deck)
    comps_total = cards_and_deck.hand_total(comps_hand)
    ##Acount for aces being possibly used for 11
    comps_ace_high = cards_and_deck.check_aces(comps_hand) *10
    comps_total_ace_high=comps_total+comps_ace_high
    ##allows game to go at users pace
    continue_the_game_two = input("Lets do this (press any key to cont)")
    ##round allows user to draw cards until he hits 21
    while users_total<=21:
    ##user hits 21
        if users_total == 21 or (users_total_ace_high) ==21:
            os.system('clear')
            drawings.cards_display_in_game(users_hand, comps_hand, users_display, dealers_display = "no")
            cprint("\nYou got 21!", "white", "on_blue")
            return 1,0
        else:    
    ##Displays running total of user to screen
            if users_ace_high == 0 or (users_total_ace_high >21):
                users_display = f"Your total is {users_total}"
            else:
                users_display = f"Your total is either {users_total} or {users_total_ace_high}"
    ##Gameplay alowing user to draw cards or Hold         
            os.system('clear')
            drawings.cards_display_in_game(users_hand, comps_hand, users_display, dealers_display = "yes")
            users_input = input("\nHit or Hold \n")
            while True:
                if users_input == "Hit" or users_input == "Hold":
                    break
                else:
    ##Error handling for wrong user inputs
                    os.system('clear')
                    drawings.cards_display_in_game(users_hand, comps_hand, users_display, dealers_display = "yes")
                    users_input = input("Can only choose Hit or Hold \n")
    ##User draws a card, appends to his hand with updated display hand/deck/total
            if users_input == "Hit":
                os.system('clear')
                users_hand = cards_and_deck.draw_card(users_hand, deck)
                users_total = cards_and_deck.hand_total(users_hand)
                users_ace_high = cards_and_deck.check_aces(users_hand) *10
                users_total_ace_high = users_total+users_ace_high
            else:
                break
    ##If User passes 21
    if users_total > 21:
        os.system('clear')
        drawings.cards_display_in_game(users_hand, comps_hand, users_display, dealers_display = "no")
        cprint("Woops! You Bust!", "white", "on_red")
        return 0,1
    ##Dealers turn, again at users pace
    else:
        continue_the_game_three = input("Now the dealers go")
    ##Dealer has same rules for 21
        while comps_total<=21:
            if comps_total == 21 or (comps_total_ace_high) ==21:
    ##If Dealer gets 21            
                os.system('clear')
                drawings.cards_display_in_game(users_hand, comps_hand, users_display, dealers_display = "no")
                cprint("\nDealer has 21!", "white", "on_blue")
                return 0,1
            else:    
    ##Dealers logic, only hits if hand is less than 16
                drawings.cards_display_in_game(users_hand, comps_hand, users_display, dealers_display = "yes")
                if comps_total <=16 or (comps_total_ace_high) <= 18:
                    os.system('clear')
    ##When dealer hits, update hand/total/display/deck
                    comps_hand = cards_and_deck.draw_card(comps_hand, deck)
                    comps_total = cards_and_deck.hand_total(comps_hand)
                    comps_ace_high = cards_and_deck.check_aces(comps_hand) *10
                    comps_total_ace_high = comps_total+comps_ace_high
                    cprint(f"Dealer draws", "white", "on_blue")
                else:
                    break
    ##If Deal busts
    if comps_total > 21:
        os.system('clear')
        drawings.cards_display_in_game(users_hand, comps_hand, users_display, dealers_display = "no")
        cprint("\nWoops, Dealer Drew and went Bust!", "white", "on_red")
        return 1,0
    else:
    ##Display/count cards/again input to control pace by user
        os.system('clear')
        cprint("Dealer Holds", "white", "on_blue")
        cprint("\nLets see what we've got", "white", "on_blue")
        drawings.cards_display_in_game(users_hand, comps_hand, users_display, dealers_display = "no")
        cprint(f"\nDealer total is {comps_total}, {users_display} \n", "white", "on_blue")
    ##Use helper functions to compare totals, declare winner and return points
        if comps_total_ace_high>21 or comps_ace_high ==0:
            if users_total_ace_high > 21 or users_ace_high == 0:
                who_won = cards_and_deck.winner(comps_total, users_total, comps_hand, users_hand)
                return who_won
            else:
                who_won = cards_and_deck.winner(comps_total, users_total, comps_hand, users_hand)
                return who_won
        else:
            if users_total_ace_high > 21 or users_ace_high == 0:
                who_won = cards_and_deck.winner(comps_total, users_total, comps_hand, users_hand)
                return who_won
            else:
                who_won = cards_and_deck.winner(comps_total, users_total, comps_hand, users_hand)
                return who_won

if "--help" in sys.argv:
    print("extras.help()")
elif "--secret" in sys.argv:
    print("secret message")
else:
    match()
