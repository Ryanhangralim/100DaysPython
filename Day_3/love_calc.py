print("The Love Calculator is calculating your score...")
name1 = input("What is you name? ")
name2 = input("What is their name? ")

true_digit = 0
love_digit = 0

for i in name1:
    letter = i.lower()
    if (letter == "t") or (letter == "r") or (letter == "u") or (letter == "e"):
        true_digit += 1
    if (letter == "l") or (letter == "o") or (letter == "v") or (letter == "e"):
        love_digit += 1

for i in name2:
    letter = i.lower()
    if (letter == "t") or (letter == "r") or (letter == "u") or (letter == "e"):
        true_digit += 1
    if (letter == "l") or (letter == "o") or (letter == "v") or (letter == "e"):
        love_digit += 1

love_score = int(str(true_digit) + str(love_digit))

if(love_score < 10 or love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos")
elif(love_score > 40 and love_score < 50):
    print(f"Your score is {love_score}, you are alright together")
else:
    print(f"Your score is {love_score}")