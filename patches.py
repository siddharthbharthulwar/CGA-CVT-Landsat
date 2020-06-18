import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt 

class BoundingBox:

    def __init__(self, image, topleftcoord, size):

        self.image = image
        self.one = topleftcoord
        self.size = size
        self.two = (topleftcoord[0] + size, topleftcoord[1])
        self.three = (topleftcoord[0], topleftcoord[1] + size)
        self.four = (topleftcoord[0] + size, topleftcoord[1] + size)

    def getImage(self):

        return self.image

    def getCoordinates(self):

        return (self.one, self.two, self.three, self.four)

    #ORIENTATION OF COORDINATES:

    # 1 ------- 2
    # |         |
    # |         |
    # |         \
    # 3 ------- 4 

#BASIC ARBITRARY IMAGE-SPLITTING FUNCTION, INPUT IMAGE MUST BE DIVISIBLE BY PATCH SIZE PARAMETER | EX: IMAGE SHAPE = (256, 256), PATCH_SIZE = 32


def split_into_patches(image, patch_size):

    num_slices = int(image.shape[0] / patch_size)

    boxes = []
    

    for i in range(0, num_slices - 1):

        for j in range(0, num_slices - 1):

            length0 = i * patch_size
            width0 = j * patch_size

            length1 = length0 + patch_size
            width1 = width0 + patch_size

            boximg = image[length0: length1, width0: width1]

            boxes.append(BoundingBox(boximg, (width0, length0), patch_size))
  
    return boxes


img = cv.imread('square.png', cv.IMREAD_GRAYSCALE)
boxes = split_into_patches(img, 20)

for box in boxes:

    plt.imshow(box.getImage())
    plt.title(str(box.getCoordinates()))
    plt.show()