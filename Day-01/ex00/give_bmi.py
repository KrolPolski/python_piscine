#!/usr/bin/env python

def give_bmi(height: list[int | float], weight: list[int | float]) \
        -> list[int | float]:
    give_bmi.__doc__ = """Returns a list of BMI values, calculated
    from the parameters. The formula is BMI = kg/m2 where kg is a
    person’s weight in kilograms and m2 is their height in metres squared."""

    assert type(height) is list, "Height must be a list of numbers"
    assert type(weight) is list, "Weight must be a list of numbers"
    if len(height) > len(weight):
        usable_len = len(weight)
    elif len(height) <= len(weight):
        usable_len = len(height)
    if len(height) != len(weight):
        print("Warning: Lists are not the same length")
        print("results will be truncated to the length of the shorter list")
    for x in height:
        assert type(x) is int or type(x) is float, "Invalid height data type"
    for y in weight:
        assert type(y) is int or type(y) is float, "Invalid weight data type"
    print("Must have valid data, moving forward")
    result = []
    for i in range(usable_len):
        result.append(weight[i] / (height[i] ** 2))
    return result


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    assert type(bmi) is list, "BMI parameter must be a list"
    assert type(limit) is int or type(limit) is float, "Limit must be a number"
    result = []
    for a in bmi:
        if a > limit:
            result.append(True)
        else:
            result.append(False)
    return result


def main():
    result = give_bmi([1.65, 2, 2.1], [100, 120])
    print(result)


if __name__ == "__main__":
    main()
