import os

# Clear the console for a fresh board display

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_board(board, player_pos):
    """Render the board with the player's current position."""
    clear()
    for y, row in enumerate(board):
        cells = []
        for x, cell in enumerate(row):
            if (x, y) == player_pos:
                cells.append('P')
            else:
                cells.append(cell)
        print(' '.join(cells))
    print("\nW/A/S/D to move, B to build, R to remove, Q to quit.")


def simple_minecraft(size=10):
    """A very small sandbox to move around and place blocks."""
    board = [['.' for _ in range(size)] for _ in range(size)]
    pos = (size // 2, size // 2)
    while True:
        print_board(board, pos)
        cmd = input("Command: ").strip().lower()
        x, y = pos
        if cmd == 'w' and y > 0:
            pos = (x, y - 1)
        elif cmd == 's' and y < size - 1:
            pos = (x, y + 1)
        elif cmd == 'a' and x > 0:
            pos = (x - 1, y)
        elif cmd == 'd' and x < size - 1:
            pos = (x + 1, y)
        elif cmd == 'b':
            board[y][x] = '#'
        elif cmd == 'r':
            board[y][x] = '.'
        elif cmd == 'q':
            break

    print("Thanks for playing!")


if __name__ == "__main__":
    simple_minecraft()
