####Importing everything we need

#import fitparse
from astropy.io import fits
import cv2
import numpy as np
from skimage.feature import blob_log
import correction
from pathlib import Path
#import camera

####Edit these ones

threshold1 = 20/256 #150
threshold2 = 100 #100
edge1 = 50/256 #50
edge2 =  150/256 #150
minlinelength = 5 #150
maxlinegap = 50  #5
threshold3 = 0.1 #0.1

####Creating arrays early and opening the image file

coords = []
lines_list = []
x_coords = np.array([])
y_coords = np.array([])

#image = camera.take_image()

with fits.open(Path(str(Path(__file__))[:-(len(Path(__file__).name)+1)]+str("\\images\\cache\\")+str("1.FIT"))) as hdu:
#with fits.open("C:/Users/thegr/Desktop/WORK/year3/python data/SATELLITES/1.FIT") as hdu:
    image = hdu[0].data
#3840,2160
image = cv2.resize(image, dsize=(1920,1080), interpolation=cv2.INTER_CUBIC)
image = (image/256).astype(np.uint8)
cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

####For flat field correction

run = True
if run == True:
    temp = correction.get_flat()
    average_flat = correction.correction_flat(temp[0],temp[1])
    average_flat = (average_flat - (cv2.minMaxLoc(average_flat))[0])/256
    blur = cv2.GaussianBlur(image,(7,7),0)
    multiplier = (cv2.minMaxLoc(image)[1]-cv2.minMaxLoc(image)[0])/(cv2.minMaxLoc(blur)[1]-cv2.minMaxLoc(blur)[0])
    image = image/256 - average_flat*multiplier
    cv2.imshow("flat",image)

####For dark field correction

run = False
if run == True:
    average_dark = correction.correction_dark(correction.get_dark()[0],correction.get_dark()[1])
    average_dark = (average_dark - (cv2.minMaxLoc(average_dark))[0])/256
    print(cv2.minMaxLoc(average_dark))
    image = image - average_dark
    cv2.imshow("dark + flat",image)

####Making sure no pixels are negative

run = False
if run == True:
    image += cv2.minMaxLoc(image)[0]
    #(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc()
    cv2.imshow("corrected image",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

####For automatic thresholding

threshold, im_bw = cv2.threshold(image, threshold1, 255, cv2.THRESH_TOZERO)
cv2.imshow("thresholded image",im_bw)
cv2.waitKey(0)
cv2.destroyAllWindows()

####Processing the image to only caring about the boundaries of the shapes

edges = cv2.Canny((im_bw*255).astype(np.uint8), edge1, edge2, apertureSize = 3)
new_image = im_bw
cv2.destroyAllWindows()
cv2.imshow("edges",edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

####Finding any lines within the image and storing the start and end coordinates of each

lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=threshold2, minLineLength=minlinelength, maxLineGap=maxlinegap)
line_image = cv2.cvtColor(new_image.astype("uint8"), cv2.COLOR_GRAY2RGB)

####Check if lines are present

####Getting coordinates of lines

for points in lines:
    x1, y1, x2, y2 = points[0]
    line_image = cv2.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 2)
    new_image = cv2.line(im_bw, (x1, y1), (x2, y2), (0, 0, 0), 2)
    lines_list.append([(x1, y1), (x2, y2)])
cv2.imshow("new image",line_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

####Finding the coordinates of all the stars in the image and adding them to a list and grouping any coordinates or lines that are likely to be the same object

blobs = blob_log(new_image, max_sigma=30, threshold=threshold3)
color_image = cv2.cvtColor(new_image, cv2.COLOR_GRAY2RGB)
for blob in blobs:
    y, x, size = blob
    coords.append([x,y])
    center = (int(x), int(y))
    radius = int(size / 2)
    cv2.circle(color_image, center, radius, (150, 150, 255), 5)
cv2.imshow("stars",color_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

####Comparing the star map to the image in question and finding the transformation

#https://gea.esac.esa.int/archive/
#https://cdsarc.cds.unistra.fr/viz-bin/cat/J/A+A/650/A201#/article
#https://astrometry.net/use.html

####Getting the corrected equation for the line

####Converting to orbital characteristics using time

####Pulling any other characteristics from the image

####Naming the object and pushing it to the external database

####The final output of the program

print("list of lines ", lines_list)
print("list of star coordinates ", coords)
cv2.waitKey(0)
cv2.destroyAllWindows()