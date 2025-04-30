import random

number = random.randint(1, 100)
while True:
    try:
        guess = int(input("Guess the number between 1 and 100:"))
        if number > guess:
            print("Too low")
        if number < guess:
            print("Too high")
        if number == guess:
            print("Congratulations! Yor guessed the number.")
            break
    except ValueError:
        print("Please enter a valid number")


