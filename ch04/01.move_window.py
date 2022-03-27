import numpy as np
import cv2

image = np.zeros((200, 400), np.uint8)
image[:] = 200  # 슬라이스 연산자로 행렬원소 값 지정 (모든 곳에 200이라는 동일 값 생성, 밝은 회색(200)바탕 영상 생성
# 0으로 초기화 된 행 200, 열 400 인 행렬 생성
# uint8타입 데이터를 갖는 원소

title1, title2 = 'position1', 'position2'  # 윈도우 이름
cv2.namedWindow(title1, cv2.WINDOW_AUTOSIZE)  # 윈도우 생성 및 크기 조정 옵션
cv2.namedWindow(title2)
cv2.moveWindow(title1, 150, 150)        # 윈도우 이동 - 위치 지정
cv2.moveWindow(title2, 400, 50)

cv2.imshow(title1, image)  # 행렬원소(회색바탕)을 영상으로 표시
cv2.imshow(title2, image)
cv2.waitKey(0)   # 키 이벤트 대기 (안하면 바로 화면 생성되었다가 꺼지는 상황발생)
cv2.destroyAllWindows() #열린 모든 윈도우 파괴