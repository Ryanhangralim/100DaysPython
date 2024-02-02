from random import randint

#initializing global variables
EASY_MODE = 10
HARD_MODE = 5

def guess(lives):
    answer = randint(1, 100)
    while(lives > 0):
        print(f"You have {lives} attemps remaining to guess the number.")
        user_guess = int(input("Make a guess: "))

        if user_guess > answer:
            print("Too High")
        elif user_guess < answer:
            print("Too Low")
        elif user_guess == answer:
            print(f"You got it! The answer was {answer}")
            return
        print("Guess again")
        lives -= 1
    print("You've run out of guesses, you lose.")
    return

def main():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    
    if difficulty == 'easy':
        guess(EASY_MODE)
    elif difficulty == 'hard':
        guess(HARD_MODE)

if __name__ == "__main__":
    main()