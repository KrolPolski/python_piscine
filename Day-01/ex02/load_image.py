#!/usr/bin/env python

import imageio.v3 as iio 


def ft_load(path: str):# -> array: #(you can return to the desired format)
    img = iio.imread(path)
    print(f"The shape of the image is {img.shape}")

ft_load("./test.jpg")