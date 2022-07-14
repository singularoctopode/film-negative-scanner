'''
This script contains the image processing functions
'''

from lib2to3.pgen2.pgen import DFAState
import numpy as np
from logging_routines import log

# take value to white balance, some average RGB values
# then find the required scaler needed to transform 
# each of these colours to 255; thus rScaler = 255/rValue
# and so on. Each of the remaining image pixels then 
# have their colour channels multiplied by their 
# corresponding scalar values. This information is succinctly
# described at https://en.wikipedia.org/wiki/Color_balance.
def set_white_point(im, imDim, whitePoint):
    log('Setting white point to {}'.format(whitePoint), newLine=False)
    for x in range(imDim[0]-1):
        for y in range(imDim[1]-1):

            rPrime = im[x][y][0] * whitePoint[0]
            gPrime = im[x][y][1] * whitePoint[1]
            bPrime = im[x][y][2] * whitePoint[2]

            if rPrime > 255: rPrime = 255
            if bPrime > 255: bPrime = 255
            if gPrime > 255: gPrime = 255

            im[x][y] = np.array([rPrime, gPrime, bPrime])
    print(' DONE')
    return im

# simply subtract each colour channel from 255
def invert_image(im, imDim):
    log('Inverting image', newLine=False)
    for x in range(imDim[0]-1):
        for y in range(imDim[1]-1):
            im[x][y] = np.array([255, 255, 255]) - im[x][y]
    print('DONE')
    return im

# find the brightest and darkest pixel in the image (where
# brightness = (R+G+B)/(255*3)). The total distance is the 
# difference between the two. Multiply each pixel by the 
# scalar: 255/distance.
def brightness_stretch(im):
    print('brightness stretch')