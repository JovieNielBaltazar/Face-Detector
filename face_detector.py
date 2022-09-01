import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread("id.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face= face_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5)

print(face)
for x, y, w, h in face:
    img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 225, 0), 2)


resized = cv2.resize(img, (int(img.shape[1]*1.5), int(img.shape[0]*1.5)))

cv2.imshow("Gray", resized)
cv2.waitKey(0)
cv2.destroyAllWindows