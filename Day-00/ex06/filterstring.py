#!/usr/bin/env python

import sys


def main():
    sys.tracebacklimit = 0
    assert len(sys.argv) == 3, "Exactly two arguments required"
    try:
        length = int(sys.argv[2])
    except ValueError:
        print("Second argument should be a number")
        return
    str = sys.argv[1]
    for x in str:
        assert (x == ' ' or '0' <= x <= '9'
                or 'A' <= x <= 'Z' or 'a' <= x <= 'z'), \
                    'No special characters or punctuation allowed in string'
    str_list = str.split()
    result = [item for item in str_list if len(item) > length]
    print(result)


main()
