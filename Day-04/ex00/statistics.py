#!/usr/bin/env python

def ft_mean(args: any):
    total = 0
    for i in range(len(args)):
        total += (args[i])
    return total / len(args)


def ft_median(args: any):
    sorted_args = sorted(args)
    if len(sorted_args) % 2 == 1:
        return sorted_args[(len(sorted_args) // 2)]
    else:
        return ft_mean([sorted_args[(len(sorted_args) // 2)],
                        sorted_args[(len(sorted_args) // 2) - 1]])


def ft_quartile(args: any):
    sorted_args = sorted(args)
    median = ft_median(sorted_args)
    lower_half = [arg for arg in sorted_args if arg <= median]
    upper_half = [arg for arg in sorted_args if arg >= median]
    return ([float(ft_median(lower_half)), float(ft_median(upper_half))])


def ft_variance(args: any):
    sorted_args = sorted(args)
    mean = ft_mean(sorted_args)
    deviations = [i - mean for i in sorted_args]
    squared_deviations = [i ** 2 for i in deviations]
    variance = ft_mean(squared_deviations)
    return variance


def ft_std(args: any):
    return ft_variance(args) ** 0.5


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
        elif kwargs[kwarg] == 'std':
            print(f"std : {ft_std(args)}")
        elif kwargs[kwarg] == 'var':
            print(f"var : {ft_variance(args)}")
        else:
            print("ERROR")


def main():
    print("mean test")
    ft_statistics(2, 4, 8, 16, first='mean')
    print("median test")
    ft_statistics(5, 3, 1, 2, 4, first='median')
    ft_statistics(3, 2, 1, 4, first='median')
    ft_statistics(1, first='median')
    print("quartile tests")
    print("For list [5,4,3,2,1,6,7,8,10,9,11]")
    ft_statistics(5, 4, 3, 2, 1, 6, 7, 8, 10, 9, first='quartile')
    ft_statistics(5, 4, 3, 2, 1, 6, 7, 8, 10, 9, first='std')
    print("empty arg test")
    ft_statistics()


if __name__ == '__main__':
    main()
