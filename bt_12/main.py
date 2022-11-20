import cv2

img=cv2.imread('test.jpg')
print(img.shape)
#mg=cv2.resize(img,(800,600))
print(img.shape)
cv2.imshow("result",img)
cv2.waitKey()
