

####This should work for the camera

def take_image():
    import cv2
    exposure_time = 10000 #in ms
    camera = cv2.VideoCapture(0)
    print(camera.isOpened())
    camera.set(cv2.CAP_PROP_EXPOSURE, exposure_time)
    print(camera.get(cv2.CAP_PROP_EXPOSURE))
    stat, image = camera.read()
    if stat == True:
        cv2.imshow("image",image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    return image





import zwoasi as asi
#import time

cameras_found = asi.list_cameras()
camera = asi.Camera()
camera = asi._init_camera()
camera.get_camera_property()
camera.set_image_type(asi.ASI_IMG_RAW16)
camera.set_control_value(asi.ASI_EXPOSURE, 30)
camera.capture(filename="imagetest")
#save_control_values(filename="values", camera.get_control_values())
#camera.start_exposure()
#time.sleep(3)
#camera.stop_exposure()



#camera.isOpened()
#camera.read()

#cv2.CAP_PROP_FRAME_WIDTH
#cv2.CAP_PROP_FRAME_HEIGHT
#cv2.CAP_PROP_FPS
#cv2.CAP_PROP_AUTOFOCUS
#cv2.CAP_PROP_BRIGHTNESS
#cv2.CAP_PROP_CONTRAST
#cv2.CAP_PROP_SATURATION
#cv2.CAP_PROP_HUE
#cv2.CAP_PROP_GAIN

#num_cameras = asi.get_num_cameras()
#asi.Camera(camera_id)
#controls = camera.get_controls()
#camera.set_control_value(asi.ASI_BANDWIDTHOVERLOAD, camera.get_controls()['BandWidth']['MinValue'])
#camera.disable_dark_subtract()
#camera.set_control_value(asi.ASI_GAIN, 150)
##camera.set_control_value(asi.ASI_WB_B, 99)
#camera.set_control_value(asi.ASI_WB_R, 75)
#camera.set_control_value(asi.ASI_GAMMA, 50)
#camera.set_control_value(asi.ASI_BRIGHTNESS, 50)
#camera.set_control_value(asi.ASI_FLIP, 0)
#camera.start_video_capture()
#camera.stop_video_capture()
##camera.capture(filename=filename)
#time.sleep(sleep_interval)
#settings = camera.get_control_values()
#df = camera.get_dropped_frames()