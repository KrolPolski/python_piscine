#!/usr/bin/env python

def ft_mean(args: any):
    total = 0
    for i in range(len(args)):
        print(args[i])
        total += (args[i])
    return total / len(args) 

def ft_median(args: any):
   # print(args)
    sorted_args = sorted(args)
    #print(sorted_args)
    if len(sorted_args) % 2 == 1:
        return sorted_args[(len(sorted_args) // 2)]
    else:
        return ft_mean([sorted_args[(len(sorted_args)// 2)], sorted_args[(len(sorted_args)// 2) - 1]])

def ft_quartile(args: any):
    #print(args)
    sorted_args = sorted(args)
   #print(sorted_args)
    length = len(sorted_args)
    median = ft_median(sorted_args)
    lower_half = [arg for arg in sorted_args if arg <= median]
    upper_half = [arg for arg in sorted_args if arg >= median]
    print(f"lower_half is {lower_half}")
    print(f"upper-half is {upper_half}")
    return ([float(ft_median(lower_half)), float(ft_median(upper_half))])

def ft_statistics(*args: any, **kwargs: any) -> None:
    if len(args) == 0 or len(kwargs) == 0:
        print("ERROR")
        return
    for kwarg in kwargs:
        if kwargs[kwarg] == 'mean':
            print(f"mean : {ft_mean(args)}")
        elif kwargs[kwarg] == 'median':
            print(f"median : {ft_median(args)}")
        elif kwargs[kwarg] == 'quartile':
            print(f"quartile : {ft_quartile(args)}")
        else:
            print("ERROR")
            return
        print(f"kwarg: {kwarg}: {kwargs[kwarg]}")


def main():
    print("mean test")
    ft_statistics(2, 4, 8, 16, first='mean')
    print("median test")
    ft_statistics(5, 3, 1, 2, 4, first='median')
    ft_statistics(3, 2, 1, 4, first='median')
    ft_statistics(1, first='median')
    print("quartile tests")
    print("For list [5,4,3,2,1,6,7,8,10,9]")
    ft_statistics(5,4,3,2,1,6,7,8,10,9, first='quartile')
    ft_statistics(first='plus', second='minus', third='multiply', fourth='divide')
    print("empty arg test")
    ft_statistics()

if __name__=='__main__':
    main()