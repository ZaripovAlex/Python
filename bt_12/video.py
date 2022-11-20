import cv2

face_cascades=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# img = cv2.imread('face.jpg')

# img_gray = cv2.cvtColor (img, cv2.COLOR_BGR2GRAY)

# faces = face_cascades.detectMultiScale(img_gray)
# for (x,y,w,h) in faces:
#     cv2.rectangle(img, (x,y),(x+w, y+h),(255,0,255),2)


# cv2.imshow("result",img)

# cv2.waitKey()
 

cap = cv2.VideoCapture('video.mp4')

while True:
  _, frame = cap.read()
  cv2.imshow("camera", frame )
  img_gray = cv2.cvtColor (frame, cv2.COLOR_BGR2GRAY)
  faces = face_cascades.detectMultiScale(img_gray) 
  for (x,y,w,h) in faces:
    cv2.rectangle(frame, (x,y),(x+w, y+h),(255,0,255),2)

  cv2.imshow("result",frame)
  if cv2.waitKey(1) & 0xff ==ord('q'):
    break

