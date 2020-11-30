import base64
import json

import cv2
import pickle
import numpy as np
import face_recognition
import os

encodeList = []
classNames = []


def classify_image(image_base64_data, file_path=None):
    if image_base64_data is not None:
        img = get_cv2_image_from_base64_string(image_base64_data)
    else:
        img = cv2.imread(file_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    try:
        encode = face_recognition.face_encodings(img)[0]

        r = []
        results = face_recognition.compare_faces(encodeList, encode)
        faceDis = face_recognition.face_distance(encodeList, encode)

        for i, j in enumerate(results):
            if j:
                r.append(i)

    except:
        print('Could not extract face features')
    try:
        faces_options = []
        for i in r:
            faces_options.append(faceDis[i])

        return classNames[r[np.argmin(faces_options)]]
    except:
        print("Unknown Face Detected")


def load_saved_artifacts():
    print("Loading saved artifacts... start")
    global encodeList
    global classNames

    with open("class_names.json", 'r') as f:
        classNames = json.load(f)

    encodeList = pickle.load(open("encodedList.pkl", "rb"))
    print("loading saved artifacts... done")


def get_cv2_image_from_base64_string(b64str):
    encoded_data = b64str.split(',')[1]
    nparr = np.frombuffer(base64.b64decode(encoded_data), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img


if __name__ == "__main__":
    load_saved_artifacts()

