
# Global variables
board = [' ' for _ in range(9)]  # Represents the Tic Tac Toe board
current_player = 'X'  # Represents the current player ('X' or 'O')
winner = None  # Represents the winner of the game

# Function to display the Tic Tac Toe board
def display_board():
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('--+---+--')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('--+---+--')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])

# Function to handle a player's move
def handle_turn():
    position = int(input("Enter a position (1-9): ")) - 1
    if board[position] == ' ':
        board[position] = current_player
    else:
        print("That position is already filled. Try again.")
        handle_turn()

# Function to check if there is a winner
def check_winner():
    global winner
    rows = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]
    for row in rows:
        if board[row[0]] == board[row[1]] == board[row[2]] != ' ':
            winner = board[row[0]]
    if ' ' not in board:
        winner = 'Tie'

# Function to change the current player
def change_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'

# Function to play the game
def play_game():
    display_board()
    while winner is None:
        handle_turn()
        display_board()
        check_winner()
        change_player()
    if winner == 'Tie':
        print("It's a tie!")
    else:
        print("Congratulations! Player", winner, "wins!")

# Main
play_game()



    