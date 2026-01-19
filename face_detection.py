import cv2
import os

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

image_path = input("Enter the path of the image: ").strip()


if not os.path.exists(image_path):
    print("Error: Image path is invalid.")
    exit()

img = cv2.imread(image_path)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.3,
    minNeighbors=5
)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

print("Number of faces detected:", len(faces))

cv2.imshow("Face Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
