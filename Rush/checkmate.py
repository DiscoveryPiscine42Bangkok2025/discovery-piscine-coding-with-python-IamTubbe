def validate_board(board):
    
    n = len(board)

    if not all(len(row) == n for row in board):
        print("กระดานไม่เป็นสี่เหลี่ยมจัตุรัส")
        return False

    king_count = sum(row.count('K') for row in board)
    if king_count == 0:
        print("ไม่มี King บนกระดาน")
        return False
    elif king_count > 1:
        print("มี King มากกว่า 1 ตัว")
        return False

    piece_counts = {'P': 0, 'B': 0, 'R': 0, 'Q': 0, 'K': 0}
    for row in board:
        for cell in row:
            if cell in piece_counts:
                piece_counts[cell] += 1
            elif cell != '.':
                print("ใช้ได้เฉพาะ P, B, R, Q, K หรือ .")
                return False

    if piece_counts['Q'] > 1:
        print("มี Queen มากกว่า 1 ตัว")
        return False
    if piece_counts['B'] > 2:
        print("มี Bishop มากกว่า 2 ตัว")
        return False
    if piece_counts['P'] > 8:
        print("มี Pawn มากกว่า 8 ตัว")
        return False
    if piece_counts['R'] > 2:
        print("มี Rook มากกว่า 2 ตัว")
        return False

    return True
