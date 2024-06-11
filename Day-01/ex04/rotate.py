#!/usr/bin/env python

from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def main():
    main.__doc__ = "Zooms in on an image, changes to \
                    grayscale and rotates 90 degrees"
    image = ft_load("animal.jpeg")
    mod_image = image[100:500, 450:850, 0:1]
    rot = [[row[i] for row in mod_image] for i in range(len(mod_image[0]))]
    rot_img = np.array(rot)
    print(f"New shape after transpose: {rot_img.shape}")
    print(rot_img)
    plt.imshow(rot_img, cmap='gray')
    plt.show()


if __name__ == '__main__':
    main()
