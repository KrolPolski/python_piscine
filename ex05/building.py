#!/usr/bin/env python
import sys


def count(str):
    count.__doc__ = """Iterates through the string and
                    counts each character by category."""
    chars = len(str)
    up = 0
    lo = 0
    pu = 0
    di = 0
    sp = 0
    i = 0

    while i < len(str):
        if '9' >= str[i] >= '0':
            di += 1
        elif 'Z' >= str[i] >= 'A':
            up += 1
        elif 'z' >= str[i] >= 'a':
            lo += 1
        elif '\b' <= str[i] <= ' ':
            sp += 1
        elif '!' <= str[i] <= '/' or ':' <= str[i] <= '@' \
                or '[' <= str[i] <= '`' or '{' <= str[i] <= '~':
            pu += 1
        i += 1
    print(f"The text contains {chars} characters:")
    print(f"{up} upper letters")
    print(f"{lo} lower letters")
    print(f"{pu} punctuation marks")
    print(f"{sp} spaces")
    print(f"{di} digits")


def main():
    main.__doc__ = """This program takes a single string argument
    and displays the sums of its upper-case characters, lower-case
    characters, punctuation characters, digits and spaces."""
    assert len(sys.argv) < 3, "Too many arguments provided"
    if len(sys.argv) != 2 or sys.argv[1] is None:
        try:
            str = input("What is the text to count? ")
        except EOFError:
            print("\nYou failed to provide a string to count.")
            return
    else:
        str = sys.argv[1]
    count(str)


main()
