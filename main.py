from cv2 import cv2 as cv
from PIL import Image, ImageDraw, ImageFont, ImageOps
import numpy as np
import argparse
import os

def printRegistration(name):
    #reading image in openCv
    input = cv.imread("plates/LicensePlatePL.png") 
    #converting it to PIL Image
    imageInPIL = Image.fromarray(np.uint8(input)).convert('RGBA')
    draw = ImageDraw.Draw(imageInPIL)
    font = ImageFont.truetype('font/arklatrs.ttf', 88) #font and size of it

    (x, y) = (50, 5) #where string will be generated
    message = name
    color = 'rgb(0, 0, 0)' #remember when you convert to CV image program will think that you are using BGR
    draw.text((x, y), message, fill=color, font = font)

    #converting PIL Image to np array
    imageInCV = np.asarray(imageInPIL)

    a = 0.13    #size of small image
    r = (int(imageInCV.shape[1]*a), int(imageInCV.shape[0]*a))
    imag2 = cv.resize(imageInCV, r)
    height, width = imag2.shape[:2]
    w, h = (40, 40) #quality of new image (the bigger the better)
    #resize image
    imageInCV = cv.resize(imageInCV, r)
    #pixelizaiz of picture
    temp = cv.resize(imageInCV, (w, h), interpolation=cv.INTER_LINEAR)
    output = cv.resize(temp, (width, height), interpolation=cv.INTER_NEAREST)
    #return imageInCV
    return output


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', action='store', dest='fileValue',
                        help='Store file value', default='data.txt')


    results = parser.parse_args()
    file = open(results.fileValue, "r")
    i = 1
    lines = file.readlines()
    for line in lines:
        cv.imwrite(f'results/{i}.png', printRegistration(line)) #save image
        i += 1
    




