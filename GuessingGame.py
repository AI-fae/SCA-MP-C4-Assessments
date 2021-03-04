import random

print("Hi! will you like to play my guessing game?")

username = input("if yes, please enter a username\n >>> ")

guess = random.randint(0, 20)
user_guess = input(f'{username}, I am thinking of a number between 0 and 20. Take a guess \n >>>')


for n in range(6):
    
    try:
        user_guess = int(user_guess)
    except ValueError:
        print("INVALID INPUT: your guess must be an integer. Try again later")

        break
        
    if user_guess < 0:
        print("GUESS TOO LOW: your guess must be a number between 0 and 20")
        user_guess = input("try again:...  ")
    elif user_guess > 20:
        print("GUESS TOO HIGH: your guess must be a number between 0 and 20")
        user_guess = input("try again:...  ")
        
    elif user_guess != guess:
        print("ouch! that was close but still incorrect.")
        user_guess = input("try again:...  ")

    elif user_guess == guess:
        print(f' waw! you guessed correctly. {username}, you are a guessing genius.')
        break

print(f" The correct answer was: {guess}.\n Thanks for playing. hope you had fun?")
