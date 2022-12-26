import cv2


face_cascades = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# image = cv2.imread(r'Python/test.jpg')
# imageGrey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# faces = face_cascades.detectMultiScale(imageGrey)

# for (x, y, w, h) in faces:
#     cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

# cv2.imshow('Result', image)
# cv2.waitKey(0)


video = cv2.VideoCapture(r"Python/test.avi")
while True:
    success, frame = video.read()
    imageGrey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascades.detectMultiScale(imageGrey)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.imshow("", frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break