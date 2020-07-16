import cards_and_deck


def blackjack():
    deck = cards_and_deck.decks()
    users_hand = cards_and_deck.hands_dealt(deck)
    comps_hand = cards_and_deck.hands_dealt(deck)
    users_total = cards_and_deck.hand_total(users_hand)
    users_ace_high = cards_and_deck.check_aces(users_hand) *10
    users_total_ace_high=users_total+users_ace_high
    comps_total = cards_and_deck.hand_total(comps_hand)
    comps_ace_high = cards_and_deck.check_aces(comps_hand) *10
    comps_total_ace_high=comps_total+comps_ace_high
    turn = 1
    while users_total<=21:
        if users_total == 21 or (users_total_ace_high) ==21:
            print(users_hand)
            print("21!")
            return 1,0
        else:    
            print(users_hand)
            if users_ace_high == 0 or (users_total_ace_high >21):
                print(f"your total is {users_total}")
            else:
                print(f"Your total is either {users_total} or {users_total_ace_high}")
            users_input = input("Draw or Hold")
            while True:
                if users_input == "Draw" or users_input == "Hold":
                    break
                else:
                    users_input = input("Can only choose Draw or Hold")
            if users_input == "Draw":
                users_hand = cards_and_deck.draw_card(users_hand, deck)
                users_total = cards_and_deck.hand_total(users_hand)
                users_ace_high = cards_and_deck.check_aces(users_hand) *10
                users_total_ace_high = users_total+users_ace_high
            else:
                break
    if users_total > 21:
        print(users_hand)
        print("Bust")
        return 0,1
    else:
        while comps_total<=21:
            if comps_total == 21 or (comps_total_ace_high) ==21:
                print(comps_hand)
                print("Dealer, 21!")
                return 0,1
            else:    
                print(comps_hand)
                if comps_total <=16 and (comps_total_ace_high) <= 18:
                    comps_hand = cards_and_deck.draw_card(comps_hand, deck)
                    comps_total = cards_and_deck.hand_total(comps_hand)
                    comps_ace_high = cards_and_deck.check_aces(comps_hand) *10
                    comps_total_ace_high = comps_total+comps_ace_high
                    print(f"Dealer draws")
                else:
                    print(f"Dealer total is {comps_total}")
                    break
    if comps_total > 21:
        print(comps_hand)
        print("Dealer Bust!")
        return 1,0
    else:
        if comps_total_ace_high>21 or comps_ace_high ==0:
            if users_total_ace_high > 21 or users_ace_high == 0:
                who_won = cards_and_deck.winner(comps_total, users_total)
                return who_won
            else:
                who_won = cards_and_deck.winner(comps_total, users_total_ace_high)
                return who_won
        else:
            if users_total_ace_high > 21 or users_ace_high == 0:
                who_won = cards_and_deck.winner(comps_total_ace_high, users_total)
                return who_won
            else:
                who_won = cards_and_deck.winner(comps_total_ace_high, users_total_ace_high)
                return who_won


    print(users_hand)
    print(users_total)
    print(comps_hand)
value = []
value = blackjack()
print(value)
