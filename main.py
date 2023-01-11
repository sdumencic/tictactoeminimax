import copy


def minimax(board, depth, is_maximizing):
    if check_for_win(board, "X"):
        return -1
    elif check_for_win(board, "O"):
        return 1
    elif depth == 0 or check_for_tie(board):
        return 0

    if is_maximizing:
        best_value = -float("inf")
        symbol = "X"
    else:
        best_value = float("inf")
        symbol = "O"

    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                new_board = copy.deepcopy(board)
                new_board[i][j] = symbol
                value = minimax(new_board, depth - 1, not is_maximizing)
                if is_maximizing:
                    best_value = max(best_value, value)
                else:
                    best_value = min(best_value, value)

    return best_value


def get_best_move(board):
    best_value = -float("inf")
    best_move = (0, 0)
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                board[i][j] = "O"
                value = minimax(board, 2, False)
                board[i][j] = ""
                if value > best_value:
                    best_value = value
                    best_move = (i, j)
    return best_move


def play_game():
    board = [["" for _ in range(3)] for _ in range(3)]

    while True:
        print_board(board)

        x_move = input("Your move (x y): ").split()
        x_move = (int(x_move[0]), int(x_move[1]))
        if board[x_move[0]][x_move[1]] != "":
            print("Invalid move!")
            continue

        board[x_move[0]][x_move[1]] = "X"
        if check_for_win(board, "X"):
            print("You won!")
            break
        elif check_for_tie(board):
            print("It's a tie!")
            break

        o_move = get_best_move(board)
        board[o_move[0]][o_move[1]] = "O"
        if check_for_win(board, "O"):
            print("AI won!")
            break
        elif check_for_tie(board):
            print("It's a tie!")
            break


def print_board(board):
    for row in board:
        print(" ".join(row))


def check_for_win(board, symbol):
    # Checking the rows
    for i in range(3):
        if board[i][0] == symbol and board[i][1] == symbol and board[i][2] == symbol:
            return True
    # Checking the columns
    for i in range(3):
        if board[0][i] == symbol and board[1][i] == symbol and board[2][i] == symbol:
            return True
    # Checking the diagonals
    if board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol:
        return True
    if board[0][2] == symbol and board[1][1] == symbol and board[2][0] == symbol:
        return True
    return False


def check_for_tie(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                return False
    return True


play_game()
