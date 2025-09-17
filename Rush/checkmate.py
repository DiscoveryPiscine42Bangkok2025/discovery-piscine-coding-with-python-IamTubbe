def validate_board(board):
    n = len(board)

    if not all(len(row) == n for row in board):
        print("Board is not square")
        return False

    king_count = sum(row.count('K') for row in board)
    if king_count == 0:
        print("No King on the board")
        return False
    elif king_count > 1:
        print("More than 1 King on the board")
        return False

    piece_counts = {'P': 0, 'B': 0, 'R': 0, 'Q': 0, 'K': 0}
    for row in board:
        for cell in row:
            if cell in piece_counts:
                piece_counts[cell] += 1
            elif cell != '.':
                print("Only P, B, R, Q, K or . are allowed")
                return False

    if piece_counts['Q'] > 1:
        print("More than 1 Queen on the board")
        return False
    
    if piece_counts['B'] > 2:
        print("More than 2 Bishops on the board")
        return False
    
    if piece_counts['P'] > 8:
        print("More than 8 Pawns on the board")
        return False
    
    if piece_counts['R'] > 2:
        print("More than 2 Rooks on the board")
        return False

    return True
