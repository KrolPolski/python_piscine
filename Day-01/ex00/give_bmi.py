#!/usr/bin/env python

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
# your code here
# The formula is BMI = kg/m2 where kg is a person’s weight in kilograms and m2 is their height in metres squared.
# You have to handle error cases if the lists are not the same size, are not int or float...
    if len(height) > len(weight):
        usable_len = len(weight)
    elif len(height) <= len(weight):
        usable_len = len(height)
    for x in height:
        assert type(x) is int or type(x) is float, "Invalid height data type"
    for y in weight:
        assert type(y) is int or type(y) is float, "Invalid weight data type"
    print("Must have valid data")    

#def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
#your code

def main():
    give_bmi([2, 2.1, 'a'], [100, 120])

if __name__ == "__main__":
  main()