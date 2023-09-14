#Guessing game
import random

guess_limit = 3
guess_count = 0
secret_number = random.randint(1, 20)


while guess_count < guess_limit:
    try:
        your_guess = int(input("Please guess a positive number less than 21: "))
        if  your_guess > 0 and your_guess==secret_number:
            print ("Congratulations, you guessed right")
            break
        elif your_guess > 0 or your_guess!=secret_number:
            print("You lose, wrong guess")
            guess_count += 1
    except ValueError as error:
        out_of_guesses=True
        guess_count += 1
        print("Unknown input, please try again with a 'POSITIVE INTEGER'")

print(f"This is the last randomly generated 'secret number': {secret_number}")






