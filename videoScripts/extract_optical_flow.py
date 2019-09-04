
#To execute
#python3 extract_video_framev2.py 
#Python 3.5.2

import numpy as np
import cv2
import os, sys
import re

DIRECTORY = "videos/"


def run():
    vector_np = []
    for name in os.listdir(DIRECTORY):
        if os.path.isdir(os.path.join(DIRECTORY, name)):
            print(name)
            for file in os.listdir(os.path.join(DIRECTORY, name)):
                if os.path.isfile(os.path.join(DIRECTORY, name, file)):
                    #rint(os.path.join(DIRECTORY, name, file))
                    vector_np.append(os.path.join(DIRECTORY, name, file))
            vector_np.sort()
            print(vector_np)
        

if __name__ == '__main__':
  run()