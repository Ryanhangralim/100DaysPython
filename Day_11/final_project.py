from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#initilalize players cards
user_cards = []
comp_cards = []

def deal_cards(user):
    card = random.choice(cards)
    if(card == 11):
        if get_score(user) + 11 > 21:
            card = 1
    user.append(card)

def start():
    user_cards.clear()
    comp_cards.clear()
    for _ in range(2):
        deal_cards(user_cards)
        deal_cards(comp_cards)
        
def is_blackjack(cards):
    total = 0
    for card in cards:
        total += card
    if total == 21:
        return True
    else: 
        return False

def get_score(cards):
    total = 0
    for card in cards:
        total += card
    return total

def black_jack():
    choice = 'y'
    while choice == 'y':
        print(logo)
        start()
        print(f"Your cards: {user_cards}")
        print(f"Computer first card: {comp_cards[0]}")

        if(is_blackjack(user_cards)):
            print("You win")

        get_card = 'y'
        while get_card == 'y':
            get_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if(get_card == 'y'):
                deal_cards(user_cards)
                print(f"Your cards: {user_cards}")
                if(is_blackjack(user_cards)):
                    break
                elif(get_score(user_cards) > 21):
                    break
        
        #if computer cards is less than 16
        while(get_score(comp_cards) < 17):
            deal_cards(comp_cards)

        print(f"Your final hand: {user_cards}")
        print(f"Computer's final hand: {comp_cards}")

        user_total = get_score(user_cards)
        comp_total = get_score(comp_cards)

        #check scores
        if(is_blackjack(user_cards)) and (not is_blackjack(comp_cards)):
            print("You win")
        elif(is_blackjack(comp_cards)):
            print("You lose")
        elif(user_total > 21):
            print("You lose")
        elif(comp_total > 21):
            print("You win")
        elif(comp_total == user_total):
            print("Draw")
        elif(comp_total > user_total):
            print("You lose")
        elif(user_total > comp_total):
            print("You win")

        choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    
black_jack() 