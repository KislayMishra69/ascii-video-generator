from ast import While
from importlib.resources import path
from turtle import back
import cv2
import ascii_magic
import imgkit
import os

vidObj = cv2.VideoCapture("test.mp4")
count = 0
flag = 1
while flag:
    flag, image = vidObj.read()
    try:
        cv2.imwrite("images/frame%d.jpg" % count, image)
    except:
        break
    count += 1

frame = cv2.imread("ascii/frame0.jpg")
ih, iw, il= frame.shape
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
video = cv2.VideoWriter("asciiVideo.mp4", fourcc, 30.00, (iw, ih))
for i in range(count):
    image="ascii/frame"+str(i)+".jpg"
    video.write(cv2.imread(image))
cv2.destroyAllWindows()
video.capture()