import cv2

#Our Image
img_file = 'car image.jpg'

#Our pre trained car classifier
clasifier_file = 'car_dector.xml'


#create an opencv image
img = cv2.imread(img_file)



#display the image with the faces spotted
cv2.imshow('Car Detector', img)


#Dont autoclose (Wait here in the code and listen for a key press)
cv2.waitKey()



print("Code Complete")