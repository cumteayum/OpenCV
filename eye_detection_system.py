import cv2

face_cascade = cv2.CascadeClassifier('E:/Programming utilities/Lib/site-packages/cv2/data/haarcascade_frontalface_alt.xml')

cap = cv2.VideoCapture(0)

while True:

	_, img = cap.read()

	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray,1.1,3)

	for (x,y,w,h) in faces:
		cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0),2)

	if (x) in range(380):
		if (y) in range(150):
			if (w) in range(280):
				if (h) in range(300):
					print("Person Identified -- Ishan Nagar", "-", i)

	cv2.imshow('vid', img)
	k = cv2.waitKey(30) & 0xFF 
	if k == 27:
		break


cap.release()