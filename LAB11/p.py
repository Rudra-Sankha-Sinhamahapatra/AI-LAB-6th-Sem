# Constants
A = 1
B = 2
SIDE = 3
AMOVE = 'O'
BMOVE = 'X'


def initialise():
    return [[' ' for i in range(SIDE)] for i in range(SIDE)]


def showBoard(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def checkWinner(board, move, player):
    symbol = AMOVE if player == A else BMOVE
    x, y = move

    if all(board[x][i] == symbol for i in range(SIDE)) or all(board[i][y] == symbol for i in range(SIDE)):
        return True
    
  
    if x == y and all(board[i][i] == symbol for i in range(SIDE)):
        return True
    if x + y == SIDE - 1 and all(board[i][SIDE - 1 - i] == symbol for i in range(SIDE)):
        return True
    
    return False


def bfsBestMove(board):
    queue = [(board, 0, None)]
    best_move = None
    
    while queue:
        current_board, depth, last_move = queue.pop(0)
        

        if last_move and checkWinner(current_board, last_move, A):
            return last_move
        

        for i in range(SIDE):
            for j in range(SIDE):
                if current_board[i][j] == ' ':
                    new_board = [row[:] for row in current_board]
                    new_board[i][j] = AMOVE
                    queue.append((new_board, depth + 1, (i, j)))
                    if best_move is None:
                        best_move = (i, j) 
    
    return best_move


def dfsBestMove(board):
    stack = [(board, 0, None)] 
    best_move = None
    
    while stack:
        current_board, depth, last_move = stack.pop()
        
        if last_move and checkWinner(current_board, last_move, A):
            return last_move
        
        for i in range(SIDE):
            for j in range(SIDE):
                if current_board[i][j] == ' ':
                    new_board = [row[:] for row in current_board]
                    new_board[i][j] = AMOVE
                    stack.append((new_board, depth + 1, (i, j)))
                    if best_move is None:
                        best_move = (i, j) 
    
    return best_move


def playTicTacToe(search):
    board = initialise()
    move_count = 0
    showBoard(board)
    
    while move_count < SIDE * SIDE:
        if move_count % 2 == 0: 
            if search == "bfs":
                move = bfsBestMove(board)
            else:
                move = dfsBestMove(board)
            if move:
                x, y = move
                board[x][y] = AMOVE
                print("A placed", AMOVE, "at", (x + 1, y + 1))
        else:  
            empty_cells = []
            for i in range(SIDE):
                for j in range(SIDE):
                    if board[i][j] == ' ':
                        empty_cells.append((i, j))
            if empty_cells:
                x, y = empty_cells[0] 
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