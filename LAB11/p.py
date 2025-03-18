# Constants
A = 1
B = 2
SIDE = 3
AMOVE = 'O'
BMOVE = 'X'

# Function to initialize board
def initialise():
    return [[' ' for i in range(SIDE)] for i in range(SIDE)]

# Function to print the board
def showBoard(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Function to check if there is a winner
def checkWinner(board, move, player):
    symbol = AMOVE if player == A else BMOVE
    x, y = move
    
    # Check row and column
    if all(board[x][i] == symbol for i in range(SIDE)) or all(board[i][y] == symbol for i in range(SIDE)):
        return True
    
    # Check diagonals
    if x == y and all(board[i][i] == symbol for i in range(SIDE)):
        return True
    if x + y == SIDE - 1 and all(board[i][SIDE - 1 - i] == symbol for i in range(SIDE)):
        return True
    
    return False

# BFS function to find the best move for the A
def bfsBestMove(board):
    queue = [(board, 0, None)]  # (board state, depth, last move)
    best_move = None
    
    while queue:
        current_board, depth, last_move = queue.pop(0)
        
        # Check if last move resulted in a win
        if last_move and checkWinner(current_board, last_move, A):
            return last_move
        
        # Generate all possible moves
        for i in range(SIDE):
            for j in range(SIDE):
                if current_board[i][j] == ' ':
                    new_board = [row[:] for row in current_board]
                    new_board[i][j] = AMOVE
                    queue.append((new_board, depth + 1, (i, j)))
                    if best_move is None:
                        best_move = (i, j)  # Store first available move as fallback
    
    return best_move

# DFS function to find the best move for the A
def dfsBestMove(board):
    stack = [(board, 0, None)]  # (board state, depth, last move)
    best_move = None
    
    while stack:
        current_board, depth, last_move = stack.pop()
        
        # Check if last move resulted in a win
        if last_move and checkWinner(current_board, last_move, A):
            return last_move
        
        # Generate all possible moves
        for i in range(SIDE):
            for j in range(SIDE):
                if current_board[i][j] == ' ':
                    new_board = [row[:] for row in current_board]
                    new_board[i][j] = AMOVE
                    stack.append((new_board, depth + 1, (i, j)))
                    if best_move is None:
                        best_move = (i, j)  # Store first available move as fallback
    
    return best_move

# Function to play Tic-Tac-Toe
def playTicTacToe(search):
    board = initialise()
    move_count = 0
    showBoard(board)
    
    while move_count < SIDE * SIDE:
        if move_count % 2 == 0:  # A's turn
            if search == "bfs":
                move = bfsBestMove(board)
            else:
                move = dfsBestMove(board)
            if move:
                x, y = move
                board[x][y] = AMOVE
                print("A placed", AMOVE, "at", (x + 1, y + 1))
        else:  # B's turn (random move for simplicity)
            empty_cells = []
            for i in range(SIDE):
                for j in range(SIDE):
                    if board[i][j] == ' ':
                        empty_cells.append((i, j))
            if empty_cells:
                x, y = empty_cells[0]  # Pick first available cell
                board[x][y] = BMOVE
                print("B placed", BMOVE, "at", (x + 1, y + 1))
        
        showBoard(board)
        move_count += 1
        
        if checkWinner(board, move, A):
            print("A wins!")
            return
        elif checkWinner(board, move, B):
            print("B wins!")
            return
    
    print("It's a draw!")

print("\nTic-Tac-Toe using BFS")
playTicTacToe("bfs")
print("\nTic-Tac-Toe using DFS")
playTicTacToe("dfs")