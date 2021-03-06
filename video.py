from cv2 import cv2

cap = cv2.VideoCapture('lim.mp4') # 카메라 생성
font = cv2.FONT_HERSHEY_SIMPLEX

# create the window & change the window size
cv2.namedWindow('Face')

# haar 코드 사용 (frontal_face) -> 어떤 파일을 쓰느냐에 따라 인식할 객체가 달라짐
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while(True) :
    ret, frame = cap.read()

    grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(grayframe, 1.8, 2, 0, (30, 30))

    for (x, y, w, h) in faces :
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3, 4, 0)
        cv2.putText(frame, 'Detected Face', (x - 5, y - 5), font, 0.9, (255, 255, 0), 2)

    cv2.imshow('Face', frame)

    if cv2.waitKey(300) >= 0 :
      break

    # if cv2.waitKey(1) != 255 : 
    #   break

cap.release()
cv2.destroyWindow('Face')