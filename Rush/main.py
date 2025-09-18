#!/usr/bin/env python3
from checkmate import validate_board, is_king_checked

def main():
    board = [
        "........",
        "........",
        "...R....",
        "....K...",
        ".....P..",
        "........",
        "........",
        "........"
    ]

    if validate_board(board):

        if is_king_checked(board):
            print("Success")
        else:
            print("Fail")

if __name__ == "__main__":
    main()