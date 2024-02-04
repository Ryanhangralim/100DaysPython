from art import logo, vs 
from game_data import data
import random

#initialize variables
score = 0

#loops for game
choice_1 = random.choice(data)
while True:
    print(logo)

    #print if answer is right
    if(score > 0):
        print(f"You're right! Current score: {score}")
        choice_1 = choice_2

    #loop to prevent same comparison
    while True:
        choice_2 = random.choice(data)
        if not choice_2 == choice_1:
            break
    
    print(f"Compare A: {choice_1['name']}, {choice_1['description']}, from {choice_1['country']}.\n")
    print(vs)
    print(f"Against B: {choice_2['name']}, {choice_2['description']}, from {choice_2['country']}.")

    #check answer
    if(choice_1['follower_count'] > choice_2['follower_count']):
        answer = 'A'
    elif(choice_1['follower_count'] < choice_2['follower_count']):
        answer = 'B'

    user_answer = input("Who has more followers? Type 'A' or 'B': ")
    if user_answer == answer:
        score += 1
    else: 
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        break
