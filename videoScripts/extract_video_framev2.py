
#To execute
#python3 extract_video_framev2.py 
#Python 3.5.2

import numpy as np
import cv2
import os, sys
import re

DIRECTORY = "videos/"

def run():
    files = os.listdir(DIRECTORY)
    for infile in files:
        #print(infile)
        new_directory = create_directory(infile)
        extract_image_one_fps(infile, new_directory)


def create_directory(nameVideo):
    sep = '.'
    dirName = nameVideo.split(sep, 1)[0]
    dirName = DIRECTORY+dirName

    if not os.path.exists(dirName):
        os.mkdir(dirName)
        print("Directory " , dirName ,  " Created ")
    else:    
        print("Directory " , dirName ,  " already exists")

    return dirName


def extract_image_one_fps(video, new_directory):
    vidcap = cv2.VideoCapture(DIRECTORY+video)
    count = 0
    success = True

    while success:
        #try:
        vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*1000))      
        success,image = vidcap.read()
        #rint(image, success)

        ## Stop when last frame is identified
        image_last = cv2.imread("frame{}.png".format(count-1))
        
        if(np.array_equal(image, image_last) or (success == False)):
            break

        
        cv2.imwrite(new_directory+"/frame%d.png" % count, image)     # save frame as PNG file
        
        print('{}s reading a new frame: {} '.format(count,success))
        print('Saving frame{}.png'.format(count))
        count += 1
        #except IOError:
            #print ("cannot create frame for {}".format(count)

if __name__ == '__main__':
  run()