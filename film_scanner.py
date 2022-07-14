'''
python 3.10.1
script: film negative -> colour

take nagative image as input and return colour 
output (which may need to be manually tweaked)

James Philbrick, July 2022
'''

import numpy as np
from PIL import Image
from im_proc_routines import *
from logging_routines import log

# import image from 'input' folder
# 'initIm' is used for comparison and for white point 
# colour (when I expand on that feature)
im = initIm = Image.open('./input/negative_to_process.png')

# swap dimensions
imDim = (im.size[1], im.size[0])
log('Image imported: {} of size {}, colour mode is {}'.format(im.format, im.size, im.mode), newLine=True)

# convert to np array to allow for efficient processing
im = np.array(im)

def show_image(im):
    (Image.fromarray(im)).show()

def main():
    global im, imDim
    whitePoint = np.array([255/244, 255/166, 255/131])

    im = set_white_point(im, imDim, whitePoint)
    im = invert_image(im, imDim)
    
    show_image(im)

if __name__=='__main__':
    main()