#!/usr/bin/env python

def ft_mean(args: any):
    total = 0
    for i in range(len(args)):
        print(args[i])
        total += (args[i])
    return total / len(args) 


def ft_statistics(*args: any, **kwargs: any) -> None:
    if len(args) == 0 or len(kwargs) == 0:
        print("ERROR")
        return
    for kwarg in kwargs:
        if kwargs[kwarg] == 'mean':
            print(f"mean : {ft_mean(args)}")
        print(f"kwarg: {kwarg}: {kwargs[kwarg]}")


def main():
    print("Arg print test")
    ft_statistics(2, 4, 8, 16, first='mean')
    print("Kwarg print test")
    ft_statistics(first='plus', second='minus', third='multiply', fourth='divide')
    print("empty arg test")
    ft_statistics()

if __name__=='__main__':
    main()