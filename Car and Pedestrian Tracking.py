import cv2

#Our Image
img_file = 'car image.jpg'

#Our pre trained car classifier
clasifier_file = ''


#create an opencv image
img = cv2.imread(img_file)


#display the image with the faces spotted
cv2.imshow('Samuel Car Detector', img)





print("Code Complete")