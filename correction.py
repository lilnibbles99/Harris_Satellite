
#https://helpx.adobe.com/uk/lightroom-classic/help/flat-field-correction.html

####This is for the dark images
####This needs images of even brightness to calibrate



import cv2
from os import walk
from pathlib import Path
from astropy.io import fits
import numpy as np


def get_dark():
    path_dark = str(Path(__file__))[:-(len(Path(__file__).name)+1)]+str("\\images\\dark\\") #this line took so long to write its stupid
    filenames_dark = next(walk(path_dark),(None,None,[]))[2]
    return path_dark, filenames_dark


def get_flat():
    path_flat = str(Path(__file__))[:-(len(Path(__file__).name)+1)]+str("\\images\\light\\")
    filenames_flat = next(walk(path_flat),(None,None,[]))[2]
    return path_flat, filenames_flat



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



def correction_dark(path_dark,filenames_dark):
    accumulated = None
    for i in range(len(filenames_dark)):
        dark_image = get_image_dark(path_dark,filenames_dark,i)
        if accumulated is None:
            accumulated = np.zeros_like(dark_image, dtype=np.float16)
        accumulated += dark_image

    average = accumulated/len(filenames_dark)
    average = np.uint16(average)
    cv2.imshow("average dark",average)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return average



def correction_flat(path_flat,filenames_flat):
    accumulated = None
    for i in range(len(filenames_flat)):
        flat_image = get_image_flat(path_flat,filenames_flat,i)
        if accumulated is None:
            accumulated = np.zeros_like(flat_image, dtype=np.float16)
        accumulated += flat_image

    average = accumulated/len(filenames_flat)
    average = np.uint16(average)
    cv2.imshow("average flat",average)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return average



