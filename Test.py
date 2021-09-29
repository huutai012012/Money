import cv2 as cv
import numpy as np
from keras.models import load_model

model = load_model('final_model.h5')


classes = { 0:'10k',
			1:'10k',
            2:'10k',      
            3:'10k',       
            4:'20k',      
            5:'20k',    
            6:'20k',      
            7:'20k',     
            8:'50k',    
            9:'50k',     
           10:'50k',   
           11:'50k',     
           12:'100k',     
           13:'100k',    
           14:'100k',     
           15:'100k'      }


frameWidth = 640
frameHeight = 300
cap = cv.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

while True:
	ret,img = cap.read()
	cv.imshow('img',img)
	if not ret:
		continue
	img = cv.resize(img,(128,128))
	img = np.expand_dims(img,axis=0)
	result = model.predict(img)
	kq = np.argmax(result)
	print(classes[kq],end="\t")
	print(result[0][kq])
	
	if cv.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv.destroyAllWindows()