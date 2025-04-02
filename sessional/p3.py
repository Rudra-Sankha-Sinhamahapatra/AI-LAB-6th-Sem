'''
Write a function to fill the 3X3 grid with 1 and 2. 
Player 1 enter the value from the keyboard and player 
2 (computer) automatically enter 2 in the blank space 
after player 1 enter the input
'''
import random

def humanMove(board) :
    print("Give input files \n")
    print("Enter the row column separated by space \n")
    row,col = map(int, input().split())

    if 1<=row <=3 and 1 <=col<=3:
        row-=1
        col-=1
        if board[row][col] == 0:
            board[row][col] = 1
            return True
        else :
            print("That position is already taken \n")
    else :
        print("Invalid Numbers, numbers should be between 1 and 3")



def computerMove(board):
    empty_space = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                empty_space.append((i,j))

    if empty_space :
        row,col = random.choice(empty_space)
        board[row][col] = 2
        print(f"\n Computer placed 2 at position: row {row+1} col:{col+1} ")
        return True
    return False


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

def main():
    board = [[0 for _ in range(3)] for _ in range(3)]
    
    print("\nWelcome to 3x3 Matrix Game!")
    print("Values: 0 = Empty, 1 = Human, 2 = Computer")
    print("\nExample board with row and column numbers:")
    print_board(board)

    
    while True:

        print("\nCurrent board state:")
        print_board(board)
        humanMove(board)
        
      
        if all(0 not in row for row in board):
            print("\nGame Over - Board is full!")
            print("Final board state:")
            print_board(board)
            break
            
  
        computerMove(board)
        

        if all(0 not in row for row in board):
            print("\nGame Over - Board is full!")
            print("Final board state:")
            print_board(board)
            break

if __name__ == "__main__":
    main() 