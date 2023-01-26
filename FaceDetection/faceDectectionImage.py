import cv2

# Pretrained data on faces
trainedFaceData = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Test image
img = cv2.imread('theOfficeCast2.jpg')

# Covert to gray scale
grayscaledImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect Faces
faceCoords = trainedFaceData.detectMultiScale(grayscaledImg)

# # Draw a rectangle around a face
# (x,y,w,h) = faceCoords[0]
# cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 10)

# Draw rectangles around multiple faces
for (x,y,w,h) in faceCoords:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 3)

# Display pic
cv2.imshow('Face Dector', img)
# wait for 6 seconds before closing
cv2.waitKey(6000)

