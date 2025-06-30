import math

def print_board(board):
    print()
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
    print()

def check_winner(board):
    # Linhas, colunas e diagonais
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == "O":
        return 1
    elif winner == "X":
        return -1
    elif is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = (0,0)
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

# -----------------------------
# Jogo principal
# -----------------------------

board = [[" " for _ in range(3)] for _ in range(3)]

print("Bem-vindo ao Jogo da Velha contra a IA!")
print("Você é X, IA é O")

while True:
    print_board(board)
    if check_winner(board):
        print(f"O vencedor é: {check_winner(board)}")
        break
    if is_board_full(board):
        print("Empate!")
        break

    # Jogador humano
    while True:
        try:
            row = int(input("Escolha a linha (0-2): "))
            col = int(input("Escolha a coluna (0-2): "))
            if board[row][col] == " ":
                board[row][col] = "X"
                break
            else:
                print("Espaço já ocupado.")
        except (ValueError, IndexError):
            print("Entrada inválida. Tente de novo.")

    print_board(board)
    if check_winner(board):
        print(f"O vencedor é: {check_winner(board)}")
        break
    if is_board_full(board):
        print("Empate!")
        break

    # IA
    i, j = best_move(board)
    board[i][j] = "O"
    print("IA jogou.")