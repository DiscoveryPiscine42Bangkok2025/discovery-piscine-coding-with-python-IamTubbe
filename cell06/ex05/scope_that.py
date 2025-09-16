#!/usr/bin/env python3
def add_one(x):
    return x + 1

def main():
    num = 5
    print("Before calling add_one :", num)

    num = add_one(num)
    print("After calling add_one :", num)

main()