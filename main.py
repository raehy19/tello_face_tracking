import cv2
import dlib
import time
from threading import Thread

from djitellopy import Tello

tello = Tello()

tello.connect()

keepRecording = True
tello.streamon()
frame_read = tello.get_frame_read()


# Code for initializing facial recognition (얼굴인식)
detector = dlib.get_frontal_face_detector()


def videoRecorder():
    # create a VideoWrite object, recoring to ./video.avi
    height, width, _ = frame_read.frame.shape
    print(f'height : {height} width {width}\n')
    video = cv2.VideoWriter('video.avi', cv2.VideoWriter_fourcc(*'XVID'), 30, (width, height))

    while keepRecording:
        time.sleep(1 / 30)

        frame = frame_read.frame

        # rect = detector(frame)[0]

        # print(rect)

        # Converts image to greyscale for easier detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # # 얼굴 detection
        # try:
        #
        #     # 얼굴이 있는 사각형 detect
        #
        #     # 얼굴 랜드마크 68개 점 detect
        #     face_dot = predictor(gray, rect)
        #
        #     # 점들을 리스트로 저장
        #     landmarks = []
        #     for j in range(68):
        #         x, y = face_dot.part(j).x, face_dot.part(j).y
        #         landmarks.append([x, y])
        #         # facial landmark를 빨간색 점으로 찍어서 표현
        #         cv2.circle(frame, (x, y), 1, (0, 0, 255), -1)
        # # 얼굴 인식에 실패할 경우
        # except:
        #     # 디버그 print
        #     print('Face read failed')
        #     # return {"msg": 'Face read failed'}

        # RGB_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # video.write(RGB_frame)
        # cv2.imshow('test', gray)

        try:
            cv2.imshow('test', gray)
        except Exception as e:
            print(e)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            # Press q to exit
            break

    video.release()


if __name__ == '__main__':
    # we need to run the recorder in a seperate thread, otherwise blocking options
    # would prevent frames from getting added to the video
    recorder = Thread(target=videoRecorder)
    recorder.start()

    recorder.join()
