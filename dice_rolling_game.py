import random

while True:
    choice = input("Roll the dice? (y/n): ").lower()
    
    if choice == "y":
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f"({die1}, {die2})")
        
    elif choice == "n":
        print("Thanks for playing!")
        break

    elif choice == "":
        print("Please enter y or n!")

    else:
        print("Invalid choice! Please enter y or n.")
