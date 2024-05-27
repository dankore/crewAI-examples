# Tic Tac Toe Game in Python

board = [[' ' for _ in range(3)] for _ in range(3)]

def print_board():
    for row in board:
        print(' | '.join(row))
        print('---------')

def check_win(player):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def game():
    current_player = 'X'
    while True:
        print_board()
        row = int(input("Enter the row (0-2): "))
        col = int(input("Enter the column (0-2): "))
        if board[row][col] == ' ':
            board[row][col] = current_player
            if check_win(current_player):
                print_board()
                print(f"Player {current_player} wins!")
                break
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Invalid move, try again!")

game()