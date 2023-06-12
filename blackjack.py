#BlackJack

#There are 52 cards in the deck.
#The cards are given a number, 1-52. 1-13 = Hearts, 14-26 = Diamonds, 27-39 = Puppy Paws, 40-52 = Spades
#Counting 1-13, A, 2, 3, ... 9, 10, J, Q, K

#imports the random function so a random number can be generated.
from multiprocessing.sharedctypes import Value
import random

#This class determines what the card name is as well as it's mathematical value.
class Cardname:

    def __init__(self, card_number):
        self.card = int(card_number)
        self.suit = ""
        self.num = ""
        self.value = ""

#This part of the class determines the suit of the card. This is for reporting the name of the card.
    def suit_type(self, card):
        self.suit = "Unknown"
        if card <= 13:
            self.suit = "Hearts"
        elif card <= 26:
            self.suit = "Diamonds"
        elif card <= 39:
            self.suit = "Puppy Paws"
        elif card <= 52:
            self.suit = "Spades"
        else:
            self.suit = "Error in determining type of suit for the card."
        return self.suit

#This determines both the number of the card and its mathemitacal value.
    def number_value(self, card):
        if card % 13 == 1:
            self.num = "Ace"
            self.value = 1
        elif card % 13 == 2:
            self.num = "Two"
            self.value = 2
        elif card % 13 == 3:
            self.num = "Three"
            self.value = 3
        elif card % 13 == 4:
            self.num = "Four"
            self.value = 4
        elif card % 13 == 5:
            self.num = "Five"
            self.value = 5
        elif card % 13 == 6:
            self.num = "Six"
            self.value = 6
        elif card % 13 == 7:
            self.num = "Seven"
            self.value = 7
        elif card % 13 == 8:
            self.num = "Eight"
            self.value = 8
        elif card % 13 == 9:
            self.num = "Nine"
            self.value = 9
        elif card % 13 == 10:
            self.num = "Ten"
            self.value = 10
        elif card % 13 == 11:
            self.num = "Jack"
            self.value = 10
        elif card % 13 == 12:
            self.num = "Queen"
            self.value = 10
        else:
            self.num = "King"
            self.value = 10
        return (self.num, self.value)
    
#This returns the card name and the value of the card.
    def __repr__(self):
        suit = self.suit_type(self.card)
        (num, value) = self.number_value(self.card)
        return "the {num_here} of {suit_here}".format(num_here = num, suit_here = suit)

#This class initializes the budget and keeps track of the budget throughout the game.
class Budget:

    def __init__(self, starting_budget):
        self.budget = int(starting_budget)
        self.result = ""
        self.auto_win = False

    def budget_update(self, bet, result, auto_win):
        self.result = result
        self.auto_win = auto_win
        if self.result == "win":
            self.budget += bet
        if self.result == "lose":
            self.budget -= bet
        if self.auto_win == True:
            self.budget += bet * 0.5

    def add_funds(self, additional_funds):
        self.budget += int(additional_funds)

    def __repr__(self):
        return "\nYou currently have a balance of $" + str(self.budget)

#Generates a deck of cards and gives two random cards to the player and two random cards to the dealer.
def deal_cards():
    card = 0
    player_cards = []
    dealer_cards = []
    list_of_cards = []

#Generates the list of 52 cards.
    i = 1
    while i < 53:
        list_of_cards.append(i)
        i += 1

#Generates the first two cards for the player.
    while len(player_cards) < 2:
        card = random.randint(1,52)
        if card in list_of_cards:
            player_cards.append(card)
            list_of_cards.remove(card)

#Generates the first two cards for the dealer.
    while len(dealer_cards) < 2:
        card = random.randint(1,52)
        if card in list_of_cards:
            dealer_cards.append(card)
            list_of_cards.remove(card)

    return player_cards, dealer_cards, list_of_cards

#In the following block of code, the starting cards and values of the player and the dealer are determined and information is passed onto the player.
#The function will return the player value and the dealer value for future use.
def begin_the_game():
    #Deals the cards
    player_value = 0
    dealer_value = 0
    player_ace = 0
    dealer_ace = False
    split = False
    dealer_show_ace = False
    dealer_show_ten = False
    initial_draw = (deal_cards())
    player_card_one = initial_draw[0][0]
    player_card_two = initial_draw[0][1]
    dealer_card_one = initial_draw[1][0]
    dealer_card_two = initial_draw[1][1]
    list_of_cards = initial_draw[2]

    #Checks for aces
    if player_card_one % 13 == 1:
        player_ace += 1
    if player_card_two % 13 == 1:
        player_ace += 1
    if dealer_card_one % 13 == 1:
        dealer_ace = True
        dealer_show_ace = True
    if dealer_card_two % 13 == 1:
        dealer_ace = True

    #Checks for dealer having 10 shown.
    if dealer_card_one % 13 == 10 or dealer_card_one % 13 == 11 or dealer_card_one % 13 == 12 or dealer_card_one % 13 == 0:
        dealer_show_ten = True

    #Determines the cards suit, name, and value for the player.
    card_drawn_p1 = Cardname(player_card_one)
    card_drawn_p1.suit_type(player_card_one)
    card_drawn_p1.number_value(player_card_one)
    player_value += card_drawn_p1.value
    card_drawn_p2 = Cardname(player_card_two)
    card_drawn_p2.suit_type(player_card_two)
    card_drawn_p2.number_value(player_card_two)
    player_value += card_drawn_p2.value
    print("\nYou were delt " + str(card_drawn_p1) + " and " + str(card_drawn_p2) + ".")

    #Determines the cards suit, name, and value for the dealer.
    card_drawn_d1 = Cardname(dealer_card_one)
    card_drawn_d1.suit_type(dealer_card_one)
    card_drawn_d1.number_value(dealer_card_one)
    dealer_value += card_drawn_d1.value
    dealer_shown_value = card_drawn_d1.value
    card_drawn_d2 = Cardname(dealer_card_two)
    card_drawn_d2.suit_type(dealer_card_two)
    card_drawn_d2.number_value(dealer_card_two)
    dealer_value += card_drawn_d2.value
    print("The dealer is showing " + str(card_drawn_d1) + ".")

    #Checks to see if the player can do a split.
    if card_drawn_p1.value == card_drawn_p2.value:
        split = True

    return player_value, dealer_value, list_of_cards, player_ace, dealer_ace, card_drawn_p1, card_drawn_p2, card_drawn_d1, card_drawn_d2, dealer_shown_value, split, dealer_show_ace, dealer_show_ten

#Code for current status.
def information(player_aces, player_value, player_value_with_ace, dealer_shown_value, double_down, stand):
    
    should_break = False
    
    if stand == True:
        print("\nYou stand with " + str(player_value) + ".")
        should_break = True
    
    if stand == False and double_down == False:

        if player_aces == False:
            if player_value == 21:
                print("\nTWENTY-ONE!")
                should_break = True
            elif player_value > 21:
                print("\nBUST!")
                should_break = True
            elif dealer_shown_value > 1:
                print("\nYou currently have " + str(player_value) + " and the dealer is showing " + str(dealer_shown_value) + ".")
            else:
                print("\nYou currently have " + str(player_value) + " and the daeler is showing " + str(dealer_shown_value) + " or " + str(dealer_shown_value + 10) + ".")
        
        if player_aces == True:
            print("Aces are true!")
            if player_value == 21:
                print("\nTWENTY-ONE!")
                should_break = True
            if player_value_with_ace == 21:
                player_value = 21
                print("\nTWENTY-ONE!")
                should_break = True
            if player_value > 21:
                print("\nBUST!")
                should_break = True
            if player_value_with_ace < 21 and dealer_shown_value > 1:
                print("\nYou currently have " + str(player_value) + " or " + str(player_value_with_ace) + " and the dealer is showing " + str(dealer_shown_value) + ".")
            if player_value_with_ace < 21 and dealer_shown_value == 1:
                print("\nYou currently have " + str(player_value) + " or " + str(player_value_with_ace) + " and the dealer is showing " + str(dealer_shown_value) + " or " + str(dealer_shown_value + 10) + ".")
            if player_value_with_ace > 21 and player_value < 21 and dealer_shown_value > 1:
                print("\nYou currently have " + str(player_value) + " and the dealer is showing " + str(dealer_shown_value) + ".")
            if player_value_with_ace > 21 and player_value < 21 and dealer_shown_value == 1:
                print("\nYou currently have " + str(player_value) + " and the dealer is showing " + str(dealer_shown_value) + " or " + str(dealer_shown_value + 10) + ".")
        
    if double_down == True:
        print("\nYou have a total of " + str(player_value))
        should_break = True
    
    return should_break

#Code for drawing a card.
def draw_a_card(card_list):
    list_of_cards = card_list
    value = 0
    in_the_list = False
    new_ace = player_aces
    
    while in_the_list == False:
        card = random.randint(1,52)
        if card in list_of_cards:
            list_of_cards.remove(card)
            in_the_list = True
            if card % 13 == 1:
                new_ace = True
    
    drawn_card = Cardname(card)
    drawn_card.suit_type(card)
    drawn_card.number_value(card)
    value += drawn_card.value

    return list_of_cards, value, new_ace, drawn_card

#Reports information on current cards.
def current_cards(player_cards, player_value, player_aces, player_value_split, dealer_cards, dealer_shown_value, player_cards_split, will_split, player_aces_split):
    
    if player_aces == True and player_value + 10 <= 21:
        print("\nYour cards:")
        for card in range(0, len(player_cards)):
            print(str(player_cards[card]))
        print("This is a total of " + str(player_value) + " or " + str(player_value + 10) + ".")
    else:
        print("\nYour cards: ")
        for card in range(0, len(player_cards)):
            print(str(player_cards[card]))
        print("This is a total of " + str(player_value) + ".")

    if will_split == True:
        if player_aces_split == True and player_value_split + 10 <= 21:
            print("\nYour cards for your second hand:")
            for card in (range(0, len(player_cards_split))):
                print(str(player_cards_split[card]))
            print("This is a total of " + str(player_value_split) + " or " + str(player_value_split + 10) + ".")
        else:
            print("\nYour cards for your second hand:")
            for card in range(0, len(player_cards_split)):
                print(player_cards_split[card])
            print("This is a total of " + str(player_value_split) + ".")

    if dealer_shown_value == 1:
        print("\nThe dealer is showing " + str(dealer_cards[0]) + " worth " + str(dealer_shown_value) + " or " + str(dealer_shown_value + 10) + ".")
    else:
        print("\nThe dealer is showing " + str(dealer_cards[0]) + " worth " + str(dealer_shown_value) + ".")
    
#Reports the wins, losses, and pushes, whether that information is called from.
def record(wins, losses, pushes):
    print("\nWins: " + str(wins))
    print("Losses: " + str(losses))
    print("Push: " + str(pushes))

#Determines what happens based on the player's choice.
def action(choice, list_of_cards, player_cards, player_value, player_value_with_ace, player_aces, wager):
    stand = False
    double_down = False

    #The player chose to hit.
    if choice == "1":
        print("\nHIT")
        new_card = draw_a_card(list_of_cards)
        print("You draw " + str(new_card[3]) + ".")
        list_of_cards = new_card[0]
        player_cards.append(new_card[3])
        player_value += new_card[1]
        player_value_with_ace += new_card[1]
        if player_aces == False:
            player_aces = new_card[2]

    
    #The player chose to stand.
    if choice == "2":
        if player_aces == True and player_value_with_ace <= 21:
            player_value = player_value_with_ace
        print("\nSTAND")
        stand = True
    
    #The player has chosen to double down.
    if choice == "3":
        if len(player_cards) > 2:
            print("Sorry! You can't double down. You've already hit.")
        elif player.budget >= on_the_line + wager:
            print("\nDOUBLE DOWN!")
            new_card = draw_a_card(list_of_cards)
            print("You draw " + str(new_card[3]) + ".")
            list_of_cards = new_card[0]
            player_cards.append(new_card[3])
            player_value += new_card[1]
            double_down = True
            wager = 2 * wager
        else:
            print("You do not have enough money to double down.")
            

    return (list_of_cards, player_cards, player_value, player_value_with_ace, player_aces, stand, double_down, wager)

#Determines the winner and updates the record.
def outcome(player, dealer, auto_win, wins, losses, pushes):
    win = False
    push = False
    result = ""
    
    if dealer > 21:
        win = True

    if player <= 21 and dealer <=21:
        if player > dealer:
            win = True
        elif player == dealer:
            push = True
    
    if auto_win == True:
        win = True
        push = False
    
    if win == True:
        wins += 1
    elif push == True:
        pushes += 1
    else:
        losses += 1

    if win == True:
        result = "win"
    elif push == True:
        result = "push"
    else:
        result = "lose"

    return wins, losses, pushes, result

def initial_wager():
    set_wager = input("")
    while set_wager[0] == "-":
        print("Well that's just silly! You need to make a wager that is a positive number! (Or zero, if you just want to play for fun!)")
        set_wager = input("")
    try:
        set_wager = int(set_wager)
    except ValueError:
        print("That's not a number! Try again!")

    return set_wager

#Code for the Game
main_menu = "0"
game_menu = "0"
wins = 0
losses = 0
pushes = 0
budget = ""
set_wager = ""

#Welcomes the player and set the starting budget.
print("\nWelcome! Before we begin, you need to have a starting balance! How much money would you like to start with?")
while type(budget) != int:
    budget = input("")
    try:
        budget = int(budget)
    except ValueError:
        print("That's not a number! Try again!")
    if type(budget) == int:
        player = Budget(budget)

#Main menu display and input.
while main_menu != "9":

    print("\nMain Menu: \n1) Start a new game. \n2) View your record. \n3) Check my balance. \n4) Add money to my balance. \n9) Exit the game.")

    main_menu = input("")
    if main_menu != "1" and main_menu != "2" and main_menu != "3" and main_menu != "4" and main_menu != "9":
        print("Oops! Try again!")

    #Starts the game.
    if main_menu == "1":
        
        if type(set_wager) != int:
            print("\nOk! Before we deal the cards, we need to set a wager. So, how much do you want to bet per hand? \nYour current balance balance is $" + str(player.budget) + ".")
            while type(set_wager) != int:
                set_wager = initial_wager()

        while game_menu != "9":
            print("\nYour current balance is $" + str(player.budget) + " and you are set to wager $" + str(set_wager) + " per hand.\nIf you need to add more funds, please go back to the main menu.")
            print("\nGame Menu: \n1) Deal the cards.\n2) View your record. \n3) Change my wager. \n9) Quit -- Go back to main menu.")
            game_menu = input("")
            if game_menu != "1" and game_menu != "2" and game_menu != "3" and game_menu != "9":
                print("Oops! Try again!")

            #Code for running the game. First thing to do it deal two cards and then varaibles are assigned their values. All the needed variables are listed below.
            if game_menu == "1" and player.budget < set_wager:
                print("Unfortunately, your balance is less than your wager. You will need to either decrease your wager or add more funds.")

            if game_menu == "1" and player.budget >= set_wager:
                game = begin_the_game()

                wager = set_wager
                wager_split = 0

                player_cards = []
                player_cards.append(game[5])
                player_cards.append(game[6])
                player_aces = False
                num_player_aces = game[3]
                player_value = game[0]
                player_value_with_ace = player_value + 10
                
                player_cards_split = []
                player_value_split = 0
                player_aces_split = False
                player_value_with_ace_split = player_value_split + 10
                split_option = game[10]
                will_split = False
                will_split_aces = False

                dealer_value = game[1]
                dealer_value_with_ace = dealer_value + 10
                dealer_shown_value = game[9]
                dealer_aces = game[4]
                dealer_cards = []
                dealer_cards.append(game[7])
                dealer_cards.append(game[8])
                dealer_done = False
                dealer_show_ace = game[11]
                dealer_show_ten = game[12]

                list_of_cards = game[2]
                
                win = False
                auto_win = False
                auto_win_split = False
                push = False
                stand = False
                stand_split = False
                double_down = False
                double_down_split = False
                doubling = ""
                doubling_split = ""
                dealer_black_jack = False
                can_split = False
                on_the_line = wager
                insurance_value = wager / 2
                insurance_want = ""
                insurance_push = False

                #Checks the balance to see if a split is financially possible.
                if player.budget >= on_the_line + wager:
                    can_split = True

                #Checks for how many aces the player is delt, so a decision can be made on a Blackjack or a split.
                if num_player_aces != 0:
                    player_aces = True

                #Checks for a BlackJack. If the player has one, they automatically win and the game ends.
                if player_aces == True and player_value_with_ace == 21:
                    print("\nBLACK JACK! YOU WIN!")
                    player_value = 21
                    auto_win = True
                    print("The dealer had " + str(dealer_cards[0]) + " and " + str(dealer_cards[1]) + " but it doens't matter, because you had a BLACKJACK! :)")
                    dealer_done = True

                #The dealer is showing an ace. Insurance is offered.
                if dealer_aces == True and dealer_show_ace == True and auto_win == False:
                    if player.budget >= on_the_line + insurance_value:
                        print("The dealer is showing an ace. Do you want insurance? y or n")
                        insurance_want = input("")
                        while insurance_want != "y" and insurance_want != "n":
                            print("""Please enter "y" or "n" """)
                            insurance_want = input("")
                    else:
                        print("The dealer is showing an ace, but you do not have enough money for insurance.")

                    if dealer_value_with_ace == 21:
                        dealer_value = 21
                        print("The dealer's second card is " + str(dealer_cards[1]) + ".")
                        print("Aww... the dealer has BlackJack. You lose :(")
                        if insurance_want == "y":
                            print("BUT! You got insurance! So you will break even! (It will still count as a loss, though.)")
                            insurance_push = True
                        dealer_done = True
                        dealer_black_jack = True
                    elif dealer_value_with_ace != 21 and insurance_want != "y":
                        print("Good news! The daler does not have a blackjack.")
                    else:
                        print("Good news! The dealer does not have a blackjack. However, you lose the insurance money.")
                        player.budget -= insurance_value

                #If the dealer is showing a ten, it will determine if the dealer has a blackjack and the game is over.
                if dealer_aces == True and dealer_show_ten == True and auto_win == False:
                    if dealer_value_with_ace == 21:
                        print("\nAww... the dealer has BlackJack. You Lose :(")
                        dealer_black_jack = True
                        dealer_done = True
                    else:
                        print("The dealer is showing 10, but fortunately, they do not have a blackjack!")

                #Checks to see if the player would like to split their aces. This is a special split, becuase you only get one hit.
                #Will automatically run the hits from here.
                if num_player_aces == 2 and dealer_black_jack == False and can_split == True:
                    split_aces = input("Do you want to split your aces? REMEMBER, if you split aces, you only get one hit for each ace.\ny or n\n")
                    
                    while split_aces != "y" and split_aces != "n":
                        print("""Please selected "y" or "n" """)
                        split_aces = input("")

                    if split_aces == "y":
                        wager_split = wager
                        on_the_line = wager + wager_split
                        will_split_aces = True
                        temp_card = player_cards.pop()
                        player_cards_split.append(temp_card)
                        player_value = 1
                        player_value_with_ace = player_value + 10
                        player_value_split = 1
                        player_value_with_ace = player_value_with_ace + 10

                        if player.budget >= on_the_line + wager:
                            while doubling != "y" and doubling != "n":
                                doubling = input("\nDo you want to double down on the first ace?\ny or n\n")
                                if doubling == "y":
                                    wager = 2 * wager
                                    on_the_line = wager + wager_split
                                if doubling != "y" and doubling != "n":
                                    print("""Please enter "y" or "n".""")
                        else:
                            print("\nYou do not have enough money to double down on the first hand.")

                        new_card = draw_a_card(list_of_cards)
                        print("\nYou draw " + str(new_card[3]) + ".")
                        list_of_cards = new_card[0]
                        player_value += new_card[1]
                        player_value += 10
                        print("The first hand has a total of " + str(player_value))
                        if player_value == 21:
                            print("BLACKJACK!")
                            auto_win = True

                        if player.budget >= on_the_line + wager_split:
                            while doubling_split != "y" and doubling_split != "n":
                                doubling_split = input("\nDo you want to double down on the second ace?\ny or n\n")
                                if doubling_split == "y":
                                    wager_split = 2 * wager_split
                                    on_the_line = wager + wager_split
                                if doubling_split != "y" and doubling_split != "n":
                                    print("""Please enter "y" or "n".""")
                        else:
                            print("\nYou do not have enough money to double down on the second hand.")
                        
                        new_card = draw_a_card(list_of_cards)
                        print("\nYou draw " + str(new_card[3]) + ".")
                        list_of_cards = new_card[0]
                        player_value_split += new_card[1]
                        player_value_split += 10
                        print("The second hand has a total of " + str(player_value_split))
                        if player_value_split == 21:
                            print("BLACKJACK!")
                            auto_win_split = True
                        
                    if auto_win == True and auto_win_split == True:
                        print("The dealer had " + str(dealer_cards[0]) + " and " + str(dealer_cards[1]) + " but it doens't matter, because you have a BLACKJACK on both hands! :)")
                        dealer_done = True

                #Informs the player they do not have enough money to split their aces.
                if num_player_aces == 2 and dealer_black_jack == False and can_split == False:
                    print("You do not have enough money to split the aces.")

                #Checks to see if the player would like to split their cards (non-aces).
                if split_option == True and dealer_black_jack == False and num_player_aces != 2 and can_split == True:
                    split = input("\nDo you want to split your cards? \ny or n\n")
                    while split != "y" and split != "n":
                        print("""Please selected "y" or "n" """)
                        split = input("")
                    if split == "y":
                        will_split = True
                        wager_split = wager
                        temp_card = player_cards.pop()
                        player_cards_split.append(temp_card)
                        player_value = player_value / 2
                        player_value = int(player_value)
                        player_value_split = player_value
                        player_value_with_ace = player_value + 10
                        player_value_with_ace_split = player_value_split + 10
                        print("\nIn one hand, you have " + str(player_cards[0]) + "and in the second hand, you have " + str(player_cards_split[0]) + ". Each hand has a value of " + str(player_value))
                        print("We'll now draw one card for each of your two hands.")

                        if player.budget >= on_the_line + wager:
                            while doubling != "y" and doubling != "n":
                                doubling = input("\nDo you want to double down on the first hand?\ny or n\n")
                                if doubling == "y":
                                    wager = 2 * wager
                                    on_the_line = wager + wager_split
                                    double_down = True
                                if doubling != "y" and doubling != "n":
                                    print("""Please enter "y" or "n".""")
                        else:
                            print("\nYou do not have enough money to double down on the first hand.")

                        new_card = draw_a_card(list_of_cards)
                        print("\nYou draw " + str(new_card[3]) + ".")
                        list_of_cards = new_card[0]
                        player_cards.append(new_card[3])
                        player_value += new_card[1]
                        player_value_with_ace += new_card[1]
                        if player_aces == False:
                            player_aces = new_card[2]
                        if doubling == True and player_aces == True:
                            player_value = player_value_with_ace

                        if player_value_with_ace == 21 and player_aces == True:
                            print("BLACKJACK!")
                            player_value = player_value_with_ace
                            auto_win = True
                        if player_aces == True and doubling == False:
                            print("Your first hand has a value of " + str(player_value) + " or " + str(player_value_with_ace) + ".")
                        if player_aces == True and doubling == True:
                            print("You double down on the first hand and thus stand with " + str(player_value) + ".")
                        if player_aces == False and doubling == True:
                            print("You double down on the first hand and thus stand with " + str(player_value) + ".")
                        if player_aces == False and doubling == False:
                            print("Your first hand has a value of " + str(player_value) + ".")
                        
                        if player.budget >= on_the_line + wager_split:
                            while doubling_split != "y" and doubling_split != "n":
                                doubling_split = input("\nDo you want to double down on the second hand?\ny or n\n")
                                if doubling_split == "y":
                                    wager_split = 2 * wager_split
                                    on_the_line = wager + wager_split
                                    double_down_split = True
                                if doubling_split != "y" and doubling_split != "n":
                                    print("""Please enter "y" or "n".""")
                        else:
                            print("\nYou do not have enough money to double down on the second hand.")


                        new_card = draw_a_card(list_of_cards)
                        print("\nYou draw " + str(new_card[3]) + ".")
                        list_of_cards = new_card[0]
                        player_cards_split.append(new_card[3])
                        player_value_split += new_card[1]
                        player_value_with_ace_split += new_card[1]
                        if player_aces_split == False:
                            player_aces_split = new_card[2]
                        if doubling_split == True and player_aces == True:
                            player_value_split = player_value_with_ace_split

                        if player_value_with_ace_split == 21 and player_aces_split == True:
                            print("BLACKJACK!")
                            player_value_split = player_value_with_ace_split
                            auto_win_split = True
                        if player_aces_split == True and doubling_split == False:
                            print("Your second hand has a value of " + str(player_value_split) + " or " + str(player_value_with_ace_split) + ".")
                        if player_aces_split == True and doubling_split == True:
                            print("You double down on the second hand and thus stand with " + str(player_value_split) + ".")
                        if player_aces_split == False and doubling_split == False:
                            print("Your second hand has a value of " + str(player_value_split) + ".")
                        if player_aces_split == False and doubling_split == True:
                            print("Your double down on the second hand and thus stand with " + str(player_value_split) + ".")

                        if auto_win == True and auto_win_split == True:
                            print("The dealer had " + str(dealer_cards[0]) + " and " + str(dealer_cards[1]) + " but it doens't matter, because you have a BLACKJACK on both hands! :)")
                            dealer_done = True

                #Informs the player they do not have enough money to split.
                if split_option == True and dealer_black_jack == False and num_player_aces != 2 and can_split == False:
                    print("You do not have enough money to split your hand.")

                #The player does not have BlackJack and neither does the dealer. Also, the player is not splitting aces.
                while dealer_black_jack == False and will_split_aces == False and auto_win == False and double_down == False:
                    
                    print_information = information(player_aces, player_value, player_value_with_ace, dealer_shown_value, double_down, stand)
                    if print_information == True:
                        break
                    
                    print("\nWhat would you like to do?")

                    #The player will now decide to hit or stand.
                    print("\n1) Hit \n2) Stand \n3) Double Down \n4) Show the cards")
                    choice = ""
                    while choice != "1" and choice != "2" and choice != "3" and choice != "4":
                        choice = input("")

                        #The player has taken action. A function is called to determine what happens with that action.
                        if choice == "1" or choice == "2" or choice == "3":
                            result_of_action = action(choice, list_of_cards, player_cards, player_value, player_value_with_ace, player_aces, wager)
                            list_of_cards = result_of_action[0]
                            player_cards = result_of_action[1]
                            player_value = result_of_action[2]
                            player_value_with_ace = result_of_action[3]
                            player_aces = result_of_action[4]
                            stand = result_of_action[5]
                            double_down = result_of_action[6]
                            wager = result_of_action[7]
                            if player_aces == True and player_value_with_ace == 21:
                                player_value = 21

                        #The player chose to view cards.
                        if choice == "4":
                            current_cards(player_cards, player_value, player_aces, player_value_split, dealer_cards, dealer_shown_value, player_cards_split, will_split, player_aces_split)

                        #Incorrect entry
                        if choice != "1" and choice != "2" and choice != "3" and choice != "4":
                            print("Oops! Try again!")

                #Runs the second hand of the game if the player has chosen to split (non-aces)
                while dealer_black_jack == False and will_split_aces == False and auto_win_split == False and will_split == True and double_down_split == False:
                    
                    print_information = information(player_aces_split, player_value_split, player_value_with_ace_split, dealer_shown_value, double_down_split, stand_split)
                    if print_information == True:
                        break
                    
                    print("\nWhat would you like to do for your second hand?")

                    #The player will now decide to hit or stand.
                    print("\n1) Hit \n2) Stand \n3) Double Down \n4) Show the cards")
                    choice = ""
                    while choice != "1" and choice != "2" and choice != "3" and choice != "4":
                        choice = input("")

                        #The player has taken action. A function is called to determine what happens with that action.
                        if choice == "1" or choice == "2" or choice == "3":
                            result_of_action = action(choice, list_of_cards, player_cards_split, player_value_split, player_value_with_ace_split, player_aces_split, wager_split)
                            list_of_cards = result_of_action[0]
                            player_cards_split = result_of_action[1]
                            player_value_split = result_of_action[2]
                            player_value_with_ace_split = result_of_action[3]
                            player_aces_split = result_of_action[4]
                            stand_split = result_of_action[5]
                            double_down_split = result_of_action[6]
                            wager_split = result_of_action[7]
                            if player_value_with_ace_split == 21:
                                player_value_split = 21

                        #The player chose to view cards.
                        if choice == "4":
                            current_cards(player_cards, player_value, player_aces, player_value_split, dealer_cards, dealer_shown_value, player_cards_split, will_split, player_aces_split)

                        #Incorrect entry
                        if choice != "1" and choice != "2" and choice != "3" and choice != "4":
                            print("Oops! Try again!")

                #Determines if the dealer needs to play. If player has busted on BOTH their initial hand and their split, then the game ends.
                if will_split_aces == True or will_split == True:
                    if player_value > 21 and player_value_split > 21:
                        dealer_done = True
                        print("The dealer had " + str(dealer_cards[0]) + " and " + str(dealer_cards[1]) + " but it doens't matter, because you busted on both hands!")
                else:
                    if player_value > 21:
                        dealer_done = True
                        print("The dealer had " + str(dealer_cards[0]) + " and " + str(dealer_cards[1]) + " but it doens't matter, because you busted.")

                #The player does not have a blackjack and has not busted. So now the program will determine what the dealer must do.
                if dealer_done == False:
                    print("Now it's the dealer's turn!")
                    if dealer_aces == True:
                        print("The dealer has " + str(dealer_cards[0]) + " and " + str(dealer_cards[1]) + " totaling " + str(dealer_value) + " or " + str(dealer_value_with_ace) + ".")
                    else:
                        print("The dealer has " + str(dealer_cards[0]) + " and " + str(dealer_cards[1]) + " totaling " + str(dealer_value) + ".")

                #Determines if the dealer needs to draw a card, and if so, draws the card. Dealer keeps drawing cards until the dealer has a value greater than or equal to 17, except for soft 17s.
                while dealer_done == False:
                    if dealer_value > 21:
                        print("\nThe dealer has busted!")
                        dealer_done = True
                    
                    if dealer_aces == True:
                        if 18 <= dealer_value_with_ace <= 21:
                            dealer_value = dealer_value_with_ace
                            dealer_done = True

                        if dealer_value_with_ace <= 17:
                            if dealer_value_with_ace == 17:
                                print("\nThe dealer has a soft 17 and must hit.")
                            else:
                                print("\nThe dealer must hit.")
                            dealer_new_card = draw_a_card(list_of_cards)
                            list_of_cards = dealer_new_card[0]
                            dealer_value += dealer_new_card[1]
                            dealer_value_with_ace = dealer_value + 10
                            dealer_cards.append(dealer_new_card[3])
                            if dealer_value_with_ace > 21:
                                print("The dealer darws " + str(dealer_new_card[3]) + " and now totals " + str(dealer_value) + ".")
                            else:
                                print("The dealer darws " + str(dealer_new_card[3]) + " and now totals " + str(dealer_value) + " or " + str(dealer_value_with_ace) + ".")

                        if dealer_value_with_ace > 21 and dealer_value < 17:
                            print("\nThe dealer must hit.")
                            dealer_new_card = draw_a_card(list_of_cards)
                            list_of_cards = dealer_new_card[0]
                            dealer_value += dealer_new_card[1]
                            dealer_cards.append(dealer_new_card[3])
                            print("The dealer darws " + str(dealer_new_card[3]) + " and now totals " + str(dealer_value) + ".")

                        if 17 <= dealer_value <= 21:
                            dealer_done = True
                        
                        if dealer_value > 21:
                            print("\nThe dealer has busted!")
                            dealer_done = True

                    if dealer_aces == False:
                        if dealer_value < 17:
                            print("\nThe dealer must hit.")
                            dealer_new_card = draw_a_card(list_of_cards)
                            list_of_cards = dealer_new_card[0]
                            dealer_value += dealer_new_card[1]
                            dealer_value_with_ace = dealer_value + 10
                            dealer_aces = dealer_new_card[2]
                            dealer_cards.append(dealer_new_card[3])
                            if dealer_aces == True and 18 <= dealer_value_with_ace <= 21:
                                print("The dealer draws " + str(dealer_new_card[3]) + " and now totals " + str(dealer_value_with_ace) + " and will now stand.")
                            elif dealer_aces == True and dealer_value_with_ace <= 17:
                                print("The dealer draws " + str(dealer_new_card[3]) + " and now totals " + str(dealer_value) + " or " + str(dealer_value_with_ace) + ".")
                            else:
                                print("The dealer darws " + str(dealer_new_card[3]) + " and now totals " + str(dealer_value) + ".")
                        else:
                            dealer_done = True

                #Determines the winner.
                game_result = outcome(player_value, dealer_value, auto_win, wins, losses, pushes)
                wins = game_result[0]
                losses = game_result[1]
                pushes = game_result[2]

                #Determines the winner of the split hand.
                if will_split == True or will_split_aces == True:
                    game_result_split = outcome(player_value_split, dealer_value, auto_win, wins, losses, pushes)
                    wins = game_result_split[0]
                    losses = game_result_split[1]
                    pushes = game_result_split[2]
                
                #Reports the outcome.
                if insurance_push == True:
                    print("The results: You lost, but you had insurance, so you break even.")
                else:
                    if will_split == False and will_split_aces == False:
                        print("The results:")
                        if auto_win == True:
                            print("BLACKJACK! \nTherefore, you get a x1.5 payout, totalling " + str(wager * 1.5) + ".")
                        if auto_win == False:
                            print("You " + game_result[3] + ".\nTherefore, you " + game_result[3] + " $" + str(wager) + ".")
                    else: 
                        print("The results: ")
                        if auto_win == True:
                            print("First hand: BLACKJACK! \nTherefore, you get a x1.5 payout, totalling " + str(wager * 1.5) + ".")
                        else:
                            print("First hand: You " + game_result[3] + ".\nTherefore, you " + game_result[3] + " $" + str(wager) + ".")
                        if auto_win_split == True:
                            print("Second hand: BLACKJACK! \nTherefore, you get a x1.5 payout, totalling " + str(wager_split * 1.5) + ".")
                        else:
                            print("Second hand: You " + game_result_split[3] + ".\nTherefore, you " + game_result_split[3] + " $" + str(wager_split) + ".")

                #Calculate and prints the new balance.
                if insurance_push == False:
                    player.budget_update(wager, game_result[3], auto_win)
                    if will_split == True or will_split_aces == True:
                        player.budget_update(wager_split, game_result_split[3], auto_win_split)
                    print(player)

                #Resets the game_menu to zero after the game have finished.
                game_menu = "0"
                
            #Code for game_menu choice "2". Shows wins/loss/push
            if game_menu == "2":
                record(wins, losses, pushes)
                game_menu = "0"

            #Code for allowing the player to change their wager.
            if game_menu == "3":
                print("Your current wager is $" + str(set_wager) + ". What would you like to set it to now?")
                set_wager = ""
                while type(set_wager) != int:
                    set_wager = initial_wager()
                    

        #Resets the game_menu, so you can exit the game and then return later.
        game_menu = "0"

    #Shows wins/loss/push
    if main_menu == "2":
        record(wins, losses, pushes)
        main_menu = "0"
    
    #Displays the current balance.
    if main_menu == "3":
        print(player)
    
    #Allows the user to add more money.
    if main_menu == "4":
        print("\nHow much do you wish to add to your balance?")
        additional_funds = ""
        while type(additional_funds) != int:
            additional_funds = input("")
            try:
                additional_funds = int(additional_funds)
            except ValueError:
                print("That's not a number! Try again!")
            if type(additional_funds) == int:
                if -1 * additional_funds > player.budget:
                    print("You do not have enough money in your balance to withdraw this much.")
                else:
                    player.add_funds(additional_funds)
                    print(player)
        
print("Thank you for playing!")
