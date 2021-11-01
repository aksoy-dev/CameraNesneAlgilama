import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy.cluster.vq import vq, kmeans
import io
import time
import time as t

from numpy import uint8
from PIL import Image

import time

stream = io.BytesIO()

import subprocess

kamera = cv2.VideoCapture(0)

while True:
    ret, image = kamera.read()

    data = np.fromstring(stream.getvalue(), uint8)

    blue_lower = np.array([100, 100, 100], np.uint8)
    blue_upper = np.array([130, 255, 255], np.uint8)

    blur = cv2.GaussianBlur(image, (5, 5), 0)  # gauss bulanikligi gerceklestirilir.
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)  # renk donusumu gerceklestirilir.
    # renkleri belirtilen sinirlar icinde ayirt etme islemi uygulanir.
    blue = cv2.inRange(hsv, blue_lower, blue_upper)

    blue = cv2.erode(blue, None, iterations=2)
    blue = cv2.dilate(blue, None, iterations=2)

    # Mavi renk icin konturlama islemi yapilir.
    _, cntr, _ = cv2.findContours(blue, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    for i, c in enumerate(cntr):
        if cv2.contourArea(c) < 1000:
            continue
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 3)
        cv2.putText(image, "HEDEF", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0))
        print(x, y)

    cv2.imshow("Ekran", image)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()
