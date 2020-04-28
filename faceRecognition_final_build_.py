#Importing modules
import numpy as np 
import cv2
import pickle

#creating cascades
face_cascade = cv2.CascadeClassifier('E:/Programming utilities/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainee.yml")

labels = {"person_name": 1}

with open("labels.picel", 'rb') as f:
	og_labels = pickle.load(f)
	labels = {v:k for k,v in og_labels.items()}

cap = cv2.VideoCapture(0)
#LOOP
while True:
	ret,frame = cap.read()

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray,1.3,3)
	
	for(x,y,w,h) in faces:
		#print(x,y,w,h)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = frame[y:y+h, x:x+w]

		#recognizer
		id_, conf = recognizer.predict(roi_gray)
		if conf >= 45:
			print(labels[id_])
			font = cv2.FONT_HERSHEY_SIMPLEX
			name = labels[id_]
			color = (245,255,252)
			stroke = 2
			cv2.putText(frame,name,(x,y),font,1,color,stroke,cv2.LINE_AA)

		img_item = "final1.jpg"
		cv2.imwrite(img_item, roi_color)

		color = (255,0,0)
		stroke = 3
		width = x+w
		height = y+h 
		cv2.rectangle(frame, (x, y), (width, height), color, stroke)

	cv2.imshow("frame", frame)
	k = cv2.waitKey(30) & 0xFF 
	if k == 27:
		break

cap.release()