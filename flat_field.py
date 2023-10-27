
#https://helpx.adobe.com/uk/lightroom-classic/help/flat-field-correction.html

####This is for the dark images
####This needs images of even brightness to calibrate



import cv2
from os import walk
from pathlib import Path
from astropy.io import fits
import numpy as np



path_dark = str(Path(__file__))[:-(len(Path(__file__).name)+1)]+str("\\images\\dark\\") #this line took so long to write its stupid
filenames_dark = next(walk(path_dark),(None,None,[]))[2]
file_number_dark = 0



path_flat = str(Path(__file__))[:-(len(Path(__file__).name)+1)]+str("\\images\\light\\") #this line took so long to write its stupid
filenames_flat = next(walk(path_flat),(None,None,[]))[2]
file_number_flat = 0



def get_image_dark(path_dark,filenames_dark,file_number_dark):
    with fits.open(Path(path_dark+str(filenames_dark[file_number_dark]))) as hdu:
        image = hdu[0].data
        image = cv2.resize(image, dsize=(3840, 2160), interpolation=cv2.INTER_CUBIC)
        image = (image / 256).astype(np.uint8)
        return image



def get_image_flat(path_flat,filenames_flat,file_number_flat):
    with fits.open(Path(path_flat+str(filenames_flat[file_number_flat]))) as hdu:
        image = hdu[0].data
        image = cv2.resize(image, dsize=(3840, 2160), interpolation=cv2.INTER_CUBIC)
        image = (image / 256).astype(np.uint8)
        return image



def correction_dark():
    import cv2
    import numpy as np
    import os

    directory = ""

    files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.FIT')]

    accumulated = None

    for images in files:
        image = cv2.imread(images)
        if accumulated is None:
            accumulated = np.zeros_like(image, dtype=np.float16)
        accumulated += image

    average = accumulated/len(files)
    average = np.uint16(average)
    cv2.imwrite("average.jpg",average)
    return average

####This code is for the dark field


