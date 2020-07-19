###rules and instructions to be printed with the --help tag
def help():
    print("""
Help

Objective
* The objective of the game is to reach 21 points or as close as possible without going over.

Rules
* The player is dealt 2 cards giving a certain total.
* The computer opponent known as the dealer is dealt 2 cards as well however only 1 is shown.
* The player can choose to Hit which will give him 1 more card and increase his total. The User can do this as many times as he wants until his hand is over 21 in which case he Busts and loses.
* The player has a further advantage that if he gets 21 in this phase will automatically win.
* If the player is happy with their hand and total they will choose to hold.
* Now it's the dealers turn and will also try to get as close to 21 without going over (can still go bust as well).
* If neither player busts or reaches 21 the two totals will be evaluated with the number closest to 21 winning, if the totals are equal, the winner will be whoever got there with the least amount of cards.

Instructions
* The game is commenced by going to the src folder and entering, 

./main.py

* You will be asked if you want to play, input "yes" to continue or "no" to receive a goodbye message.
* A prompt will come to start the game, here the user may input anything and return to start.
* The game will deal the cards and the user can choose to hit by inputing "Hit" or "Hold" to hold. Any other input will ask the user to try again either of those 2 options.
* Again any key prompts are used for the user to continue the game and control the pacing.
* These prompts will be used to continue until the end of the game to reach the final count and winner declared.
* The running total of how many ames won each player has is displayed and the game will ask if a rematch is wanted.
* "yes" to play again or "no" for the goodbye message)

""")
    return ""
### My secret message that will be displayed with the right flag
def secret():
    print("""

Wow You Won 15 Games, You Must Like This Game, Well I Must Say

 ____     ____     ____     ____     ____     ____     ____     ____
|    |   |    |   |    |   |    |   |    |   |    |   |    |   |    |
|  C |   |  O |   |  N |   |  G |   |  R |   | A  |   |  T |   |  S |
|____|   |____|   |____|   |____|   |____|   |____|   |____|   |____|
 
                            ____  
                           |    |  
                           |  & |  
                           |____| 

          ____     ____     ____     ____     ____
         |    |   |    |   |    |   |    |   |    |
         |  T |   |  H |   |  A |   |  N |   |  K |
         |____|   |____|   |____|   |____|   |____|          

                   ____     ____     ____
                  |    |   |    |   |    |
                  |  Y |   |  O |   |  U |  
                  |____|   |____|   |____|         
    
          
                        For Playing!  
""")
    return ""

