from ast import While
from importlib.resources import path
from tkinter import image_names
from turtle import back
import cv2
import ascii_magic
import imgkit
import os

os.mkdir("images")
os.mkdir("ascii")
os.mkdir("html")
vidObj = cv2.VidepCapture("test.mp4")
count = 0
flag = 1
while flag:
    flag, image = vidObj.read()
    try:
        cv2.imwrite("images/frames%d.jpg" % count, image)
    except:
        break
    count += 1
for i in range(count):
    e = "images/frame"+str(i)+".jpg"
    output = ascii_magic.from_image_file(
        e,
        columns = 250,
        width_ratio = 2,
        mode=ascii_magic.Modes.HTML
    )
    ascii_magic.to_html_file("html/frame"+str(i)+".html", output, additional_styles="background: #222")
path = r"D:\wkhtmltox\wkhtmltopdf\bin\wkhtmltoimage.exe"
configs = imgkit.config(wkhtmltoimage=path)
for i in range(count):
    imgkit.from_file('html/frame'+str(i)+".html", 'ascii/frame'+str(i)+".jpg", config=configs)
frame = cv2.imread("ascii/frame.jpg")
ih, iw, il = frame.shape
fourcc = cv2.VideoWriter_fourcc(*".mp4v")
video = cv2.VideoWriter("asciiVideo.mp4", fourcc, 30.00, (iw, ih))

for i in range(count):
    image = "ascii/frame"+str(i)+".jpg"
    video.write(cv2.imread(image))
cv2.destroyAllWindows()
video.release()
