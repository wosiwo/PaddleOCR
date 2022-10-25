import numpy as np
import cv2
# Create a black image
img = np.zeros((200, 200, 3), np.uint8)

pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)  # 每个点都是(x, y)
pts = pts.reshape((-1, 1, 2))
cv2.polylines(img, [pts], True, (0, 255, 255))

pts = np.array([[100, 5], [150, 30], [80, 20], [90, 10]], np.int32)
cv2.polylines(img, [pts], False, (0, 255, 255))
cv2.imshow('img2', img)

cv2.waitKey()