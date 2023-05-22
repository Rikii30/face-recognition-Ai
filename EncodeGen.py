import cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

cred = credentials.Certificate("C:/Users/riksh/Documents/face recognition/serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancerealtime-78d8e-default-rtdb.firebaseio.com/",
    'storageBucket': "faceattendancerealtime-78d8e.appspot.com"
})

# Importing Student images into a list
folderPath = 'C:/Users/riksh/Documents/face recognition/images'
pathList = os.listdir(folderPath)
imgList = []
studentIds = []
#
for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderPath, path)))
    studentIds.append(os.path.splitext(path)[0])

    fileName = f'{folderPath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)
#
# get only the id number
#      print(os.path.splitext(path)[0])
#
print(studentIds)


def findEncodings(imagesList):
    encodeList = []

    for img in imagesList:
        # pencv library uses RGB library, and images are in BRGB, converting
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList


print("encoding started ...")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown, studentIds]
print("encoding complete")

file = open("C:/Users/riksh/Documents/face recognition/EncodeFile.p", 'wb')
pickle.dump(encodeListKnownWithIds, file)
file.close()