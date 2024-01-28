import random
#import words from hangman_words
from hangman_words import word_list
import hangman_art

#initialize variables needed
lives = 6
end_of_game = False
chosen_word = random.choice(word_list)

#initialize empty list for user ui
answers = []
for _ in range(len(chosen_word)):
    answers.append("_")

#user menu
print(hangman_art.logo)
print(chosen_word)
#loops user's answer
while(lives > 0):
    guessed_letter = input("Guess a letter: ").lower()
    #check if guessed letter is in answer
    if guessed_letter in answers:
        print(f"You've already guessed the letter '{guessed_letter}'")
    
    if guessed_letter in chosen_word:
        for index in range(len(chosen_word)):
            if chosen_word[index] == guessed_letter:
                answers[index] = guessed_letter
    else:
        print(f"You guessed '{guessed_letter}', that's not in the word. You lose a life.")
        lives -= 1
        print(hangman_art.stages[lives])

    #print current answers
    print(f"{' '.join(answers)}")

    if("_" not in answers):
        print("You win.")
        break

if(lives == 0):
    print(f"You lose. The word is {chosen_word}")
    