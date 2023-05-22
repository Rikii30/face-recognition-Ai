
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("C:/Users/riksh/Documents/face recognition/serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://faceattendancerealtime-78d8e-default-rtdb.firebaseio.com/"
})

ref=db.reference("students")

data={
    "13677":
        {
            "name":"Rikshitha Ravikumar",
            "major":"B.Sc IT",
            "starting_year":2020,
            "total_attendance":3,
            "standing":'B',
            "year":3,
            "last_attendance_time":"2023-1-11 00:54:34"
        },
        "13867":
        {
            "name":"Evander",
            "major":"B.Sc IT",
            "starting_year":2020,
            "total_attendance":5,
            "standing":'G',
            "year":3,
            "last_attendance_time":"2023-1-12 00:30:37"
        },
        "14818":
        {
            "name":"Sumithra",
            "major":"B.Sc IT",
            "starting_year":2020,
            "total_attendance":6,
            "standing":'G',
            "year":3,
            "last_attendance_time":"2023-1-11 00:55:34"
        },

}
for key,value in data.items():
    ref.child(key).set(value)