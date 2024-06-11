#!/usr/bin/env python

import imageio.v3 as iio


def ft_load(path: str) -> str:
    ft_load.__doc__ = \
        """Prints shape and pixel content of desired image"""
    try:
        img = iio.imread(path)
    except FileNotFoundError:
        print(f"The file '{path}' does not exist.")
        return
    except PermissionError:
        print(f"You don't have permissions to read '{path}'")
        return
    print(f"The shape of the image is {img.shape}")
    for a in range(len(img)):
        for b in range(len(img[a])):
            print(img[a][b])
    return img


def main():
    main.__doc__ = "Testing function for ft_load"
    ft_load("./test.jpg")
#    ft_load("nopers.jpg")
#    ft_load("no_perm.jpg")


if __name__ == "__main__":
    main()
