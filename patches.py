import numpy as np
import matplotlib.pyplot as plt 

#BASIC ARBITRARY IMAGE-SPLITTING FUNCTION, INPUT IMAGE MUST BE DIVISIBLE BY PATCH SIZE PARAMETER | EX: IMAGE SHAPE = (256, 256), PATCH_SIZE = 32


def split_into_patches(image, patch_size):

    num_slices = image.shape[0] / patch_size

    boxes = []
    boxindices = []

    for i in range(0, num_slices - 1):

        for j in range(0, num_slices - 1):

            length = i * patch_size
            width = j * patch_size

            boxes.append(image[i:i+1, j:j+1])
            boxindices.append(((i, j), (), (), ()))
            
    return boxes
