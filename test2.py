import cv2
import dlib

cam = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector()

while True:
    check, frame = cam.read()

    rect = detector(frame)[0]

    print(rect)
    # print(rect[0], rect[0][1], rect[1][0], rect[1][1])

    cv2.imshow('video', frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cam.release()
cv2.destroyAllWindows()
