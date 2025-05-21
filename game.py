import random

def print_board(board):
    for i in range(3):
        row = board[i*3:(i+1)*3]
        print(' | '.join(cell or ' ' for cell in row))
        if i < 2:
            print('-'*9)

def check_winner(board, player):
    winning_combos = [
        [0,1,2],[3,4,5],[6,7,8], # rows
        [0,3,6],[1,4,7],[2,5,8], # columns
        [0,4,8],[2,4,6]          # diagonals
    ]
    for combo in winning_combos:
        if all(board[i] == player for i in combo):
            return True
    return False

def tic_tac_toe():
    board = [''] * 9
    current = 'X'
    for turn in range(9):
        print_board(board)
        move = None
        while move is None:
            try:
                choice = int(input(f"Player {current}, choose 0-8: "))
                if choice < 0 or choice > 8 or board[choice]:
                    print("Invalid move, try again.")
                else:
                    move = choice
            except ValueError:
                print("Please enter a valid number.")
        board[move] = current
        if check_winner(board, current):
            print_board(board)
            print(f"Player {current} wins!")
            return
        current = 'O' if current == 'X' else 'X'
    print_board(board)
    print("It's a draw!")

if __name__ == '__main__':
    tic_tac_toe()
