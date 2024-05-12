import face_recognition
import cv2
import numpy as np
import csv
import os
from datetime import datetime



alok_image = face_recognition.load_image_file("E:\\computer\\Python\\assitance\\photos\\alok.jpg")
alok_encoding = face_recognition.face_encodings(alok_image)[0]

arshad_image = face_recognition.load_image_file("E:\\computer\\Python\\assitance\\photos\\arshad.jpg")
arshad_encoding = face_recognition.face_encodings(arshad_image)[0]

binod_image = face_recognition.load_image_file("E:\\computer\\Python\\assitance\\photos\\binod.jpg")
binod_encoding = face_recognition.face_encodings(binod_image)[0]

deepak_image = face_recognition.load_image_file("E:\\computer\\Python\\assitance\\photos\\deepak.jpg")
deepak_encoding = face_recognition.face_encodings(deepak_image)[0]

gourav_image = face_recognition.load_image_file("E:\\computer\\Python\\assitance\\photos\\gourav.jpg")
gourav_encoding = face_recognition.face_encodings(gourav_image)[0]

nirmal_image = face_recognition.load_image_file("E:\\computer\\Python\\assitance\\photos\\nirmal.png")
nirmal_encoding = face_recognition.face_encodings(nirmal_image)[0]

rashika_image = face_recognition.load_image_file("E:\\computer\\Python\\assitance\\photos\\rashika.jpg")
rashika_encoding = face_recognition.face_encodings(rashika_image)[0]

ritesh_image = face_recognition.load_image_file("E:\\computer\\Python\\assitance\\photos\\ritesh.jpg")
ritesh_encoding = face_recognition.face_encodings(ritesh_image)[0]

shashi_image = face_recognition.load_image_file("E:\\computer\\Python\\assitance\\photos\\shashi2.jpg")
shashi_encoding = face_recognition.face_encodings(shashi_image)[0]



known_face_encoding = [
    alok_encoding,
    arshad_encoding,
    binod_encoding,
    deepak_encoding,
    gourav_encoding,
    nirmal_encoding,
    rashika_encoding,
    ritesh_encoding,
    shashi_encoding
]

known_faces_names = [
    "Alok Pandey",
    "Professor Arshad Ushmani",
    "Professor Binod Kumar",
    "Professor Deepak Verma",
    "Gourav Kumar",
    "Nirmal Kumar",
    "Rashika Navneet Singh",
    "Professor Ritesh Kumar",
    "Shashikant Kumar"
]

students = known_faces_names.copy()

face_locations = []
face_encodings = []
face_names = []
s = True


frame = cv2.imread('E:\\computer\\Python\\assitance\\photos\\p1.jpg')

small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
rgb_small_frame = small_frame[:, :, ::-1]

face_locations = face_recognition.face_locations(rgb_small_frame)
face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

face_names = []
for face_encoding in face_encodings:
    matches = face_recognition.compare_faces(known_face_encoding, face_encoding)
    name = ""
    face_distance = face_recognition.face_distance(known_face_encoding, face_encoding)
    best_match_index = np.argmin(face_distance)
    if matches[best_match_index]:
        name = known_faces_names[best_match_index]

print(name)