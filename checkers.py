# Learnign how to make a checkers w/ claude sonnet 3.5 -> Probs not the best way to learn.


# Make the board

def create_board():
    board = []
    for row in range(8):
        board_row = []
        for col in range(8):
            if row < 3 and (row + col) % 2 == 1:
                board_row.append('b')  # Black pieces
            elif row > 4 and (row + col) % 2 == 1:
                board_row.append('w')  # White pieces
            else:
                board_row.append(' ')  # Empty spaces
        board.append(board_row)
    return board

def print_board(board):
    print('   0 1 2 3 4 5 6 7')  # Column numbers
    print('  ─────────────────')
    for i, row in enumerate(board):
        print(f'{i} │', end=' ')  # Row numbers
        for cell in row:
            print(cell, end=' ')
        print('│')
    print('  ─────────────────')

def is_valid_move(board, start_row, start_col, end_row, end_col, player):
    # Check if coordinates are within bounds
    if not (0 <= start_row <= 7 and 0 <= start_col <= 7 and 
            0 <= end_row <= 7 and 0 <= end_col <= 7):
        return False

    # Check if destination is empty
    if board[end_row][end_col] != ' ':
        return False

    # Check if selected piece belongs to current player
    piece = board[start_row][start_col]
    if (player == 'white' and piece != 'w') or (player == 'black' and piece != 'b'):
        return False

    # Check if move is diagonal and one space
    row_diff = abs(end_row - start_row)
    col_diff = abs(end_col - start_col)
    if row_diff != 1 or col_diff != 1:
        return False

    # Check direction (white moves up, black moves down)
    if player == 'white' and end_row >= start_row:
        return False
    if player == 'black' and end_row <= start_row:
        return False

    return True

def play_checkers():
    board = create_board()
    current_player = 'black'  # Black goes first
    
    while True:
        print_board(board)
        print(f"\n{current_player.capitalize()}'s turn")
        
        try:
            # Get move from player
            start = input("Enter start position (row col): ")
            if start.lower() == 'quit':
                break
            start_row, start_col = map(int, start.split())
            
            end = input("Enter end position (row col): ")
            if end.lower() == 'quit':
                break
            end_row, end_col = map(int, end.split())
            
            # Validate and make move
            if is_valid_move(board, start_row, start_col, end_row, end_col, current_player):
                # Move piece
                board[end_row][end_col] = board[start_row][start_col]
                board[start_row][start_col] = ' '
                
                # Switch players
                current_player = 'white' if current_player == 'black' else 'black'
            else:
                print("\nInvalid move! Try again.")
        
        except ValueError:
            print("\nInvalid input! Use format: row col (e.g., 2 1)")
        except IndexError:
            print("\nInvalid position! Numbers must be between 0 and 7")
        
        print()  # Empty line for readability

if __name__ == "__main__":
    print("Welcome to Simple Checkers!")
    print("Enter positions as: row col (e.g., 2 1)")
    print("Type 'quit' to end the game")
    print()
    play_checkers()