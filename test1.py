import time
import cv2
import dlib
from threading import Thread
from djitellopy import Tello

tello = Tello()

tello.connect()

keepRecording = True
tello.streamon()
frame_read = tello.get_frame_read()

detector = dlib.get_frontal_face_detector()


def videoRecorder():
    global detector
    height, width, _ = frame_read.frame.shape

    while keepRecording:
        frame = frame_read.frame

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Converts image to greyscale for easier detection
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #
        # rect = detector(gray)

        # rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        cv2.imshow('test', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


recorder = Thread(target=videoRecorder)
recorder.start()

keepRecording = False
recorder.join()
