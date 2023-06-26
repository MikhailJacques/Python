# Game of rock, paper, scissors (Google Bard generated)
import random


def get_user_choice():
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please try again.")


def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Tie"
    elif user_choice == "rock" and computer_choice == "scissors":
        return "User"
    elif user_choice == "paper" and computer_choice == "rock":
        return "User"
    elif user_choice == "scissors" and computer_choice == "paper":
        return "User"
    else:
        return "Computer"


def main():
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)

        print(f"Your choice: {user_choice}, Computer's choice: {computer_choice}")
        if winner == "User":
            print("You win!")
        elif winner == "Computer":
            print("Computer wins!")
        else:
            print("Tie!")

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again in ["y", "n"]:
            if play_again == "y":
                continue
            else:
                break
        else:
            print("Invalid input. Please enter 'y' or 'n': ")


if __name__ == "__main__":
    main()
