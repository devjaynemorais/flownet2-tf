
#To execute
#python3 extract_video_framev2.py 
#Python 3.5.2

import numpy as np
import cv2
import os, sys
import re
from itertools import zip_longest as zip

DIRECTORY = "videos/"

def run():
    
    for dir in os.listdir(DIRECTORY):
        if os.path.isdir(os.path.join(DIRECTORY, dir)):
            print(dir)
            vector_np = np.array([])
            array_key = np.array([])
            array_value = np.array([])

            for file in os.listdir(os.path.join(DIRECTORY, dir)):
                if os.path.isfile(os.path.join(DIRECTORY, dir, file)):

                    numberFrame = (re.findall('\d+', file ))

                    array_key = np.append(array_key, numberFrame)
                    array_value = np.append(array_value, (os.path.join(DIRECTORY, dir, file)))
                    
                    #vector_np = np.append(vector_np, ([numberFrame, os.path.join(DIRECTORY, dir, file)]))

            #new_dict = {k: v for k, v in zip(array_key, array_value)}
            new_dict = dict(zip(array_key, array_value))
            for i in sorted (new_dict.keys()):  
                print((i , new_dict[i]), end = " ") 

            #for i in range(len(vector_np)-1):
               # print((vector_np[i]) + " ----------- " + vector_np[i+1])
            #print(vector_np)
        

if __name__ == '__main__':
  run()