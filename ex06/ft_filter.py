#!/usr/bin/env python

def ft_filter(my_func, my_list):
    ft_filter.__doc__ = """Filters a list based on the
        bool value returned by my_func"""
    result = [a for a in my_list if my_func(a) is True]
    return result

# def ft_is_all_caps(str):
#     return str.isupper()
# names = ["ADAM", "bart", "CHARLES", "david"]
# up_names = ft_filter(ft_is_all_caps, names)
# print(f"Names were {names}")
# print(f"Up_names are {up_names}")
