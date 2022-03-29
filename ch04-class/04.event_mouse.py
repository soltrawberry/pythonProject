import numpy as np
import cv2

# 콜백 함수 호출은 OS, OpenCV 함수의 구현은 개발자의 몫
def onMouse(event, x, y, flags, param):  # 콜백 함수 - 이벤트 내용 출력
    if event == cv2.EVENT_LBUTTONDOWN:  # 이벤트 필드 설정
        print("마우스 왼쪽 버튼 누르기")
    elif event == cv2.EVENT_RBUTTONDOWN:
        print("마우스 오른쪽 버튼 누르기")
    elif event == cv2.EVENT_RBUTTONUP:
        print("마우스 오른쪽 버튼 떼기")
    elif event == cv2.EVENT_LBUTTONDBLCLK:
        print("마우스 왼쪽 버튼 더블클릭")

image = np.full((200, 300), 255, np.uint8)  # 초기 영상(행과 열의 집합의 개념정도로) 생성
# full 은 두번 째 인자로 자동 설정이 된다. (0~~255) 양자화 어둠->밝음

title1, title2 ='Mouse Event1', 'Mouse Event2'
cv2.imshow(title1, image)
cv2.imshow(title2, image)

cv2.setMouseCallback(title1, onMouse)  # 마우스 콜백 함수  이 title1 창에 있을 때 onMouse가 계속 활성화 된다
cv2.waitKey(0)
cv2.destroyAllWindows()