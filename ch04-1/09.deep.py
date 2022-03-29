import numpy as np
import cv2

def onMouse(event, x, y, flags, param):
    global title, pt
roi1 = (50, 200, 200, 100)
roi2 = (210,50,200,100)
image[:] = (255, 255, 255)
size = (200, 100)

    if event == cv2.EVENT_LBUTTONDOWN:
        if  cv2.rectangle(image, roi1, (255, 0, 0), 2, cv2.LINE_8)
            cv2.imshow(title, image)

        else cv2.ellipse(image, pt, size, 0, 40, 250, (0, 165, 255), 4 )


    if event == cv2.EVENT_RBUTTONDOWN:
        if  cv2.rectangle(image, pt, (x, y), (255, 0, 0), 2)
            cv2.imshow(title, image)


        else


image = np.full((300, 500, 3), (255, 255, 255), np.uint8)

pt = (-1, -1)
title = "Draw Event"
cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)