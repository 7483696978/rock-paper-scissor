import random
import fontstyle

def get_user_choice():
    print("\n\nChoose (r) for Rock, (p) for Paper, or (s) for Scissors: ", end=" ")
    user_choice = input().strip().lower()
    while user_choice not in ["r", "p", "s"]:
        print("Invalid choice. Please choose 'r' for Rock, 'p' for Paper, or 's' for Scissors.")
        user_choice = input().strip().lower()
        
    if user_choice == "r":
        return "rock"
    elif user_choice == "p":
        return "paper"
    else:
        return "scissors"

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return fontstyle.apply("It's a TIE!", "bold/YELLOW")
    if (user_choice == "rock" and computer_choice == "scissors") or \
       (user_choice == "scissors" and computer_choice == "paper") or \
       (user_choice == "paper" and computer_choice == "rock"):
        return fontstyle.apply("You WIN!", "bold/GREEN")
    return fontstyle.apply("Computer Wins!", "bold/RED")

while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"You chose {user_choice}.")
    print(f"The computer chose {computer_choice}.")

    result = determine_winner(user_choice, computer_choice)
    print(result)

    play_again = input("Do you want to play again? (Y for Yes/N for No): ").strip().lower()
    if play_again != "y":
        break