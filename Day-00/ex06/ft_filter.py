#!/usr/bin/env python

def ft_filter(my_func, my_list):
    ft_filter.__doc__ = """\
filter(function or None, iterable) --> filter object\n
Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.
"""
    if my_func is None:
        result = [a for a in my_list if a == True]
        return result
    result = [a for a in my_list if my_func(a) is True]
    return result


#def ft_is_all_caps(str):
#    return str.isupper()


# names = ["ADAM", "bart", "CHARLES", "david"]
# up_names = ft_filter(ft_is_all_caps, names)
# ref_names = filter(ft_is_all_caps, names)
# print(f"Names were {names}")
# print(f"Up_names are {up_names}")
# print(f"Ref_names are {ref_names}")
# print(filter.__doc__)
# print(ft_filter.__doc__)
