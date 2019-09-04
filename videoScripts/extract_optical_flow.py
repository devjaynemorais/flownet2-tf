
#To execute
#python3 extract_video_framev2.py 
#Python 3.5.2

import numpy as np
import cv2
import os, sys
import re

DIRECTORY = "videos/"


def run():
    
    for dir in os.listdir(DIRECTORY):
        if os.path.isdir(os.path.join(DIRECTORY, dir)):
            print(dir)
            vector_np = np.array([])
            for file in os.listdir(os.path.join(DIRECTORY, dir)):
                if os.path.isfile(os.path.join(DIRECTORY, dir, file)):
                    #rint(os.path.join(DIRECTORY, dir, file))
                    vector_np = np.append(vector_np, os.path.join(DIRECTORY, dir, file))
            vector_np.sort()
            print(vector_np)
        

if __name__ == '__main__':
  run()