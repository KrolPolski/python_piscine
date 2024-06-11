#!/usr/bin/env python

from load_image import ft_load
import matplotlib.pyplot as plt


def main():
    main.__doc__ = "Zooms in on an image and changes to grayscale"
    image = ft_load("animal.jpeg")
    mod_image = image[100:500, 450:850, 0:1]
    print(f"New shape after slicing: {mod_image.shape}")
    print(mod_image)
    plt.imshow(mod_image, cmap='gray')
    plt.show()


if __name__ == '__main__':
    main()
