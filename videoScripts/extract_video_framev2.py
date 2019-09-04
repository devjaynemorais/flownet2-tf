
import numpy as np
import cv2
#import os, sys


#files = os.listdir("/home/jayne/Documentos/ECOMAPSS/Historia")

#for infile in files:

def extract_image_one_fps():
    vidcap = cv2.VideoCapture('example1.mp4')
    count = 0
    success = True
    while success:
        #try:
        vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*1000))      
        success,image = vidcap.read()
        #print(image, success)

        ## Stop when last frame is identified
        image_last = cv2.imread("frame{}.png".format(count-1))
        
        if(np.array_equal(image, image_last) or (success == False)):
            break

        print('Saving frame{}.png'.format(count-1))
        cv2.imwrite("frame%d.png" % count, image)     # save frame as PNG file
        print('{}.sec reading a new frame: {} '.format(count,success))
        count += 1
        #except IOError:
            #print ("cannot create frame for {}".format(count)

extract_image_one_fps()