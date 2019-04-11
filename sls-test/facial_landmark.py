# USAGE
# python facial_landmarks.py --shape-predictor shape_predictor_68_face_landmarks.dat --image images/example_01.jpg 

# Using Dlib & iBUG300-W dataset

# import the necessary packages
from imutils import face_utils
import numpy as np
import argparse
import imutils
import dlib
import cv2
import math

# import video packages
from imutils.video import VideoStream
from imutils import face_utils
import datetime
import time

def calDegrees(p1, p2):
	"Calculate the degrees of two points"
	width = abs(p1[0] - p2[0])
	height = abs(p1[1] - p2[1])

	if height == 0:
		return 0
	elif width == 0:
		return 90
	return math.degrees(math.atan(float(height)/float(width)))

def calLength(p1, p2):
	"Calculate the length of the line made by point1, 2"
	return sqrt(pow((p1[0] - p2[0]), 2) + pow((p1[1] - p2[1]), 2))

def calRatio(l1, l2):
	"Calculate the ratio of "

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--shape-predictor", required=True,
	help="path to facial landmark predictor")
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
args = vars(ap.parse_args())

# initialize dlib's face detector (HOG-based) and then create
# the facial landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(args["shape_predictor"])


# load the input image, resize it, and convert it to grayscale
image = cv2.imread(args["image"])
image = imutils.resize(image, width=500)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# detect faces in the grayscale image
rects = detector(gray, 1)


# initialize the video stream and allow the cammera sensor to warmup
print("[Info] Camera Sensor Warming Up ...")
#vs = VideoStream(0).start()
#time.sleep(2.0)


# Make 2D array
points = [[0]*2 for i in range(200)]

size = image.shape

gray = cv2.cvtColor(image, cv2.COLOR_BRG2GRAY)

#detect faces in the gray scale frame
rects = detector(gray, 0)

# loop over the face detections
for (i, rect) in enumerate(rects):
	# determine the facial landmarks for the face region, then
	# convert the facial landmark (x, y)-coordinates to a NumPy
	# array
	shape = predictor(gray, rect)
	shape = face_utils.shape_to_np(shape)

	# convert dlib's rectangle to a OpenCV-style bounding box
	# [i.e., (x, y, w, h)], then draw the face bounding box
	(x, y, w, h) = face_utils.rect_to_bb(rect)
	
	# Print Rectangle 
	cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

	# show the face number
	cv2.putText(image, "Face #{}".format(i + 1), (x - 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

	# Point Number
	p = 1

	# loop over the (x, y)-coordinates for the facial landmarks
	# and draw them on the image
	for (x, y) in shape:
		
		points[p][0] = x;
		points[p][1] = y;		

		# Write point number to images
		'''
		cv2.putText(image, "{}".format(p), (x+2,y+2),
		cv2.FONT_HERSHEY_PLAIN, 0.5, (0, 0, 255), 1)
		'''
		
		# Write circle to images
		cv2.circle(image, (x, y), 2, (0, 255, 255), -1)
		
		# print Point
		# print ("p.{}".format(p),(x,y))
		p = p + 1
		


