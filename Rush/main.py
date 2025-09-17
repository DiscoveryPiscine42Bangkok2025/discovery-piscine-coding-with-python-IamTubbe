#!/usr/bin/env python3
from checkmate import validate_board

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
            print("Valid board configuration")
        else:
            print("Invalid board configuration")

if __name__ == "__main__":
    main()