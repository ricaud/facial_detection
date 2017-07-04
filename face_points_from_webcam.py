from imutils import face_utils
import numpy as np
import argparse
import imutils
import dlib
import cv2

#constructing argument parser using 'argparse' (a native python library')
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--shape-predictor", required=True, help="path to facial landmark predictor") #shape_predictor_model.dat
#ap.add_argument("-i", "--image", required=True, help="path to image") #paul_face.png
args = vars(ap.parse_args())

#Initialize dlib's face detector, then create the facial landmark predictor
detector = dlib.get_frontal_face_detector() #just detects the face
predictor = dlib.shape_predictor(args["shape_predictor"]) #loads the landmark detector

##
#this is where we find just the face
##

#define capture device (webcam 0)
cap = cv2.VideoCapture(0)

#load image, resize, convert to grayscale
#image = cv2.imread(args["image"])
while(True):
    ret, image = cap.read()
    image = imutils.resize(image, width=500)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    rects = detector(gray, 1) #detect faces in grayscale image

    #loop over the face detections
    for(i, rect) in enumerate(rects):
        shape = predictor(gray, rect) #determine the facal landmarks for the face region 'rect' in the grayscale picture
        shape = face_utils.shape_to_np(shape) #convert landmark (X,Y) to numpy array

        (x,y,w,h) = face_utils.rect_to_bb(rect) #convert dlib rect to openCV rects
        cv2.rectangle(image, (x,y), (x+w, y+h), (0, 255, 0), 2) #now draw that rect on the image

        #TODO show face number

        #place dots on coordinates of each facial landmark
        for (x,y) in shape:
            cv2.circle(image, (x,y), 1, (0, 0, 255), -1)

    cv2.imshow("Output", image) #show the image
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
