#!/usr/bin/env python

def slice_me(family: list, start: int, end: int) -> list:
    assert type(family) is list, "family parameter must be a list"
    assert type(start) is int, "Start must be an integer"
    assert type(end) is int, "End must be an integer"
    # add assert for valid indexes
    for a in family:
        assert len(a) == len(family[0]), "Sublists must be the same length"
    print(f"My shape is : ({len(family)}, {len(family[0])})")
    result = family[start: end]
    print(f"My new shape is : ({len(result)}, {len(result[0])})")
    return result


def main():
    slice_me([[2, 100], [1.65, 70], [1.75, 80]], 0, 2)


if __name__ == "__main__":
    main()
