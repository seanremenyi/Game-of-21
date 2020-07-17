import cards_and_deck
import drawings
from termcolor import cprint
import os


def match():
    
    #######try:
    
    want_to_play = input("Want to play BlackJack?\n")
    user_games = 0
    comp_games = 0
    while want_to_play =="yes":
        
        points = blackjack()
        user_games += points[0]
        comp_games += points[1]
        continue_the_game_one = input("")
        os.system('clear')
        cprint(f"So far it's your {user_games} games to my {comp_games} games", "red","on_yellow")
        want_to_play = input("Rematch?\n")
    cprint("Goodbye", "white", "on_blue")
    





def blackjack():
    deck = cards_and_deck.decks()
    users_hand = cards_and_deck.hands_dealt(deck)
    users_total = cards_and_deck.hand_total(users_hand)
    users_ace_high = cards_and_deck.check_aces(users_hand) *10
    users_total_ace_high=users_total+users_ace_high
    users_display = ""
    comps_hand = cards_and_deck.hands_dealt(deck)
    comps_total = cards_and_deck.hand_total(comps_hand)
    comps_ace_high = cards_and_deck.check_aces(comps_hand) *10
    comps_total_ace_high=comps_total+comps_ace_high
    continue_the_game_two = input("Lets do this")
    while users_total<=21:
        if users_total == 21 or (users_total_ace_high) ==21:
            drawings.cards_display_in_game(users_hand, comps_hand, users_display, dealers_display = "yes")
            cprint("\nYou got 21 already!", "white", "on_blue")
            return 1,0
        else:    
            if users_ace_high == 0 or (users_total_ace_high >21):
                users_display = f"\nYour total is {users_total}"
            else:
                users_display = f"\nYour total is either {users_total} or {users_total_ace_high}"
            drawings.cards_display_in_game(users_hand, comps_hand, users_display, dealers_display = "yes")
            users_input = input("\nDraw or Hold \n")
            while True:
                if users_input == "Draw" or users_input == "Hold":
                    break
                else:
                    
                    os.system('clear')
                    drawings.cards_display_in_game(users_hand, comps_hand, users_display, dealers_display = "yes")
                    users_input = input("Can only choose Draw or Hold \n")
            if users_input == "Draw":
                users_hand = cards_and_deck.draw_card(users_hand, deck)
                users_total = cards_and_deck.hand_total(users_hand)
                users_ace_high = cards_and_deck.check_aces(users_hand) *10
                users_total_ace_high = users_total+users_ace_high
            else:
                break
    if users_total > 21:
        drawings.cards_display_in_game(users_hand, comps_hand, users_display, dealers_display = "yes")
        cprint("You Bust", "white", "on_red")
        return 0,1
    else:
        while comps_total<=21:
            if comps_total == 21 or (comps_total_ace_high) ==21:
                drawings.cards_display_in_game(users_hand, comps_hand, users_display, dealers_display = "no")
                cprint("Dealer, 21!", "white", "on_blue")
                return 0,1
            else:    
                drawings.cards_display_in_game(users_hand, comps_hand, users_display, dealers_display = "yes")
                if comps_total <=16 and (comps_total_ace_high) <= 18:
                    comps_hand = cards_and_deck.draw_card(comps_hand, deck)
                    comps_total = cards_and_deck.hand_total(comps_hand)
                    comps_ace_high = cards_and_deck.check_aces(comps_hand) *10
                    comps_total_ace_high = comps_total+comps_ace_high
                    cprint(f"Dealer draws", "white", "on_blue")
                else:
                    
                    break
    if comps_total > 21:
        drawings.cards_display_in_game(users_hand, comps_hand, users_display, dealers_display = "no")
        cprint("Dealer Bust!", "white", "on_red")
        return 1,0
    else:
        os.system('clear')
        cprint("\nLets see what we've got", "white", "on_blue")
        drawings.cards_display_in_game(users_hand, comps_hand, users_display, dealers_display = "no")
        cprint(f"\nDealer total is {comps_total}, {users_display}", "white", "on_blue")
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

match()
# system clear or sysclear
# txt file
