
#https://helpx.adobe.com/uk/lightroom-classic/help/flat-field-correction.html

####This is for the bright field
####This needs images of even brightness to calibrate

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


