def check_winner(board):
    """
    If the player has won the game or not on Tic Tac Toe board
    """
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None and row[0] != '':
            return row[0]
    
    for col in range(3):
        if (board[0][col] == board[1][col] == board[2][col] and 
            board[0][col] is not None and board[0][col] != ''):
            return board[0][col]
    

    if (board[0][0] == board[1][1] == board[2][2] and 
        board[0][0] is not None and board[0][0] != ''):
        return board[0][0]
    
    if (board[0][2] == board[1][1] == board[2][0] and 
        board[0][2] is not None and board[0][2] != ''):
        return board[0][2]
    
    return None


def test_tic_tac_toe():
    board1 = [
        ['X', 'X', 'X'],
        ['O', 'O', None],
        [None, None, None]
    ]
    assert check_winner(board1) == 'X', "Test case 1 failed"

    board2 = [
        ['X', 'O', 'X'],
        ['X', 'O', None],
        [None, 'O', None]
    ]
    assert check_winner(board2) == 'O', "Test case 2 failed"

    board3 = [
        ['X', 'O', None],
        ['O', 'X', None],
        ['O', None, 'X']
    ]
    assert check_winner(board3) == 'X', "Test case 3 failed"

    board4 = [
        ['X', 'O', 'X'],
        ['O', None, None],
        [None, None, None]
    ]
    assert check_winner(board4) is None, "Test case 4 failed"

    print("All test cases passed!")

if __name__ == "__main__":
    test_tic_tac_toe() 