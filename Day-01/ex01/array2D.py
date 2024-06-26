#!/usr/bin/env python

def slice_me(family: list, start: int, end: int) -> list:
    slice_me.__doc__ = """Returns a truncated list,
        based on the start and end indexes"""
    assert type(family) is list, "family parameter must be a list"
    assert type(start) is int, "Start must be an integer"
    assert type(end) is int, "End must be an integer"
    assert len(family) * -1 <= start < len(family), "Invalid start index"
    assert len(family) * -1 < end <= len(family), "Invalid end index"
    for a in family:
        assert len(a) == len(family[0]), "Sublists must be the same length"
    print(f"My shape is : ({len(family)}, {len(family[0])})")
    result = family[start: end]
    print(f"My new shape is : ({len(result)}, {len(result[0])})")
    return result


def main():
    slice_me([[2, 100], [1.65, 70], [1.75, 80]], 0, 2)
    slice_me([[2, 100], [1.65, 70], [1.75, 80]], 0, 1)


if __name__ == "__main__":
    main()
