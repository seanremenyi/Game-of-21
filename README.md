# Twenty - One

This is a game of Twenty one built by Sean Remenyi to be run in the terminal and coded with the Python v 3.8 language.

#To Play

##### For the App,

1. Create a directory to clone the git repo into
2. Clone git repo
3. If not running python 3.8, run the following bash commands
    1. `sudo apt update`
    2. `sudo apt install python3.8`
    3. `sudo apt-get install python3-pip`
    4. `sudo apt install python3-termcolor`
4. Run the app by using
    `python main.py`

# Purpose and Scope
This application gives people a no-card-needed way to play twenty-one which is a game of BlackJack minus the gambling aspect. It’s purpose is to entertain and to give anyone who would like to play it, a way to break up their day. 

To discuss the problem this application solves is to look at the benefits of taking a break in your day. Without taking a break and working constantly can lead to fatigue and bad decision making. Taking a break is also a good way to reduce stress which can lead to adverse health effects. If someone would like to take a break without leaving their desk, they can open this application.

The target audience for this application is developers or anyone well versed in using terminal based applications. Anyone in this group who would like to take a break from their day can easily open the app and play a game of 21. This is a small contained file with ascii art  so shouldn’t impact the user’s work. This allows the user to easily switch to the game in a separate window if ever they want to play. 

The game can be executed from the terminal. It is made with understandability in mind. The user will be able to interact with the program through what the program displays to the terminal as well as user prompts and inputs of simple words to move the game forward. Rules and instructions will be made available in game as well as in a separate help file for the user to follow if they don’t understand how it works. The application will have cards drawn and not much text shown, again this is to make the game easy for the user and again the game's purpose is a pass time with breaks in mind. If the user is a developer i would like him to be able to have a break from staring at hundreds of lines of code with this application. There will be basic logic programmed into the computer opponent to also make the game more challenging.

# Features
### Deck and Dealing Cards
The game will create a variable and assign a list of values A,2,3,4,5,6,7,8,9,J, Q and K representing values of each card. The game will create another variable and assign a list of the suits (diamond, hearts, clubs and spades). 
```
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K"]
suits = ["♠", "♥", "♣", "♦"]
```
It has a function with a nested for loop that will then create a new list that will have every 52 possible card values. As for dealing cards, the game uses the built-in python module random to grab cards from this list and append it to either hand. Hands are just lists of strings, each string is a combination of a value and a suit created through the deck function.
```
['4♣', '8♦']
```
 The game then searches the deck for the matching card and deletes it from the list making sure a card isn’t dealt twice.


### Value of Cards
There are several functions used for the value of cards. This was done in mind to be able to import to future card games. As such each function has only one purpose and are used in conjunction for different tasks. The first function will take in one of these virtual cards in as an argument return the value of it (this accounts for the values of Aces, Jacks, Queens ad Kings as well). 
```
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
```

The second function will check for aces, remember the aces can be valued at either 1 or 11 so a check is needed, this function just loops through the hand to find the value of the 0th index of the card which is the value, it will find ‘‘A’’ and for any instances of this will add it to a variable count and return that value. The next function which uses the first mentioned function will take in a hand as an argument, it will take again the 0th index of each string, pass it through our value function and append that to a new list, this list will therefore just contain integers. Our final function takes in a hand and first passes through this last function mentioned. It will then create a variable “total” and set it to 0. It then loops through our returned list of integers and add them together and returns that value. 
```
def hand_total(hand):
    total = 0
    get_values = only_values(hand)
    for items in get_values:
        total += items
    return total
```
This again could of simply been done in one larger function but i believe this is easier to read going back to the code and again increases reusability as i can repurpose any function into further card games. These functions are wrapped in try/except statements to give messages if errors are thrown.


All these functions are used to find the total of each hand. This is used in the game to declare winners. Getting 21 is the goal of the game or as close as possible. The game will use my “winner” function to assess this. If either the user or dealer get 21 with the user as the priority (this game follows my custom set of rules) then we have our final function in my second module cards_and_deck.py which again uses the above functions to get a total of both the user and dealer’s hand and this “winner” function compares the two values and declares a winner. If it’s a tie the win goes to whoever has the least amount of cards.


### Display
Cards are drawn accounting for a possible maximum of 7 cards in either the dealer’s or the user’s hand  they will be displayed to the terminal to simulate an actual card game. The display will also show the dealer’s total as well the user’s. This is all drawn in a separate module for ease of readability. It will take in 4 arguments, the users hand, the dealers hand, users display and the dealers display. The first 2 arguments are used with the built-in “len” function to determine how many cards to show. The user’s display will show the total to the user (and if an ace is contained in the hand, both values for ace so the total if ace is valued for 1 or 11). 


The dealer’s display comes with an optional parameter. This is because until the game is deemed over the dealer’s first card remains hidden. Only when the user has decided to hold his hand, the parameter is changed and the dealer’s full hand and total is shown. This function will be wrapped in a try/except function in case an error is thrown and the cards are not displayed


### Gameplay
The game is wrapped in a function called “Match”. This function executes the function twenty one. This function will also declare variables, user games and comp games and after each game of twenty one is played will display to the terminal the running total of each before asking for a rematch. This is all looped until the user says no. Between turns and especially when the computer is having their turn i have added inputs for the user to press any key. This will be described in the instructions. This is just a way to pace out the game.


The computer can draw multiple cards before holding and without the user’s input this will happen in a second and the user won’t see each step. I found this takes away from the game. I have also imported the os module which using

```
os.system('clear')
```

Can tell the terminal to clear the screen so this avoids a huge mess of cards displayed. The program proceeds into the twenty-one function which will play out using all the above mentioned functions, creating a deck, dealing out hands and displaying this to the terminal. The User after receiving their hand then has a chance to hit or hold, hit being drawing a new card and the display and total is updated if the user chooses this or by holding which then the dealer goes. The user therefore may input hit or hold, anything else and the program will ask him to retry. As for the dealer, the logic built in will hit if it’s hand’s value is less than 16. Once it’s hand is above or equal to that the dealer will hold then the aforementioned functions are used to evaluate a winner  who is displayed to the screen. Along with this, 2 values are returned referring to the users points and the computer's points. This is then returned to the match function who adds it to the corresponding score and the loop continues. Text is displayed to guide the user as well as declare winners and this is colored using the termcolor module for fun.

### Flags

There will be 2 flags included in the game. One will be used if the user inputs the 
```
--help
```

 tag, this will display instructions and rules of the game to the terminal for the user.

The other tag will be 
```
--srem
```
 and this will be a secret the game contains. If the user reaches 15 winning games (so 15 points is reached in the match function) a message will appear to the user informing them of this tag. This if the user inputs while running the file will instead print to the screen a congratulations/thank you message.

# Implementation Plan

This project is to be completed by the 19th of July 2020. I will be using a trello board to help me complete this task and stay on track. I have created 4 lists of features, in progress (coding), testing and completed. I have created items for all the features in my game and move them to the corresponding list as I progress through the project.

My original idea was a game of cribbage but later pivoted into a game of twenty one, repurposing my code and this is reflected in my trello boards. Trello Board screenshots are also included in the assets folder for larger images and are named after their corresponding dates.


1. **Cards** To be completed by 12/07/2020
    1. Create my lists of suits and card values
Nested for loop to create a deck of cards.
    2.  Randomly assign 2 cards to new lists called hands and delete the corresponding card from the deck to avoid doubles and simulate a shuffled deck.
    3. Use same function for single cards to be dealt.

2. **Value of cards** To be completed by 12/15/2020
    1. Make function that will account for A,J,Q,K and return correct value.
    2. Make another function to extend that process to a whole list (hand) of cards.
    3. Make a third function to use the above process to return an integer total of a whole hand.

3. **Main Game** To be completed by 16/07/2020
    1. Prompt user if they would like to play (no leads to goodbye, yes starts game).
    2. Use any key prompts to control pacing of the game.
    3. Deal cards and tell user their total.
    4. Ask to hit or hold (hold moves on to next stage, hit adds a new card and the hand and total are reevaluated.
    5. Computer hits or holds (only hits if total is less than 16).
    6. Both hands are shown as well as both totals
    7. Totals are evaluated.
    8. Winner is declared.

4. **Drawings** To be completed by 17/07/2020
    1. Draw each possible hand with corresponding total making it useable for each cards value to be printed within the card.

5. **Extras** to be completed by 18/07/2020
    1. Clear terminal between hands.
    2. Ask for a rematch with total game points being tallied.
    3. Add flags for rules and secret message


# Testing

Testing was done by me and I created 10 different tests with a total of 30 documented trials where I isolated different functions as well as paying the game as a whole. This was too make sure the game worked and nothing unexpected occured

Included in my assests folder in a copy of the spreadsheet with a larger picture of the testing named test
or view [here](https://docs.google.com/spreadsheets/d/1zxKGWgfnHmTRH6I-4CCVleaFrLzmqBaGi3Zh3KcV6T4/edit?usp=sharing)


thank you and Enjoy!
