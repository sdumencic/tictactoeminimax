import copy

SCORE_WIN = 1
SCORE_DRAW = 0
SCORE_LOSS = -1


def minimax(board, depth, is_maximizing):
    # is_maximizing je isto sto i IS_AI
    if check_for_win(board, "X"):
        return SCORE_LOSS
    elif check_for_win(board, "O"):
        return SCORE_WIN
    elif depth <= 0 or check_for_tie(board):
        return SCORE_DRAW

    if is_maximizing:
        # We are simulating this round as AI
        best_score = SCORE_LOSS
        symbol = "O"
    else:
        # We are simulating this round as Player
        best_score = SCORE_WIN
        symbol = "X"

    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                new_board = copy.deepcopy(board)
                new_board[i][j] = symbol
                # print("")
                # print("")
                # print_board(new_board)
                score = minimax(new_board, depth - 1, not is_maximizing)

                if is_maximizing:
                    best_score = max(best_score, score)
                else:
                    best_score = min(best_score, score)

    return best_score


def get_best_move(board):
    best_move = (0, 0)  # Set to first field regardless of if it is available
    best_score = SCORE_LOSS  # Set to worst case scenario
    depth = 9 - get_move_counter(board)

    # We are on our first AI move and player has not put it into center. Statistically,
    # center is the best option, so always do that in that case.
    if depth == 8 and board[1][1] == "":
        return (1, 1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                # We are on our first AI move and player has put it into center, just
                # skip all other calculations since it does not really matter at this
                # point where we put it.
                if depth == 8:
                    return (i, j)

                board[i][j] = "O"
                value = minimax(board, depth - 1, False)
                board[i][j] = ""

                if value > best_score:
                    best_score = value
                    best_move = (i, j)
    return best_move


def get_move_counter(board):
    count = 0
    for row in board:
        for el in row:
            if el != "":
                count += 1
    return count


def play_game():
    # 3x3 Prazan ""
    board = [["" for _ in range(3)] for _ in range(3)]

    while True:
        print_board(board)

        # Provjeri ako je doslo do pobjede ili izjednacenja i prekini igru
        if check_for_win(board, "X"):
            print("You won!")
            break
        elif check_for_win(board, "O"):
            print("AI won!")
            break
        elif check_for_tie(board):
            print("It's a tie!")
            break

        # Input dio i odradivanje player dijela
        x_move = input("Your move (x y): ").split()
        x_move = (int(x_move[0]), int(x_move[1]))  # will save as tuple e.g. (3, 3)
        try:
            if board[x_move[0]][x_move[1]] != "":
                raise Exception("Invalid move!")
        except Exception:
            print("Invalid move!")
            continue
        board[x_move[0]][x_move[1]] = "X"

        # Odradi AI dio
        o_move = get_best_move(board)
        board[o_move[0]][o_move[1]] = "O"


def print_board(board):
    for row in board:
        print("|".join([el if el != "" else " " for el in row]))
        print("-----")


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
