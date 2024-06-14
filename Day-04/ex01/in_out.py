#!/usr/bin/env python
"""Write a function that returns the square of argument, a function that returns the
Exponentiation of argument by himself and a function that takes as argument a number
and a function, it returns an object that when called returns the result of the arguments
calculation."""

def square(x: int | float) -> int | float:
    return x * x
def pow(x: int | float) -> int | float:
    return x ** x

def outer(x: int | float, function) -> object:
    def ret(x, function):
        return (function(x))
    return ret
#def inner() -> float:
#your code here
