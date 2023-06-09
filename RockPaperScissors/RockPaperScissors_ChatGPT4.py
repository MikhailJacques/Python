# Game of rock, paper, scissors (OpenAI ChatGPT4 generated)
import random


def play():
    user = input("What's your choice? 'rock', 'paper', or 'scissors': ")
    user = user.lower()

    while user != 'rock' and user != 'paper' and user != 'scissors':
        user = input("Invalid input. Please enter 'rock', 'paper', or 'scissors'\n")

    computer = random.choice(['rock', 'paper', 'scissors'])

    if user == computer:
        return f"Both you and the computer chose {user}. It's a tie!"

    if win(user, computer):
        return f"You chose {user} and the computer chose {computer}. You won!"

    return f"You chose {user} and the computer chose {computer}. You lost!"


def win(player, opponent):
    # return true if player wins
    # rock > scissors, scissors > paper, paper > rock
    if (player == 'rock' and opponent == 'scissors') or (player == 'scissors' and opponent == 'paper') \
            or (player == 'paper' and opponent == 'rock'):
        return True


def game():
    print("Rock, Paper, Scissors Game\n")
    print("You are playing against the computer. The game will continue until you decide to quit.\n")

    while True:
        print(play())
        play_again = input("Do you want to play again? (y/n): ")
        while play_again.lower() not in ['y', 'n']:
            play_again = input("Invalid input. Please enter 'y' or 'n': ")
        if play_again.lower() == 'n':
            break




# # Game of rock, paper, scissors (OpenAI ChatGPT4 via voice command generated)
# import random
#
#
# def get_computer_choice():
#     choices = ['rock', 'paper', 'scissors']
#     return random.choice(choices)
#
#
# def get_user_choice():
#     choice = input("Enter your choice (rock/paper/scissors) or 'q' to quit: ").lower()
#     return choice
#
#
# def determine_winner(user, computer):
#     if user == computer:
#         return "It's a tie!"
#     if (user == 'rock' and computer == 'scissors') or \
#        (user == 'scissors' and computer == 'paper') or \
#        (user == 'paper' and computer == 'rock'):
#         return "User wins!"
#     else:
#         return "Computer wins!"
#
#
# def main():
#     while True:
#         user_choice = get_user_choice()
#         if user_choice in ['q', 'quit']:
#             print("Thanks for playing!")
#             break
#         computer_choice = get_computer_choice()
#         print(f"Computer chose {computer_choice}")
#         result = determine_winner(user_choice, computer_choice)
#         print(result)
#
#
# if __name__ == "__main__":
#     main()
