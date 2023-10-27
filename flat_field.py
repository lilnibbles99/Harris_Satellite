
#https://helpx.adobe.com/uk/lightroom-classic/help/flat-field-correction.html

####This is for the bright field
####This needs images of even brightness to calibrate


import cv2
from os import walk
from os.path import isfile, join
from pathlib import Path
from astropy.io import fits
import numpy as np


path = Path(str(Path(__file__))[:-(len(Path(__file__).name)+1)]+str("\\images\\dark\\")) #this line took so long to write its stupid
filenames = next(walk(path),(None,None,[]))[2]
for i in range(len(filenames)):
    with fits.open("C:/Users/thegr/Desktop/WORK/year3/python data/SATELLITES/2023-01-13-1830_7-CapObj_0026.FIT") as hdu:
        image = hdu[0].data
        image = cv2.resize(image, dsize=(3840, 2160), interpolation=cv2.INTER_CUBIC)
        image = (image / 256).astype(np.uint8)

        cv2.imshow(image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


#path = Path(__file__).with_name("Dark_ASIImg_0sec_Bin1_1.4C_gain0_2023-10-23_151042_frame0008.fit")
#with path.open("r") as file:
#    print(file.read())
#files = open(os.path.join("images"))
#print("-------")
#print(os.path.join("images"))

#for file in files:
#    image = cv2.imread(file)
#    cv2.imshow(image)
#    cv2.waitkey(0)
#    cv2.destroyAllWindows()




def correction():
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


