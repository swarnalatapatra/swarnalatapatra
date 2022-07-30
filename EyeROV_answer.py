import numpy as np
import cv2
import sys
import os

n = len(sys.argv)
if (n != 3):
    print("Usage: python answer.py path_to_image pixel_coordinate")
    exit()

# print("Continue..")
path = sys.argv[1]
px = sys.argv[2]

files = os.listdir(path)
for i in files:
    img = path + '/' +i
    print("Processing for image:", img)
    image = cv2.imread(img)
    output = image.copy()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 100)

    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        print(circles.shape)

        for (x, y, r) in circles:
            # draw the circle in the output image
            cv2.circle(output, (x, y), r, (0, 255, 0), 10)

        # cv2.imshow("gray image",gray)
        # cv2.waitKey(0)
