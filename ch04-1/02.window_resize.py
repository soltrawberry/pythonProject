import numpy as np
import cv2

image = np.zeros((200,300), np.uint8)
image.fill(255)


title1, title2 = 'AUTOSIZE' , 'NORMAL' # 윈도우 이름 변수
# normal - 하면 이미지 픽셀 하나 당 크기가 커짐. 그래서 리사이즈 한만큼 이미지 커짐
# Autosize 이미지는 그대로 유지되면서 윈도우만 커짐

cv2.namedWindow(title1, cv2.WINDOW_AUTOSIZE) # 윈도우 생성 - 크기변경X
cv2.namedWindow(title2, cv2.WINDOW_NORMAL) # 크기 변경 가능

cv2.imshow(title1, image)
cv2.imshow(title2, image)
cv2.resizeWindow(title1, 400, 300) # 윈도우 크기 변경
cv2.resizeWindow(title2, 400, 300)
cv2.waitKey(0) # key event 대기
cv2.destroyALLWindows() #열린 모든 윈도우 제거
