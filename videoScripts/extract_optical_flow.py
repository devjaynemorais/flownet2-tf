
#To execute
#python3 extract_video_framev2.py 
#Python 3.5.2
#python -m src.flownet2.test --input_a data/samples/img001.png --input_b data/samples/img002.png --out ./


import numpy as np
import cv2
import os, sys, glob
import re

#from itertools import zip_longest as zip
#from itertools import zip_longest

DIRECTORY = "videos/"
PATH = "/home/jayne/Documentos/flownet2-tf"





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

def run():
    for dir in os.listdir(DIRECTORY):
        data = []
        if os.path.isdir(os.path.join(DIRECTORY, dir)):

            #new_directory = create_directory(infile)
            vector_np = np.array([])
            #array_key = np.array([])
            #array_value = np.array([])

            print(dir)
            for file in sorted(glob.glob(os.path.join(DIRECTORY, dir, '*.png')), key=os.path.getmtime):
                data.append(file)
                #if os.path.isfile(os.path.join(DIRECTORY, dir, file)):

                    #numberFrame = (re.findall('\d+', file ))

                    #array_key = np.append(array_key, numberFrame)
                    #array_value = np.append(array_value, (os.path.join(DIRECTORY, dir, file)))
                    
                vector_np = np.append(vector_np, (file))

            print(data)

            #new_dict = {k: v for k, v in zip(array_key, array_value)}
           # new_dict = dict(zip(array_key, array_value))
            #for i in sorted (new_dict.keys()):  
            #    print((i , new_dict[i]), end = " ") 
            os.chdir('..')
            for i in range(len(vector_np)-1):
                #print((vector_np[i]) + " ----------- " + vector_np[i+1])
               #bashCommand = "cd ../.."
                print("python -m src.flownet2.test --input_a {} --input_b {} --out ./".format(str("videoScripts/"+vector_np[i]), str('videoScripts/'+vector_np[i+1])))

                #os.system(bashCommand)
                os.system("python -m src.flownet2.test --input_a {} --input_b {} --out ./".format(str("videoScripts/"+vector_np[i]), str('videoScripts/'+vector_np[i+1])))
               # print(bashCommand)
                #os.system(bashCommand)

if __name__ == '__main__':
  run()