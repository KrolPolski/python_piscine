#!/usr/bin/env python

def ft_statistics(*args: any, **kwargs: any) -> None:
    for arg in args:
        print(f"arg: {arg}")
    for kwarg in kwargs:
        print(f"kwarg: {kwarg}: {kwargs[kwarg]}")
#your code here

def main():
    print("Arg print test")
    ft_statistics(2, 4, 8, 16)
    print("Kwarg print test")
    ft_statistics(first='plus', second='minus', third='multiply', fourth='divide')

if __name__=='__main__':
    main()