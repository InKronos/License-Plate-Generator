from cv2 import cv2 as cv
from PIL import Image, ImageDraw, ImageFont, ImageOps
import numpy as np
import argparse
from zipfile import ZipFile 
import os
import smtplib
from sender2 import send_file_zipped

def get_all_file_paths(directory): 
  
    # initializing empty file paths list 
    file_paths = [] 
  
    # crawling through directory and subdirectories 
    for root, directories, files in os.walk(directory): 
        for filename in files: 
            # join the two strings in order to form the full filepath. 
            filepath = os.path.join(root, filename) 
            file_paths.append(filepath) 
  
    # returning all file paths 
    return file_paths         

def printRegistration(name):
    input = cv.imread("reg/rejestracja.png") 
    imageInPIL = Image.fromarray(np.uint8(input)).convert('RGBA')
    draw = ImageDraw.Draw(imageInPIL)
    font = ImageFont.truetype('arklatrs.ttf', 88)
    wordArray = name.split(" ")
    #print(len(wordArray[0]))
    i = 0
    r = wordArray[0]
    g = wordArray[1]
    b = wordArray[2]
    #print(r)
    (x, y) = (50, 5)
    for word in wordArray:
        if len(wordArray[3]) == 3 and i == 4 and i > 2:
            x = 230
        elif i == 4 and  len(wordArray[3]) != 3 and i > 2 and len(wordArray[4]) > 3:
            x = 210
        elif i == 4 and  len(wordArray[5]) == 1 and i > 2:
            x = 200
        if i == 5 and i > 2:
            x = 390
        if i > 2:
            message = word
            color = f'rgb({r}, {g}, {b})'
            print(color)
            draw.text((x, y), message, fill=color, font = font)
        i += 1

    
    imageInCV = np.asarray(imageInPIL)

    a = 0.13
    r = (int(imageInCV.shape[1]*a), int(imageInCV.shape[0]*a))

    imag2 = cv.resize(imageInCV, r)
    height, width = imag2.shape[:2]
    w, h = (20, 20)
    #resize image
    imageInCV = cv.resize(imageInCV, r)
    #pixelizaiz of picture
    temp = cv.resize(imageInCV, (w, h), interpolation=cv.INTER_LINEAR)
    output = cv.resize(temp, (width, height), interpolation=cv.INTER_NEAREST)
    #return imageInCV
    return output


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', action='store', dest='simple_value',
                        help='Store file value', default='dane2.txt')
    parser.add_argument('-r', action='store', dest='recipient',
                        help='Store recipient value', default='fnaticisthebest@gmail.com')
    parser.add_argument('-s', action='store', dest='sender',
                        help='Store sender value', default='i15.piorkowski@gmail.com')


    results = parser.parse_args()
    file = open(results.simple_value, "r")
    print(results.simple_value)
    i = 1
    lines = file.readlines()
    for line in lines:
        cv.imwrite(f'saved/{i}.png', printRegistration(line))
        i += 1
    
    send_file_zipped('saved', 'fnaticisthebest@gmail.com', 'i15.piorkowski@gmail.com')




