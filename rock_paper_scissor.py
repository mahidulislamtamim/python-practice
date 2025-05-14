import random

choices = ("r", "p", "s")
emojis = {"r" : "Rock", "p" : "Paper", "s" : "Scissor"}

def get_user_choice():
    while True:
        user_choice = str(input("Rock, Paper or Scissor?(r/p/s):"))
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid choice!")


def show_choices(user_choice, computer_choice):
    print(f"Your chose {emojis[user_choice]}")
    print(f"Computer chose {emojis[computer_choice]}")


def determine_winer(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("Tie!")
    elif (
        (user_choice == "r" and computer_choice == "s") or
        (user_choice == "s" and computer_choice == "p") or
        (user_choice == "p" and computer_choice == "r")):
        print("You win")
    else :
        print("You lose") 

def main():
    while True:
        user_choice = get_user_choice()    
        computer_choice = random.choice(choices)

        show_choices(user_choice, computer_choice)
        
        determine_winer(user_choice, computer_choice)

        

        continue_game = (input("Do you play more?(y/n):")).lower()
        if continue_game == "n":
            break
        elif continue_game != "y":
            print("Invalid choice!")
            break



main()