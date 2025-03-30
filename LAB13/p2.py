import random

def print_board(board):
    print("\n    1   2   3  (columns)")  
    for i in range(3):
        print(f"{i+1} ", end="")  
        for j in range(3):
            print(f" {board[i][j]} ", end="")
            if j < 2:
                print("|", end="")
        print() 
        if i < 2:
            print("   -----------")
    print("(rows)\n")

def make_move(board):
    while True:
        try:
            print("\nExample input format: '2 3' for row 2, column 3")
            print("Enter row and column (1-3) separated by space: ")
            row, col = map(int, input().split())

            if 1 <= row <= 3 and 1 <= col <= 3:
                row -= 1
                col -= 1
                if board[row][col] == 0:
                    board[row][col] = 1  
                    return True
                else:
                    print("That position is already taken! Try again.")
            else:
                print("Invalid input! Numbers must be between 1 and 3.")
        except ValueError:
            print("Invalid input! Please enter two numbers separated by space.")

def computer_turn(board):
    empty_spots = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                empty_spots.append((i, j))
    
    if empty_spots:
        row, col = random.choice(empty_spots)
        board[row][col] = 2  
        print(f"\nComputer placed 2 at position: row {row+1}, column {col+1}")
        return True
    return False

def main():
    board = [[0 for _ in range(3)] for _ in range(3)]
    
    print("\nWelcome to 3x3 Matrix Game!")
    print("Values: 0 = Empty, 1 = Human, 2 = Computer")
    print("\nExample board with row and column numbers:")
    print_board(board)
    
    print("How to play:")
    print("1. Enter your move as 'row column' (e.g., '2 3' for row 2, column 3)")
    print("2. Computer will make a random move after your turn")
    print("3. Game continues until no empty spaces (0s) are left")

    print("\nExample moves:")
    print("- To place 1 in first row, first column: enter '1 1'")
    print("- To place 1 in second row, third column: enter '2 3'")
    print("- To place 1 in third row, second column: enter '3 2'")
    
    while True:

        print("\nCurrent board state:")
        print_board(board)
        make_move(board)
        
      
        if all(0 not in row for row in board):
            print("\nGame Over - Board is full!")
            print("Final board state:")
            print_board(board)
            break
            
  
        computer_turn(board)
        

        if all(0 not in row for row in board):
            print("\nGame Over - Board is full!")
            print("Final board state:")
            print_board(board)
            break

if __name__ == "__main__":
    main() 