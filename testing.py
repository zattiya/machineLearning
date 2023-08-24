# Ziad Attiya on August 22, 2023
# code from OpenCV course - Full tutorial with Python freeCodeCamp.org

import cv2 as cv

# rescaling function
def rescaledFrame(frame, scale=0.75):
	width=int(frame.shape[1]*scale)
	height=int(frame.shape[0]*scale)
	dimensions=(width,height)
	
	return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
#end of rescaling

# reading images
image = cv.imread('/home/xiad/Desktop/ziad.jpg')
#cv.imshow('ziad chest', image) #this is full-scale
resized_image = rescaledFrame(image, scale=0.25)
cv.imshow('smaller Ziad', resized_image)
# end of reading images


#Reading and showing videos
#capture = cv.VideoCapture(0) #webcam is integer 0. You can show a saved one as follows:
capture = cv.VideoCapture('/home/xiad/Desktop/vid1.mp4') 
while True:
	isTrue, frame= capture.read()
	#reads the video, returns the frame and a boolean if the frame is read
	
	#cv.imshow ('Videp',frame)
	#this shows the full scale.
	
	frame_resized = rescaledFrame(frame, scale=0.25)
	cv.imshow('resized video', frame_resized)
	
	if cv.waitKey(20) & 0xFF==ord('d'):#if letter 'd' is pressed break
		break
		
capture.release() #release the capture pointer
cv.destroyAllWindows()
	
#end of videos




cv.waitKey(0) #wait for a specific delay

