#!/usr/bin/env python
import sys
import string


def count(str):
    chars = len(str)
    up = 0
    lo = 0
    pu = 0
    di = 0
    sp = 0
    i = 0

    while i < len(str):
        if str[i] in string.digits:
            di += 1
        elif str[i] in string.ascii_uppercase:
            up += 1
        elif str[i] in string.ascii_lowercase:
            lo += 1
        elif str[i] in string.whitespace:
            sp += 1
        elif str[i] in string.punctuation:
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
            print("\nYou failed to provide a string to count. No cookie for you.")
            return
    else:
        str = sys.argv[1]
    count(str)


main()
