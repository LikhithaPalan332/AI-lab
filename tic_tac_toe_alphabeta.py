import math
board = [' ']*9
def print_board():
    print()
    for i in range(0,9,3):
        print(board[i],"|",board[i+1],"|",board[i+2])
        if i<6:
            print("--+---+--")
    print()

def check_winner(p):
    wins=[[0,1,2],[3,4,5],[6,7,8],
          [0,3,6],[1,4,7],[2,5,8],
          [0,4,8],[2,4,6]]
    
    for w in wins:
        if board[w[0]]==board[w[1]]==board[w[2]]==p:
            return True
    return False
def is_draw():
    return ' ' not in board

def alphabeta(is_max, alpha, beta):

    if check_winner('O'):
        return 1
    if check_winner('X'):
        return -1
    if is_draw():
        return 0

    if is_max:
        best=-math.inf
        for i in range(9):
            if board[i]==' ':
                board[i]='O'
                score=alphabeta(False,alpha,beta)
                board[i]=' '
                best=max(best,score)
                alpha=max(alpha,best)

                if beta<=alpha:
                    break
        return best

    else:
        best=math.inf
        for i in range(9):
            if board[i]==' ':
                board[i]='X'
                score=alphabeta(True,alpha,beta)
                board[i]=' '
                best=min(best,score)
                beta=min(beta,best)

                if beta<=alpha:
                    break
        return best
def best_move():

    best_score=-math.inf
    move=-1

    print("\nComputer evaluating moves:\n")

    for i in range(9):
        if board[i]==' ':
            board[i]='O'
            score=alphabeta(False,-math.inf,math.inf)
            board[i]=' '
            print("Move",i+1,"Score =",score)

            if score>best_score:
                best_score=score
                move=i

    return move
  
while True:
    print_board()
    try:
        pos=int(input("Enter position (1-9): "))-1
    except:
        print("Enter a number between 1 and 9")
        continue
    if pos<0 or pos>8 or board[pos]!=' ':
        print("Invalid move, try again")
        continue

    board[pos]='X'
    if check_winner('X'):
        print_board()
        print("Player Wins")
        break

    if is_draw():
        print_board()
        print("Game Draw")
        break

    comp=best_move()
    board[comp]='O'

    if check_winner('O'):
        print_board()
        print("Computer Wins")
        break

    if is_draw():
        print_board()
        print("Game Draw")
        break
