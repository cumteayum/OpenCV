import os
import cv2
from PIL import Image 
import numpy as np
import pickle

image_dir = "E:\\Python\\OpenCv projects\\dataset"

face_cascade = cv2.CascadeClassifier('E:/Programming utilities/Lib/site-packages/cv2/data/haarcascade_frontalface_alt.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()


current_id = 0
label_ids = {}
x_train = []
y_labels = []


for root, dirs, files in os.walk(image_dir):
	for file in files:
		if file.endswith("png") or file.endswith("jpg"):
			path = os.path.join(root, file)
			label = os.path.basename(root).replace(" ", "-").lower()
			#print(label,path)
			if not label in label_ids:
				label_ids[label] = current_id
				current_id += 1

			id_ = label_ids[label]
			print(label_ids)
			#y_labels.append(label)
			#x_train.append(path)
			pil_image = Image.open(path).convert("L")
			size = (330,330)
			final_image = pil_image.resize(size,Image.ANTIALIAS)
			image_array = np.array(final_image, "uint8")
			#print(image_array)
			faces = face_cascade.detectMultiScale(image_array, 1.5, 3)

			for (x,y,w,h) in faces:
				roi = image_array[y:y+h, x:x+w]
				x_train.append(roi)
				y_labels.append(id_)

#print(y_labels)
#print(x_train)

with open("labels.picel", 'wb') as f:
	pickle.dump(label_ids, f)

recognizer.train(x_train, np.array(y_labels))
recognizer.save("trainee.yml")