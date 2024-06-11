#!/usr/bin/env python

from load_image import ft_load
import matplotlib.pyplot as plt


def ft_invert(array):
    ft_invert.__doc__ = "Inverts each pixel of an image"
    inv_img = (array)
    print("Beginning inversion process")
    a = 0
    b = 0
    c = 0
    while a < len(inv_img):
        while b < len(inv_img[0]):
            while c < len(inv_img[0][0]):
                inv_img[a][b][c] = 255 - inv_img[a][b][c]
                c += 1
            c = 0
            b += 1
        b = 0
        a += 1
    print("Inversion complete")
    return inv_img


def ft_red(array):
    ft_red.__doc__ = "disables green and blue channels"
    inv_img = (array)
    print("Beginning reddening process")
    a = 0
    b = 0
    c = 1
    while a < len(inv_img):
        while b < len(inv_img[0]):
            while c < len(inv_img[0][0]):
                inv_img[a][b][c] = 0
                c += 1
            c = 1
            b += 1
        b = 0
        a += 1
    print("Reddening complete")
    return inv_img


def ft_green(array):
    ft_green.__doc__ = "disables red and blue channels"
    inv_img = (array)
    print("Beginning greening process")
    a = 0
    b = 0
    c = 0
    while a < len(inv_img):
        while b < len(inv_img[0]):
            while c < len(inv_img[0][0]):
                inv_img[a][b][c] = 0
                c += 2
            c = 0
            b += 1
        b = 0
        a += 1
    print("greening complete")
    return inv_img


def ft_blue(array):
    ft_blue.__doc__ = "disables red and green channels"
    inv_img = (array)
    print("Beginning blueing process")
    a = 0
    b = 0
    c = 0
    while a < len(inv_img):
        while b < len(inv_img[0]):
            while c < len(inv_img[0][0]) - 1:
                inv_img[a][b][c] = 0
                c += 1
            c = 0
            b += 1
        b = 0
        a += 1
    print("Blueing complete")
    return inv_img


def ft_grey(array):
    ft_grey.__doc__ = "Sets green and blue channels \
        to the same value as red, to acheive grayscale"
    inv_img = (array)
    print("Beginning graying process")
    a = 0
    b = 0
    c = 1
    while a < len(inv_img):
        while b < len(inv_img[0]):
            while c < len(inv_img[0][0]):
                inv_img[a][b][c] = inv_img[a][b][0]
                c += 1
            c = 1
            b += 1
        b = 0
        a += 1
    print("Graying complete")
    return inv_img


def main():
    img = ft_load('landscape.jpg')
    mod_img = ft_grey(img)
    plt.imshow(mod_img)
    plt.show()


if __name__ == '__main__':
    main()
