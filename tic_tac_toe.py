import math

board = ["-" for i in range(9)]

def print_board():
    for i in range(0, 9, 3):
        print("|",board[i], "|", board[i+1], "|", board[i+2], "|")
    print()

def check_winner(player):
    wins = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    
    for w in wins:              
        if board[w[0]] == board[w[1]] == board[w[2]] == player:
            return True          
    return False                 


def is_draw():
    return "-" not in board

def minimax(is_max):
    if check_winner("O"):
        return 1
    if check_winner("X"):
        return -1
    if is_draw():
        return 0

    if is_max:
        best = -math.inf
        for i in range(9):
            if board[i] == "-":
                board[i] = "O"
                score = minimax(False)
                board[i] = "-"
                best = max(best, score)
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == "-":
                board[i] = "X"
                score = minimax(True)
                board[i] = "-"
                best = min(best, score)
        return best

def best_move():
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == "-":
            board[i] = "O"
            score = minimax(False)
            board[i] = "-"
            if score > best_score:
                best_score = score
                move = i
    return move

def play_game():
    print("You = X | AI = O")
    print("Positions: 1-9\n")

    while True:
        print_board()

        while True:
            human = int(input("Your move (1-9): "))
            if human < 1 or human > 9:
                print("Invalid position! Choose between 1-9.")
                continue
            if board[human-1] == "-":
                board[human-1] = "X"
                print_board()
                break
            else:
                print("It is already taken!")

        if check_winner("X"):
            print_board()
            print("You win!")
            break
        if is_draw():
            print_board()
            print("Draw!")
            break

        print("AI is making a move...")

        ai = best_move()
        board[ai] = "O"

        if check_winner("O"):
            print_board()
            print("AI wins!")
            break
        if is_draw():
            print_board()
            print("Draw!")
            break

play_game()

choice=input("you need to play again(y/n): ")
if 'y' in choice or 'Y' in choice:
    board = ["-" for i in range(9)]
    play_game()