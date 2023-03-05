import cv2
import math
import numpy as np
import face_recognition
import os
import io
import matplotlib.pyplot as plt
from datetime import datetime
from PIL import ImageGrab
from PIL import Image
from pymongo import MongoClient
from bson.binary import Binary
import matplotlib.pyplot as plt


client = MongoClient('mongodb+srv://user-5:user-5pass@cluster1.h9nlbyo.mongodb.net/test')
db = client['employee_jk']

extracted_images = db.images
image_bytes = io.BytesIO()

image = extracted_images.find()

images = []
classNames = []

for i in image:
    # print(i['id'])
    pil_img = Image.open(io.BytesIO(i['data']))
    # plt.imshow(pil_img)
    # plt.show()
    np_image = np.array(pil_img)
    images.append(np_image)
    classNames.append(i['id'])

def findEncodings(images):
    encodeList = []
    for img in images:
        # plt.imshow(img)
        # plt.show()
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


def markAttendance(name):
    with open('Attendance.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        # print(nameList)
        if str(name) not in nameList:
            now = datetime.now()
            dtString = now.date()
            tString = now.time()
            f.writelines(f'\n{int(name)},{dtString},{tString}')



encodeListKnown = findEncodings(images)
print('Encoding Complete')
# print(len(encodeListKnown))

cap = cv2.VideoCapture('C:\\Users\\hp\\Desktop\\hackit\\prac.mp4')
success, image = cap.read()

# seconds = 0.1
# fps = cap.get(cv2.CAP_PROP_FPS) # Gets the frames per second
# multiplier = seconds * fps
multiplier = 25

i = 0
while success:
    i+=1
    
    frameId = int(round(cap.get(1))) #current frame number, rounded b/c sometimes you get frame intervals which aren't integers...this adds a little imprecision but is likely good enough
    # print(frameId)
    success, img = cap.read()

    if frameId % multiplier == 0:
        print(i)
        # cv2.imwrite("FolderSeconds/frame%d.jpg" % frameId, image)
        #img = captureScreen()
        
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            # print(faceDis)
            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                name = classNames[matchIndex]
                # print(name)
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2-35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, str(name), (x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                markAttendance(name)

cap.release()
print("Completed")