#Importing modules(`cv2`)
import cv2

#Create Cascades

face_cascade = cv2.CascadeClassifier('E:/Programming utilities/Lib/site-packages/cv2/data/haarcascade_frontalface_alt.xml')
smile = cv2.CascadeClassifier('E:/Programming utilities/Lib/site-packages/cv2/data/haarcascade_eye.xml')
cap = cv2.VideoCapture(0)

#Infinite Loop
while True:

	_, img = cap.read()

	#Converting image to grayscale and classifying facial landmarks
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray,1.1,5)
	smiles = smile.detectMultiScale(img,1.2,3)
	#Iterating through landmakrs of faces
	for (x,y,w,h) in faces:
		cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2)
	#Iterating through landmarks of eyes
	for (x,y,w,h) in smiles:
		cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255),2)

	cv2.imshow('vid', img)
	k = cv2.waitKey(30) & 0xFF 
	if k == 27:
		break
#Recognize face through given database

if (x) in range(380):
	print("Ishan - X coord")

if (y) in range(150):
	print("Ishan - Y coord")

if (w) in range(280):
	print("Ishan -- w coord")

if (h) in range(300):
		font = cv2.FONT_HERSHEY_DUPLEX
		name = "Ishan"
		color = (255,255,255)		
		stroke = 2
		cv2.putText(img,name,(x,w),font,1,color,stroke,cv2.LINE_AA)


cap.release()