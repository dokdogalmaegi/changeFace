from cv2 import cv2
import numpy as np

text = "Found. your face!"

overlayFace = cv2.imread('1000.png', -1)

changingFace = False

secretCode = 0

init = 0

# 보통 쓰는 카메라가 0번에 등록되어 있으니 0번을 사용
cap = cv2.VideoCapture(0)
cap.set(3, 640) # 너비 (width)
cap.set(4, 480) # 높이 (height)

print('width :%d, height : %d' % (cap.get(3), cap.get(4)))

xml = 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(xml)

while(True) :
    print(init)

    if secretCode >= 4 :
        changingFace = True

    # cap.read() 함수는 재생되는 비디오의 한 프레임씩 읽습니다.
    # 비디오 프레임을 제대로 읽었다면 ret 값이 True가 되고, 실패하면 False가 됩니다.
    # 필요한 경우, ret 값을 체크하여 비디오 프레임을 제대로 읽었는지 확인할 수 있습니다.

    # 읽은 프레임은 frame에 할답됩니다.
    ret, frame = cap.read()

    # 좌우 대칭
    frame = cv2.flip(frame, 1) 

    # 예측을 하기 위해 grayscale로 조정
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 

    faces = face_cascade.detectMultiScale(gray, 1.05, 5)
    if len(faces) is not 0 :
        print("Number of faces detected : " + str(len(faces)))

    if len(faces) :
        for (x, y, w, h) in faces :
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 1)
            cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

            if changingFace :    
                changeFace = cv2.resize(overlayFace, dsize=(h, w), interpolation=cv2.INTER_LINEAR)
                y1, y2 = y, y + changeFace.shape[0]
                x1, x2 = x, x + changeFace.shape[1]

                overlayAlpha = changeFace[:, :, 3] / 255.0
                imgAlpha = 1.0 - overlayAlpha

                for c in range(0, 3) :
                    frame[y1:y2, x1:x2, c] = (overlayAlpha * changeFace[:, :, c] + imgAlpha * frame[y1:y2, x1:x2, c])

            
    
    cv2.imshow("result" , frame)

    k = cv2.waitKey(30) & 0xff

    # Esc 키를 누르면 종료
    if k == 27 :
        break

    # secretCode {
    if k == 49 :
        print("test")
        if secretCode is 0 :
            secretCode = 1

    if k == 48 :
        if secretCode >= 1 :
            secretCode += 1
    # }

    # init {
    if k == ord('b') :
        if init is 0 :
            init += 1

    if k == ord('o') :
        print(init)
        if init is 1 :
            init += 1

    if k == ord('x') :
        if init is 2 :
            changingFace = False
            init = 0
            secretCode = 0
    # }

cap.release()
cap.destroyWindow()