#!/usr/bin/env python

from load_image import ft_load
import matplotlib.pyplot as plt


def main():
    main.__doc__ = "Zooms in on an image and changes to grayscale"
    image = ft_load("animal.jpeg")
    mod_image = image[100:500, 450:850, 0:1]
    
    rot_img = [[row[i] for row in mod_image] for i in range(len(mod_image[0]))]
    print(f"New shape after transpose: ({len(rot_img)}, {len(rot_img[0])}, {len(rot_img[0][0])})")
    for i in range(len(rot_img)):
        for k in range(len(rot_img[0])):
            print(rot_img[i][k])
    plt.imshow(rot_img, cmap='gray')
    plt.show()


if __name__ == '__main__':
    main()
