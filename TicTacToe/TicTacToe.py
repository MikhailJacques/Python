# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')__name__
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/

def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)


def is_winner(board, player):
    # Check rows, columns and diagonals for a win
    return (any(all(cell == player for cell in row) for row in board) or
            any(all(row[i] == player for row in board) for i in range(3)) or
            all(board[i][i] == player for i in range(3)) or
            all(board[i][2 - i] == player for i in range(3)))


def is_full(board):
    return all(cell != ' ' for row in board for cell in row)


def tic_tac_toe():
    # Initialize the board
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)

        # Get the player's move
        try:
            row, col = map(int,
                           input(f"Player {current_player}, enter row and column (1-3) separated by space: ").split())
        except ValueError:
            print("Please enter valid numbers.")
            continue

        # Check if the move is valid
        if row < 1 or row > 3 or col < 1 or col > 3 or board[row - 1][col - 1] != ' ':
            print("Invalid move. Try again.")
            continue

        # Make the move
        board[row - 1][col - 1] = current_player

        # Check for a win or tie
        if is_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif is_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # Switch the current player
        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == "__main__":
    tic_tac_toe()
