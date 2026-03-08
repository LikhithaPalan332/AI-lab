import math

board = [' ' for _ in range(9)]
def print_board():
    print()
    for i in range(0,9,3):
        print(board[i], "|", board[i+1], "|", board[i+2])
        if i < 6:
            print("--+---+--")
    print()
    
def check_winner(p):
    win = [[0,1,2],[3,4,5],[6,7,8],
           [0,3,6],[1,4,7],[2,5,8],
           [0,4,8],[2,4,6]]
    
    for pos in win:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == p:
            return True
    return False

def is_draw():
    return ' ' not in board

def minimax(is_max, depth=0):

    if check_winner('O'):
        return 1
    if check_winner('X'):
        return -1
    if is_draw():
        return 0

    if is_max:
        best = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(False, depth+1)
                board[i] = ' '
                best = max(score, best)
        return best

    else:
        best = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(True, depth+1)
                board[i] = ' '
                best = min(score, best)
        return best

def best_move():
    best_score = -math.inf
    move = -1

    print("\nComputer evaluating moves using Minimax:\n")

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'

            score = minimax(False)

            board[i] = ' '

            print("Move", i+1, "Score =", score)

            if score > best_score:
                best_score = score
                move = i

    print("Computer chooses position:", move+1, "\n")

    return move

while True:

    print_board()

    pos = int(input("Enter position (1-9): ")) - 1

    if board[pos] != ' ':
        print("Invalid move")
        continue

    board[pos] = 'X'

    if check_winner('X'):
        print_board()
        print("Player Wins")
        break

    if is_draw():
        print_board()
        print("Draw")
        break

    comp = best_move()

    board[comp] = 'O'

    if check_winner('O'):
        print_board()
        print("Computer Wins")
        break

    if is_draw():
        print_board()
        print("Draw")
        break
